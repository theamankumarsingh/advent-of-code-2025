#!/usr/bin/env python3

"""Day 10 - Part 1"""

from pathlib import Path
from itertools import combinations

def read_input():
    return Path(__file__).with_name(f"10-input.txt").read_text().splitlines()

def solve(lines):
    lines = [line.split() for line in lines if line.split()]

    machines = []
    for line in lines:
        machine = []
        machine.append("".join('1' if x == "#" else '0' for x in list(line)[0][1:-1]))
        length = len(machine[0])
        for button in line[1:-1]:
            btn = eval(button)
            if type(btn) is int:
                machine.append("".join('1' if x == btn else '0' for x in range(length)))
            else:
                machine.append("".join('1' if x in btn else '0' for x in range(length)))
        machines.append(machine)

    sum_toggles = 0
    for machine in machines:
        for i in range(len(machine[1:])):
            flag = 0
            operation = list(combinations(machine[1:], i + 1))
            for sequence in operation:
                res = "0"*len(machine[0])
                for op in sequence:
                    res = bin(int(res, 2) ^ int(op,2))[2:].zfill(len(machine[0])) # XOR operation for toggling
                if res == machine[0]:
                    flag = 1
                    break
            if flag:
                sum_toggles += i + 1
                break

    return sum_toggles

if __name__ == '__main__':
    print(solve(read_input()))
