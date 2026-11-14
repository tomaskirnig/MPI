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
        n_objects, n_attributes = int(nm[0]), int(nm[1])
        line_idx += 1

        matrix = []
        for _ in range(n_objects):
            matrix.append([float(x) for x in lines[line_idx].split()])
            line_idx += 1

        fuzzy_thresholds = [float(x) for x in lines[line_idx].split()]
        line_idx += 1
        support_thresholds = [float(x) for x in lines[line_idx].split()]
        line_idx += 1

        for f_thresh, s_thresh in zip(fuzzy_thresholds, support_thresholds):
            obj_to_attrs = [
                set(j for j in range(n_attributes) if matrix[i][j] >= f_thresh)
                for i in range(n_objects)
            ]
            attr_to_objs = [
                set(i for i in range(n_objects) if matrix[i][j] >= f_thresh)
                for j in range(n_attributes)
            ]

            def get_intent(objects):
                if not objects:
                    return set(range(n_attributes))
                common_attrs = set(range(n_attributes))
                for obj in objects:
                    common_attrs &= obj_to_attrs[obj]
                return common_attrs

            concepts = []

            def cbo(extent, intent, start_attr):
                if len(extent) / n_objects >= s_thresh:
                    concepts.append((extent, intent))

                for j in range(start_attr, n_attributes):
                    if j in intent:
                        continue

                    new_extent = extent & attr_to_objs[j]
                    if len(new_extent) / n_objects < s_thresh:
                        continue

                    new_intent = get_intent(new_extent)

                    is_canonical = True
                    for k in new_intent:
                        if k < j and k not in intent:
                            is_canonical = False
                            break

                    if is_canonical:
                        cbo(new_extent, new_intent, j + 1)

            all_objects = set(range(n_objects))
            cbo(all_objects, get_intent(all_objects), 0)

            concepts.sort(key=lambda c: (len(c[0]), sorted(c[0])))

            print(f"Number of concepts with support>={s_thresh:.2f} is: {len(concepts)}")
            for extent, intent in concepts:
                ext_str = ",".join(str(x) for x in sorted(extent))
                int_str = ",".join(str(x) for x in sorted(intent))
                print(f"({{{ext_str}}},{{{int_str}}})")

            rules = []

            def generate_rules(lhs, lhs_extent, start_attr):
                if lhs:
                    closure = get_intent(lhs_extent)
                    candidate_rhs = sorted(closure - set(lhs))
                    if candidate_rhs:
                        for size in range(1, len(candidate_rhs) + 1):
                            for rhs in combinations(candidate_rhs, size):
                                rules.append((lhs, rhs))

                for attr in range(start_attr, n_attributes):
                    new_extent = lhs_extent & attr_to_objs[attr]
                    if len(new_extent) > 0 and len(new_extent) / n_objects >= s_thresh:
                        generate_rules(lhs + (attr,), new_extent, attr + 1)

            generate_rules((), all_objects, 0)

            rules.sort(key=lambda r: (len(r[0]), r[0], len(r[1]), r[1]))

            print(f"Number of rules with confidence=1.00 from concepts is: {len(rules)}")
            for lhs, rhs in rules:
                lhs_str = ",".join(str(x) for x in lhs)
                rhs_str = ",".join(str(y) for y in rhs)
                print(f"{{{lhs_str}}}=>{{{rhs_str}}}")


if __name__ == "__main__":
    solve()