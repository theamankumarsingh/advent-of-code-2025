#!/usr/bin/env python3

"""Day 6 - Part 1"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"6-input.txt").read_text().splitlines()

def solve(lines):
    math_homework = [line.split() for line in lines]

    expressions = math_homework[0]
    for row in range(1,len(math_homework)-1):
        expressions = [x+" k "+y for x,y in zip(expressions, math_homework[row])]
    
    for i in range(len(expressions)):
        expressions[i] = expressions[i].replace("k", math_homework[-1][i])

    return sum([x for x in map(eval, expressions)])

if __name__ == '__main__':
    print(solve(read_input()))
