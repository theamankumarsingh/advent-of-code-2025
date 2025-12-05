#!/usr/bin/env python3

"""Day 5 - Part 2"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"5-input.txt").read_text().splitlines()

def solve(lines):
    fresh_ingredients, ingredients = [[int(x)+i for i, x in enumerate(line.split("-"))] for line in lines[:lines.index('')]], list(map(int,lines[lines.index('') + 1:]))

    range_union = []
    for a,b in sorted(fresh_ingredients):
        if range_union == []:
            range_union.append([a,b])
        else:
            if range_union[-1][1] <= a:
                range_union.append([a,b])
            else:
                range_union[-1] = [range_union[-1][0], max(range_union[-1][1], b)]
    condition = " + ".join(["len(range("+",".join(map(str, r))+"))" for r in range_union])

    return eval(condition)

if __name__ == '__main__':
    print(solve(read_input()))
