#!/usr/bin/env python3

"""Day 2 - Part 1"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"2-input.txt").read_text().splitlines()

def solve(lines):
    lines = [[int(x.split("-")[0]),int(x.split("-")[1])] for x in lines[0].split(',')]

    id_sum = 0
    for line in lines:
        for i in range(line[0], line[1]+1):
            str_i = str(i)
            if str_i[:len(str_i)//2] == str_i[len(str_i)//2:]:
                id_sum += i

    return id_sum

if __name__ == '__main__':
    print(solve(read_input()))
