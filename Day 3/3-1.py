#!/usr/bin/env python3

"""Day 3 - Part 1"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"3-input.txt").read_text().splitlines()

def solve(lines):
    output = 0

    for line in lines:
        b1=max(line[:-1])
        b2=max(line[line.index(b1)+1:])
        output+=int(b1)*10+int(b2)
    
    return output

if __name__ == '__main__':
    print(solve(read_input()))
