#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:22:48 2023

@author: josemuniz
"""

import math

def ida_star(initial_state, goal_state, heuristic):

    # Define the initial f-value as the heuristic cost of the initial state
    f_limit = heuristic(initial_state)
    while f_limit <= 100:
        # Perform a depth-first search with a limit of the current f-value limit
        result, f_limit = dfs(initial_state, goal_state, 0, f_limit, heuristic)
        if result is not None:
            # Solution found
            cost = len(result) - 1
            print(f"Solution found with cost {cost}:")
            for state in result:
                print(state)
            return result, cost
    print("No solution found.")
    return None, math.inf

def dfs(state, goal_state, g, f_limit, heuristic):
    
    # Calculate the f-value of the current state
    f = g + heuristic(state)
    if f > f_limit:
        # Exceeded the f-limit, return None to signal that a better solution may exist
        return None, f
    if state == goal_state:
        # Reached the goal state, return the solution path and cost
        return [state], g
    # Generate the successors of the current state
    successors = get_successors(state)
    for successor in successors:
        # Recursively search the successors
        result, new_f_limit = dfs(successor, goal_state, g + 1, f_limit, heuristic)
        if result is not None:
            # Solution found, add the current state to the path and return the solution path and cost
            result.insert(0, state)
            return result, new_f_limit
        # Check if all possible states have been explored
        if new_f_limit == math.inf:
            return None, math.inf
    # No solution found from this state
    return None, math.inf

def get_successors(state):
    """
    Returns a list of the valid successor states for the given state.
    Args:
        state (tuple): The current state of the problem.
    Returns:
        A list of the valid successor states for the given state.
    """
    # Find the location of the blank tile (0)
    blank_index = state.index(0)
    # Define the possible moves
    moves = {
        'up': -3,
        'down': 3,
        'left': -1,
        'right': 1
    }
    successors = []
    # Try each move and generate a new state if it is valid
    for move, delta in moves.items():
        new_index = blank_index + delta
        # Check if the move is within the bounds of the board
        if 0 <= new_index < len(state):
            # Check if the move is valid (i.e., the blank tile is moving into a non-blank tile)
            if (move == 'up' and blank_index not in [0, 1, 2]) \
                or (move == 'down' and blank_index not in [6, 7, 8]) \
                or (move == 'left' and blank_index not in [0, 3, 6]) \
                or (move == 'right' and blank_index not in [2, 5, 8]):
                # Create a new state by swapping the blank tile with the tile being moved into
                new_state = list(state)
                new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
                successors.append(tuple(new_state))
    return successors

def heuristic(state, goal_state):
    """
    Computes the Manhattan distance heuristic for the 8-puzzle problem.
    Args:
        state (tuple): The current state of the problem.
        goal_state (tuple): The goal state of the problem.
    Returns:
        The Manhattan distance heuristic for the given state and goal state.
    """
    # Create a dictionary to map tile values to their indices
    indices = {state[i]: (i // 3, i % 3) for i in range(len(state))}
    
    # Compute the Manhattan distance by summing the distances between the tiles and their goal positions
    distance = 0
    for i in range(len(state)):
        if state[i] != 0:
            goal_row, goal_col = divmod(goal_state.index(state[i]), 3)
            curr_row, curr_col = indices[state[i]]
            distance += abs(goal_row - curr_row) + abs(goal_col - curr_col)
            
    return distance

ida_star((2, 8, 3, 1, 6, 4, 7, 0, 5), (1, 2, 3, 8, 0, 4, 7, 6, 5), heuristic) 
