import subprocess
import sys
from pathlib import Path

DU1_DIR = Path(__file__).parent
MAIN_PY = DU1_DIR / "main.py"

SAMPLE_INPUT = """2
3 3
1.0 0.8 0.2
1.0 0.8 0.9
0.1 0.1 0.9
0.5 1.0
0.5 1.0
2 3
1.0 1.0 1.0
0.8 0.9 0.7
0.5
1.0
"""

EXPECTED_OUTPUT = """Number of concepts with support>=0.50 is: 3
({0,1},{0,1})
({1,2},{2})
({0,1,2},{})
Number of rules with confidence=1.00 from concepts is: 2
{0}=>{1}
{1}=>{0}
Number of concepts with support>=1.00 is: 1
({0,1,2},{})
Number of rules with confidence=1.00 from concepts is: 0
Number of concepts with support>=1.00 is: 1
({0,1},{0,1,2})
Number of rules with confidence=1.00 from concepts is: 12
{0}=>{1}
{0}=>{2}
{0}=>{1,2}
{1}=>{0}
{1}=>{2}
{1}=>{0,2}
{2}=>{0}
{2}=>{1}
{2}=>{0,1}
{0,1}=>{2}
{0,2}=>{1}
{1,2}=>{0}
"""


def test_sample():
    proc = subprocess.run(
        [sys.executable, str(MAIN_PY)],
        input=SAMPLE_INPUT,
        text=True,
        capture_output=True,
        check=True,
    )
    actual = proc.stdout.replace("\r\n", "\n")
    expected = EXPECTED_OUTPUT.replace("\r\n", "\n")
    assert actual == expected, f"Mismatch:\nExpected:\n{expected}\nActual:\n{actual}"
    print("All tests passed!")


if __name__ == "__main__":
    test_sample()
