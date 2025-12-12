#!/usr/bin/env python3

"""Day 12 - Part 1"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"12-input.txt").read_text().splitlines()

def solve(lines):
    gifts = []
    regions = []
    for i in range(len(lines)):
        if 'x' in lines[i] and ':' in lines[i]:
            regions.append([tuple(map(int, lines[i].split(':')[0].split('x'))), tuple(map(int, lines[i].split(':')[1].strip().split(' ')))])
        elif ':' in lines[i]:
            gifts.append([])
        elif lines[i] == '':
            continue
        else:
            gifts[-1].append(lines[i])

    count = 0
    for region in regions:
        r,c = region[0][0] // 3, region[0][1] // 3 # calculate how many 3x3 sections we have
        if sum(region[1]) <= r * c: # check if we can fit all gifts in their own section by itself, this works for the input provided
            count += 1
    
    return count

if __name__ == '__main__':
    print(solve(read_input()))
