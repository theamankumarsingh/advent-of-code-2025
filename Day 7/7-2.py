#!/usr/bin/env python3

"""Day 7 - Part 2"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"7-input.txt").read_text().splitlines()

def solve(lines):
    lines = [list(line) for line in lines]

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '.':
                if type(lines[i-1][j]) == int:
                    lines[i][j] = lines[i-1][j]
                elif lines[i-1][j] == 'S':
                    lines[i][j] = 1
            elif type(lines[i][j]) == int:
                if type(lines[i-1][j]) == int:
                    lines[i][j] += lines[i-1][j] # convergence of rays from above
            elif lines[i][j] == '^' and type(lines[i-1][j]) == int:
                if lines[i][j-1] == '.':
                    lines[i][j-1] = lines[i-1][j]
                elif type(lines[i][j-1]) == int:
                    lines[i][j-1] += lines[i-1][j] # convergence of rays from left
                if lines[i][j+1] == '.':
                    lines[i][j+1] = lines[i-1][j]
                elif type(lines[i][j+1]) == int:
                    lines[i][j+1] += lines[i-1][j] # convergence of rays from right

    return sum([c for c in lines[-1] if type(c) == int])

if __name__ == '__main__':
    print(solve(read_input()))
