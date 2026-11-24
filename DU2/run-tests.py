#!/usr/bin/env python3

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional, List, Union

# Usage: python3 run-tests.py [<path-to-binary> | <DU2.csproj> | <Program.cs>] [--exact]
# Example: python3 run-tests.py
# Example: python3 run-tests.py ./DU2.csproj

CURRENT_DIR = Path(__file__).absolute().parent


def resolve_path(test_name: str, path: str) -> Path:
    return CURRENT_DIR / test_name / path


class Failure:
    pass


class WrongExitCode(Failure):
    def __init__(self, expected: int, actual: int):
        self.expected = expected
        self.actual = actual


class StreamMismatch(Failure):
    def __init__(self, stream: str, expected: Path, actual: Path, reason: str = ""):
        self.stream = stream
        self.expected = expected
        self.actual = actual
        self.reason = reason


class OutputFileMissing(Failure):
    def __init__(self, name: str):
        self.name = name


class OutputFileMismatch(Failure):
    def __init__(self, name: str, expected: Path, actual: Path):
        self.name = name
        self.expected = expected
        self.actual = actual


def read_file(path: Path) -> str:
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def files_equal(file_a: Path, file_b: Path) -> bool:
    return read_file(file_a) == read_file(file_b)


def match_assignment_output(act_str: str, exp_str: str) -> tuple[bool, str]:
    act_lines = [l.strip() for l in act_str.strip().splitlines() if l.strip()]
    exp_lines = [l.strip() for l in exp_str.strip().splitlines() if l.strip()]
    if len(act_lines) != len(exp_lines):
        return False, f"Line count mismatch (got {len(act_lines)}, expected {len(exp_lines)})"

    for idx, (a, e) in enumerate(zip(act_lines, exp_lines)):
        if a.startswith("Case "):
            if a != e:
                return False, f"Header mismatch on line {idx + 1}: '{a}' != '{e}'"
        elif a.startswith("Minima "):
            try:
                a_parts = dict(p.split("=") for p in a[7:].split())
                e_parts = dict(p.split("=") for p in e[7:].split())
            except Exception:
                return False, f"Malformed Minima on line {idx + 1}: '{a}'"

            if a_parts.get("PCA") != e_parts.get("PCA"):
                return False, f"Minima PCA mismatch: got {a_parts.get('PCA')}, expected {e_parts.get('PCA')}"
            if a_parts.get("MDS") != e_parts.get("MDS"):
                return False, f"Minima MDS mismatch: got {a_parts.get('MDS')}, expected {e_parts.get('MDS')}"
            try:
                rp_val = int(a_parts.get("RP", -99))
                if rp_val < -1:
                    return False, f"Invalid RP minima: {rp_val}"
            except ValueError:
                return False, f"Non-integer RP minima on line {idx + 1}: '{a_parts.get('RP')}'"
        else:
            a_toks = a.split()
            e_toks = e.split()
            if len(a_toks) != 8 or len(e_toks) != 8:
                return False, f"Expected 8 columns on line {idx + 1}, got {len(a_toks)}"
            if a_toks[0] != e_toks[0]:
                return False, f"Dimension mismatch on line {idx + 1}: got {a_toks[0]}, expected {e_toks[0]}"
            # Verify PCA & MDS metrics (indices 1 to 5) with tolerance 1e-4
            for c in range(1, 6):
                try:
                    diff = abs(float(a_toks[c]) - float(e_toks[c]))
                    if diff > 1.0001e-4:
                        return False, f"Col {c + 1} mismatch on line {idx + 1}: got {a_toks[c]}, expected {e_toks[c]} (diff {diff:.6f})"
                except ValueError:
                    return False, f"Invalid number '{a_toks[c]}' on line {idx + 1}"
            # Verify RP stress (index 6): finite and non-negative
            try:
                s_rp = float(a_toks[6])
                if s_rp < 0.0 or not (-1e10 < s_rp < 1e10):
                    return False, f"Invalid RP stress on line {idx + 1}: {s_rp}"
            except ValueError:
                return False, f"Invalid RP stress on line {idx + 1}: '{a_toks[6]}'"
            # Verify RP concentration (index 7): -1.0000 or in [0, 1]
            try:
                k_rp = float(a_toks[7])
                if abs(k_rp - (-1.0)) > 1e-4 and not (0.0 <= k_rp <= 1.0 + 1e-6):
                    return False, f"Invalid RP concentration on line {idx + 1}: {k_rp}"
            except ValueError:
                return False, f"Invalid RP concentration on line {idx + 1}: '{a_toks[7]}'"
    return True, "OK"


def streams_equal(actual: Path, expected: Path, stream: str, exact: bool = False) -> tuple[bool, str]:
    if exact or stream != "stdout":
        match = files_equal(actual, expected)
        return match, "" if match else "Exact string mismatch"
    return match_assignment_output(read_file(actual), read_file(expected))


def get_test_workdir(name: str) -> Path:
    return resolve_path(name, "workdir")


def relative_path(path: Path) -> Path:
    try:
        return path.relative_to(os.getcwd())
    except ValueError:
        return path


def calculate_diff(workdir: Path, name: str, expected: Path, actual: Path, indent: str) -> str:
    from difflib import unified_diff

    diff_path = workdir / f"{name}.diff"
    expected_lines = read_file(expected).splitlines(keepends=True)
    actual_lines = read_file(actual).splitlines(keepends=True)
    diff = "".join(
        unified_diff(expected_lines, actual_lines, fromfile=str(expected), tofile=str(actual))
    )
    with open(diff_path, "w", encoding="utf-8") as diff_file:
        diff_file.write(diff)

    return f"""
{indent}Expected file: {relative_path(expected)}
{indent}Actual file: {relative_path(actual)}
{indent}Diff: {relative_path(diff_path)}"""


def run_test(
    binary: Union[str, List[str]],
    name: str,
    title: str | None = None,
    args: List[str] | None = None,
    stdin: str | None = None,
    stdout: str | None = None,
    stderr: str | None = None,
    exit_code: int = 0,
    files_in: List[str] | None = None,
    files_out: List[str] | None = None,
    exact: bool = False,
):
    workdir = get_test_workdir(name)
    shutil.rmtree(workdir, ignore_errors=True)
    os.makedirs(workdir, exist_ok=True)

    args = args or []
    files_in = files_in or []
    files_out = files_out or []

    for file in files_in:
        shutil.copy(resolve_path(name, file), workdir)

    actual_stdout = workdir / "actual-stdout"
    actual_stderr = workdir / "actual-stderr"

    command = (binary if isinstance(binary, list) else [binary]) + args

    with open(actual_stdout, "wb") as stdout_file:
        with open(actual_stderr, "wb") as stderr_file:
            stdin_file = (
                open(resolve_path(name, stdin), "rb") if stdin is not None else subprocess.DEVNULL
            )
            result = subprocess.run(
                command, stdin=stdin_file, stdout=stdout_file, stderr=stderr_file, cwd=workdir
            )

    if stderr is None and os.path.exists(actual_stderr) and os.path.getsize(actual_stderr) == 0:
        os.unlink(actual_stderr)
    if stdout is None and os.path.exists(actual_stdout) and os.path.getsize(actual_stdout) == 0:
        os.unlink(actual_stdout)
    if stdin is not None:
        stdin_file.close()

    if result.returncode != exit_code:
        yield WrongExitCode(expected=exit_code, actual=result.returncode)

    def check_stream(path: Optional[str], actual: Path, stream: str):
        if path is not None:
            expected = resolve_path(name, stream)
            matched, reason = streams_equal(actual, expected, stream, exact=exact)
            if not matched:
                yield StreamMismatch(stream=stream, expected=expected, actual=actual, reason=reason)

    yield from check_stream(stdout, actual_stdout, "stdout")
    yield from check_stream(stderr, actual_stderr, "stderr")

    for file in files_out:
        actual_file = workdir / file
        expected_file = resolve_path(name, file)
        if not actual_file.is_file():
            yield OutputFileMissing(file)
        elif not files_equal(actual_file, expected_file):
            yield OutputFileMismatch(file, expected=expected_file, actual=actual_file)


exact_mode = "--exact" in sys.argv
non_flag_args = [a for a in sys.argv[1:] if a != "--exact"]

if not non_flag_args:
    # Auto-detect C# project
    csproj_files = list(CURRENT_DIR.glob("*.csproj"))
    if csproj_files:
        binary_cmd = ["dotnet", "run", "--project", str(csproj_files[0].resolve()), "--"]
    elif (CURRENT_DIR / "Program.cs").exists():
        binary_cmd = ["dotnet", "run", "--project", str(CURRENT_DIR.resolve()), "--"]
    else:
        print("Usage: python3 run-tests.py [<path-to-binary> | <DU2.csproj> | <Program.cs>] [--exact]")
        sys.exit(1)
else:
    target = non_flag_args[0]
    p = Path(target).resolve()
    if target.endswith(".csproj") or (p.is_dir() and list(p.glob("*.csproj"))):
        binary_cmd = ["dotnet", "run", "--project", str(p), "--"]
    elif target.endswith(".cs"):
        binary_cmd = ["dotnet", "run", "--project", str(p.parent), "--"]
    elif target.endswith(".dll"):
        binary_cmd = ["dotnet", str(p)]
    elif " " in target:
        import shlex
        binary_cmd = shlex.split(target)
    else:
        binary_cmd = [str(p) if p.exists() else target]

# Discover test directories
test_dirs = sorted(
    [d for d in CURRENT_DIR.iterdir() if d.is_dir() and d.name.startswith("test") and (d / "stdin").exists()],
    key=lambda d: d.name
)

tests = []
if test_dirs:
    for td in test_dirs:
        tests.append({
            'name': td.name,
            'title': td.name,
            'exit_code': 0,
            'args': [],
            'stdin': 'stdin',
            'stdout': 'stdout' if (td / 'stdout').exists() else None,
            'stderr': None,
            'files_in': [],
            'files_out': [],
            'exact': exact_mode
        })
else:
    tests.append({
        'name': 'test0',
        'title': 'test0',
        'exit_code': 0,
        'args': [],
        'stdin': 'stdin',
        'stdout': 'stdout',
        'stderr': None,
        'files_in': [],
        'files_out': [],
        'exact': exact_mode
    })

indent = " " * 4
passed = 0
for test in tests:
    failures = list(run_test(binary_cmd, **test))
    title = test.get("title", test["name"])
    label = f"Test {title}: "
    print(f"{label:<60}", end="")
    if len(failures) == 0:
        print("SUCCESS")
        passed += 1
    else:
        workdir = get_test_workdir(test["name"])
        print("FAILURE")
        for failure in failures:
            if isinstance(failure, WrongExitCode):
                print(f"{indent}- Wrong exit code, expected {failure.expected}, actual {failure.actual}")
            elif isinstance(failure, OutputFileMissing):
                print(f"{indent}- Missing output file `{failure.name}`")
            elif isinstance(failure, OutputFileMismatch):
                diff = calculate_diff(workdir, failure.name, expected=failure.expected, actual=failure.actual, indent=indent + "  ")
                print(f"{indent}- Output file `{failure.name}` has wrong contents. {diff}")
            elif isinstance(failure, StreamMismatch):
                diff = calculate_diff(workdir, failure.stream, expected=failure.expected, actual=failure.actual, indent=indent + "  ")
                reason_str = f" Reason: {failure.reason}" if failure.reason else ""
                print(f"{indent}- `{failure.stream}` has wrong contents.{reason_str} {diff}")

total_tests = len(tests)
print()
print(f"Passed {passed}/{total_tests} test(s) ({(passed / total_tests) * 100.0:.0f} %)")
if passed == total_tests:
    print("All tests have passed")
else:
    print("Some tests have failed")
    sys.exit(1)
