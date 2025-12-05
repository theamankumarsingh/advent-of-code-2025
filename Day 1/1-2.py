#!/usr/bin/env python3

"""Day 1 - Part 2"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"1-input.txt").read_text().splitlines()

def solve(lines):
    dial = 50
    count = 0
    for line in lines:
        starting_dial = dial
        if line[0] == "L":
            dial -= int(line[1:])%100 # To account for full rotations
            count += int(line[1:])//100 # The 0 is encountered once every full rotation
        else:
            dial += int(line[1:])%100
            count += int(line[1:])//100
        if dial < 0:
            dial += 100
            if starting_dial != 0: # Checks if the dial was already at 0, to avoid duplicate counting
                count += 1
        elif dial > 99:
            dial -= 100
            if dial != 0: # Checks if the current dial is at 0, to avoid duplicate counting
                count += 1
        if dial == 0:
            count += 1

    return count

if __name__ == '__main__':
    print(solve(read_input()))
