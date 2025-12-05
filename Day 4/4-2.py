#!/usr/bin/env python3

"""Day 4 - Part 2"""

from pathlib import Path

def read_input():
    return Path(__file__).with_name(f"4-input.txt").read_text().splitlines()

def solve(lines):
    matrix = [list(map(lambda x: 0 if x == "." else 1, line)) for line in lines] # replacing '.' with 0 and '@' with 1 for direct calculations
    matrix = [[0]*(len(matrix[0])+2)] + [[0] + row + [0] for row in matrix] + [[0]*(len(matrix[0])+2)] # Add padding to matrix

    count = 0
    while True: # Repeat until no more changes
        changed_indices = [] # To track which cells to change
        for r in range(1,len(matrix)-1):
            for c in range(1,len(matrix[0])-1):
                if matrix[r][c]==0:
                    continue
                submatrix = [row[c-1:c+2] for row in matrix[r-1:r+2]] # Extract 3x3 submatrix
                if sum([sum(row) for row in submatrix]) <= 4: # Includes the center cell, thus has to be <= 4 instead of < 4
                    changed_indices.append((r,c))
                    count += 1
        if not changed_indices:
            break
        for r,c in changed_indices:
            matrix[r][c] = 0
    
    return count

if __name__ == '__main__':
    print(solve(read_input()))
