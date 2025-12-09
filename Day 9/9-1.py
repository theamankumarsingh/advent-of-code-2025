#!/usr/bin/env python3

"""Day 9 - Part 1"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"9-input.txt").read_text().splitlines()

def solve(lines):
    lines = [list(map(int, line.split(","))) for line in lines]
    lines = sorted(lines, key=lambda x: x[0])

    a = lambda x,y: (abs(x[0]-y[0])+1) * (abs(x[1]-y[1])+1)
    area_pairs = []
    for i in range(len(lines)-1):
        for j in range(i+1, len(lines)):
            area_pairs.append((a(lines[i], lines[j]), [lines[i], lines[j]]))
    area_pairs = sorted(area_pairs, key=lambda x: x[0], reverse=True)

    return area_pairs[0][0]

if __name__ == '__main__':
    print(solve(read_input()))
