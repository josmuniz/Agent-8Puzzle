#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 10:03:58 2023

@author: josemuniz
"""

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def get_blank_pos(state):
    state_list = [list(state[i:i+3]) for i in range(0, 9, 3)]
    for i in range(3):
        for j in range(3):
            if state_list[i][j] == 0:
                return (i, j)

def get_neighbors(state):
    neighbors = []
    blank_pos = get_blank_pos(state)
    i, j = blank_pos
    if i > 0:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        neighbors.append(new_state)
    if i < 2:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
        neighbors.append(new_state)
    if j > 0:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
        neighbors.append(new_state)
    if j < 2:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
        neighbors.append(new_state)
    return neighbors

def ida_star(start, goal):
    threshold = manhattan_distance(get_blank_pos(start), get_blank_pos(goal))
    path = [start]
    visited_nodes = set()
    depth = 0
    while True:
        result, next_threshold, node_count = search(path, 0, threshold, goal, visited_nodes, depth)
        if result is not None:
            return result, node_count
        threshold = next_threshold

def search(path, g, threshold, goal, visited_nodes, depth):
    visited_nodes.add(tuple(tuple(row) for row in path[-1]))
    #visited_nodes.add(tuple(map(tuple, path[-1])))
    node_count = 1
    node = path[-1]
    f = g + manhattan_distance(get_blank_pos(node), get_blank_pos(goal))
    print("node", node)
    print("path", path)
    if f > threshold:
        return None, f, node_count
    if node == goal:
        return path, threshold, node_count
    min_threshold = float('inf')
    for neighbor in get_neighbors(node):
        if tuple(map(tuple, neighbor)) not in visited_nodes:
            path.append(neighbor)
            result, next_threshold, new_node_count = search(path, g+1, threshold, goal, visited_nodes, depth+1)
            node_count += new_node_count
            if result is not None:
                return result, next_threshold, node_count
            if next_threshold < min_threshold:
                min_threshold = next_threshold
            path.pop()
    return None, min_threshold, node_count

ida_star((2, 8, 3, 1, 6, 4, 7, 0, 5), (1, 2, 3, 8, 0, 4, 7, 6, 5))