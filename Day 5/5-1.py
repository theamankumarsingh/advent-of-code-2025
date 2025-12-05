#!/usr/bin/env python3

"""Day 5 - Part 1"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"5-input.txt").read_text().splitlines()

def solve(lines):
    fresh_ingredients, ingredients = ["ingredient in range(" + ",".join(line.split("-"))+"+1)" for line in lines[:lines.index('')]], list(map(int,lines[lines.index('') + 1:]))

    count = 0
    condition = " or ".join(fresh_ingredients)
    for ingredient in ingredients:
        if eval(condition):
            count+=1

    return count

if __name__ == '__main__':
    print(solve(read_input()))
