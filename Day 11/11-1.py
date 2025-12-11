#!/usr/bin/env python3

"""Day 11 - Part 1"""

from pathlib import Path

count = 0

def read_input():
    return Path(__file__).with_name(f"11-input.txt").read_text().splitlines()

def count_paths(graph, start, end):
    global count
    for value in graph[start]:
        if value == end:
            count += 1
        else:
            count_paths(graph, value, end)

def solve(lines):
    lines = dict([[line.split(":")[0],line.split(":")[1].split()] for line in lines])

    count_paths(lines, 'you', 'out')

    return count

if __name__ == '__main__':
    print(solve(read_input()))
