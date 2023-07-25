#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 07:20:58 2023

@author: josemuniz
"""

import heapq

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
        neighbors.append(tuple(map(tuple, new_state)))
    if i < 2:
        new_state = [row[:] for row in state]
        new_state[i], new_state[i-1] = list(new_state[i]), list(new_state[i-1])
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        neighbors.append(tuple(map(tuple, new_state)))
    if j > 0:
        new_state = [row[:] for row in state]
        new_state[i], new_state[i-1] = list(new_state[i]), list(new_state[i-1])
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        neighbors.append(tuple(map(tuple, new_state)))
    if j < 2:
        new_state = [row[:] for row in state]
        new_state[i], new_state[i-1] = list(new_state[i]), list(new_state[i-1])
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        neighbors.append(tuple(map(tuple, new_state)))
    return neighbors

def a_star(start, goal):
    heap = []
    closed = set()
    g = {tuple(map(tuple, start)): 0}
    f = {tuple(map(tuple, start)): manhattan_distance(get_blank_pos(start), get_blank_pos(goal))}
    heapq.heappush(heap, (f[tuple(map(tuple, start))], tuple(map(tuple, start))))
    came_from = {}
    while heap:
        current = heapq.heappop(heap)[1]
        print("Goal! :", tuple(map(tuple, goal)))
        
        if current == tuple(map(tuple, goal)):
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(tuple(map(tuple, start)))
            path.reverse()
            print("Success! Path found:", path)
            return path
        closed.add(current)
        for neighbor in get_neighbors(current):
            if neighbor in closed:
                continue
            tentative_g = g[current] + 1
            if neighbor not in g or tentative_g < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = tentative_g
                f[neighbor] = tentative_g + manhattan_distance(get_blank_pos(neighbor), get_blank_pos(goal))
                if neighbor not in [i[1] for i in heap]:
                    heapq.heappush(heap, (f[neighbor], neighbor))
        print("current:", current)
        print("heap:", heap)
        print("closed:", closed)
    print("Failed to find a path.")            
    return


a_star([
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]], [
    [1, 2, 3],
    [8, 0 , 4],
    [7, 6, 5]
])
       
       
       
      
