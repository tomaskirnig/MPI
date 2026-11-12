#!/usr/bin/env python3
import sys
from itertools import combinations


def solve():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return

    line_idx = 0
    num_tests = int(lines[line_idx])
    line_idx += 1

    for _ in range(num_tests):
        nm = lines[line_idx].split()
        num_objects, num_attributes = int(nm[0]), int(nm[1])
        line_idx += 1

        matrix = []
        for _ in range(num_objects):
            matrix.append([float(x) for x in lines[line_idx].split()])
            line_idx += 1

        fuzzy_thresholds = [float(x) for x in lines[line_idx].split()]
        line_idx += 1
        support_thresholds = [float(x) for x in lines[line_idx].split()]
        line_idx += 1

        for f_thresh, s_thresh in zip(fuzzy_thresholds, support_thresholds):
            # 1. Binary incidence matrix for threshold f
            obj_attrs = [
                set(j for j in range(num_attributes) if matrix[i][j] >= f_thresh)
                for i in range(num_objects)
            ]
            attr_objs = [
                set(i for i in range(num_objects) if matrix[i][j] >= f_thresh)
                for j in range(num_attributes)
            ]

            # Derivation operator (objects -> attributes)
            def up(objs):
                if not objs:
                    return set(range(num_attributes))
                res = set(range(num_attributes))
                for i in objs:
                    res &= obj_attrs[i]
                return res

            # 2. Formal concepts using Close-by-One (CbO)
            concepts = []

            def cbo(extent, intent, start_attr):
                if len(extent) / num_objects >= s_thresh:
                    concepts.append((extent, intent))
                for j in range(start_attr, num_attributes):
                    if j in intent:
                        continue
                    new_extent = extent & attr_objs[j]
                    if len(new_extent) / num_objects < s_thresh:
                        continue
                    new_intent = up(new_extent)
                    # Canonical test: no smaller attribute was added unless already in intent
                    if all(k >= j or k in intent for k in new_intent):
                        cbo(new_extent, new_intent, j + 1)

            all_objects = set(range(num_objects))
            cbo(all_objects, up(all_objects), 0)

            # Sort concepts: 1. size of extent, 2. extent elements lexicographically
            concepts.sort(key=lambda c: (len(c[0]), sorted(c[0])))

            print(f"Number of concepts with support>={s_thresh:.2f} is: {len(concepts)}")
            for ext, intent in concepts:
                ext_str = ",".join(str(x) for x in sorted(ext))
                int_str = ",".join(str(x) for x in sorted(intent))
                print(f"({{{ext_str}}},{{{int_str}}})")

            # 3. Association rules (support >= s, confidence == 1)
            rules = []

            def find_rules(curr_X, curr_ext, start):
                if curr_X:
                    closure = up(curr_ext)
                    diff = sorted(closure - set(curr_X))
                    if diff:
                        for r in range(1, len(diff) + 1):
                            for Y in combinations(diff, r):
                                rules.append((curr_X, Y))
                for j in range(start, num_attributes):
                    new_ext = curr_ext & attr_objs[j]
                    # Monotonic pruning: LHS must cover >= 1 object and meet support threshold
                    if len(new_ext) > 0 and len(new_ext) / num_objects >= s_thresh:
                        find_rules(curr_X + (j,), new_ext, j + 1)

            find_rules((), all_objects, 0)

            # Sort rules: 1. len(X), 2. X, 3. len(Y), 4. Y
            rules.sort(key=lambda r: (len(r[0]), r[0], len(r[1]), r[1]))

            print(f"Number of rules with confidence=1.00 from concepts is: {len(rules)}")
            for X, Y in rules:
                x_str = ",".join(str(x) for x in X)
                y_str = ",".join(str(y) for y in Y)
                print(f"{{{x_str}}}=>{{{y_str}}}")


if __name__ == "__main__":
    solve()
