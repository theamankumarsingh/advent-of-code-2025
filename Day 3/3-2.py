#!/usr/bin/env python3

"""Day 3 - Part 2"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"3-input.txt").read_text().splitlines()

def solve(lines):
    output = 0

    for line in lines:
        digits = []
        bank = line

        for i in range(11,0,-1):
            digits.append(max(bank[:-i]))
            bank = bank[bank.index(digits[-1])+1:]
        else:
            digits.append(max(bank[:]))

        output += int(''.join(digits))

    return output

if __name__ == '__main__':
    print(solve(read_input()))
