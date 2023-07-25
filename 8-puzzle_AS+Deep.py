#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 08:51:18 2023

@author: josemuniz
"""


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def get_blank_pos(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)

def get_neighbors(state):
    neighbors = []
    blank_pos = get_blank_pos(state)
    i, j = blank_pos
    if i > 0:
        new_state = [row[:] for row in state]
        new_state[i], new_state[i-1] = list(new_state[i]), list(new_state[i-1])
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        neighbors.append(new_state)
    if i < 2:
        new_state = [row[:] for row in state]
        new_state[i], new_state[i-1] = list(new_state[i]), list(new_state[i-1])
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        neighbors.append(new_state)
    if j > 0:
        new_state = [row[:] for row in state]
        new_state[i], new_state[i-1] = list(new_state[i]), list(new_state[i-1])
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        neighbors.append(new_state)
    if j < 2:
        new_state = [row[:] for row in state]
        new_state[i], new_state[i-1] = list(new_state[i]), list(new_state[i-1])
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        neighbors.append(new_state)
    return neighbors

def ida_star(start, goal):
    threshold = manhattan_distance(get_blank_pos(start), get_blank_pos(goal))
    path = [start]
    depth = 0
    evaluated_nodes = 0
    while True:
        result, next_threshold, eval_count = search(path, 0, threshold, goal, depth+1)
        evaluated_nodes += eval_count
        if result is not None:
            return result, evaluated_nodes, depth
        threshold = next_threshold
        depth += 1

def search(path, g, threshold, goal, depth):
    node = path[-1]
    f = g + manhattan_distance(get_blank_pos(node), get_blank_pos(goal))
    if f > threshold:
        return None, f, 1
    if node == goal:
        return path, threshold, 1
    min_threshold = float('inf')
    eval_count = 0
    for neighbor in get_neighbors(node):
        if neighbor not in path:
            path.append(neighbor)
            result, next_threshold, evals = search(path, g+1, threshold, goal, depth+1)
            eval_count += evals
            if result is not None:
                return result, next_threshold, eval_count
            if next_threshold < min_threshold:
                min_threshold = next_threshold
            path.pop()
    return None, min_threshold, eval_count


ida_star([
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]], [
    [1, 2, 3],
    [8, 0 , 4],
    [7, 6, 5]
])