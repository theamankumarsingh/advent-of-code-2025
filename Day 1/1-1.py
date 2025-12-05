#!/usr/bin/env python3

"""Day 1 - Part 1"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"1-input.txt").read_text().splitlines()

def solve(lines):
    dial = 50
    count = 0
    for line in lines:
        if line[0] == "L":
            dial -= int(line[1:])%100 # To account for full rotations
        else:
            dial += int(line[1:])%100
        if dial < 0:
            dial += 100
        elif dial > 99:
            dial -= 100
        if dial == 0:
            count += 1

    return count

if __name__ == '__main__':
    print(solve(read_input()))
