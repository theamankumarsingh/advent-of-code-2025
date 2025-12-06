#!/usr/bin/env python3

"""Day 6 - Part 2"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"6-input.txt").read_text().splitlines()

def solve(lines):
    math_homework = [list(line) for line in lines]
    operators = list("".join(math_homework[-1]).replace(" ", ""))

    expressions = []
    parsed_math_homework = math_homework[0]
    for row in range(1, len(math_homework)-1):
        parsed_math_homework = [ x+y for x,y in  zip(parsed_math_homework, math_homework[row])]
    parsed_math_homework.append(' ')
    
    e = ""
    for i in range(len(parsed_math_homework)):
        if set(parsed_math_homework[i]) == {' '}:
            expressions.append(e[:-3])
            e = ""
        else:
            e += parsed_math_homework[i] + " k "

    return sum([x for x in map(lambda x: eval(x.replace("k", operators.pop(0))), expressions)])

if __name__ == '__main__':
    print(solve(read_input()))
