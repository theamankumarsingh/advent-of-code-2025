#!/usr/bin/env python3

"""Day 2 - Part 2"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"2-input.txt").read_text().splitlines()

def solve(lines):
    lines = [[int(x.split("-")[0]),int(x.split("-")[1])] for x in lines[0].split(',')]

    id_sum = 0
    for line in lines:
        for i in range(line[0], line[1]+1):
            str_i = str(i)
            for k in range(2,len(str_i)+1):
                if len(str_i) % k:
                    continue
                part_len = len(str_i) // k
                parts = [str_i[j*part_len:(j+1)*part_len] for j in range(k)] # split str_i into k equal parts and check if all parts are equal
                if all(part == parts[0] for part in parts):
                    id_sum += i
                    break

    return id_sum

if __name__ == '__main__':
    print(solve(read_input()))
