#!/usr/bin/env python3

"""Day 8 - Part 2"""

from pathlib import Path
import math

def read_input():
    return Path(__file__).with_name(f"8-input.txt").read_text().splitlines()

def solve(lines):
    lines = [tuple(map(int, l.split(","))) for l in lines]
    lines = sorted(lines)

    d = lambda x,y: ((x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2)**0.5
    distance_pairs = []
    for i in range(len(lines)-1):
        for j in range(i+1,len(lines)):
            distance_pairs.append((d(lines[i], lines[j]), [lines[i], lines[j]]))
    distance_pairs = sorted(distance_pairs, key=lambda x: x[0])

    cluster = []
    final_connection = None
    for dist, points in distance_pairs:
        disjoint_cluster = []
        common_cluster = set()
        for i in range(len(cluster)):
            if points[0] in cluster[i] or points[1] in cluster[i]: # check if either point is in the cluster
                common_cluster = common_cluster.union(cluster[i])
                common_cluster = common_cluster.union(points)
            else:
                disjoint_cluster.append(cluster[i]) # if not, keep the cluster as is
        if common_cluster:
            disjoint_cluster.append(list(common_cluster)) # add the merged cluster
        else:
            disjoint_cluster.append(points) # create a new cluster
        cluster = disjoint_cluster # update clusters
        if len(cluster) == 1:
            if len(cluster[0]) == len(lines): # all points are connected
                final_connection = points
                break

    return math.prod([p[0] for p in final_connection])

if __name__ == '__main__':
    print(solve(read_input()))
