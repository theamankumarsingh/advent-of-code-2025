#!/usr/bin/env python3

"""Day 11 - Part 2"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"11-input.txt").read_text().splitlines()

def count_paths(graph, start, end, memo=None): # momoization to optimize repeated calculations
    if memo is None:
        memo = {}
    if start == end:
        return 1
    if start not in graph:
        return 0
    if start in memo:
        return memo[start]
    count = 0
    for value in graph[start]:
        if value == end:
            count += 1
        else:
            count += count_paths(graph, value, end, memo)
    memo[start] = count
    return count

def solve(lines):
    lines = dict([[line.split(":")[0],line.split(":")[1].split()] for line in lines])

    return count_paths(lines, 'svr', 'fft')*count_paths(lines, 'fft', 'dac')*count_paths(lines, 'dac', 'out') + count_paths(lines, 'svr', 'dac')*count_paths(lines, 'dac', 'fft')*count_paths(lines, 'fft', 'out')

if __name__ == '__main__':
    print(solve(read_input()))
