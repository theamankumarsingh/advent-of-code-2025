#!/usr/bin/env python3

"""Day 7 - Part 1"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"7-input.txt").read_text().splitlines()

def solve(lines):
    lines = [list(line) for line in lines]
    count = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '.':
                if lines[i-1][j] in ('S', '|'):
                    lines[i][j] = '|'
            elif lines[i][j] == '^' and lines[i-1][j] == '|':
                count += 1
                if lines[i][j-1] == '.':
                    lines[i][j-1] = '|'
                if lines[i][j+1] == '.':
                    lines[i][j+1] = '|'
    
    return count

if __name__ == '__main__':
    print(solve(read_input()))
