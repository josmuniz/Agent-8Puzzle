# Agent-8Puzzle

Given an initial state of an 8-puzzle problem and final state to be reached as follows:
Initial state   Final state
2 8 3            1 2 3
1 6 4              8 4 
7   5            7 6 5

Assuming our agent needs to figure out the shortest path from the initial state to the final state using the A* algorithm and the heuristic function h(n) used is: “The number of misplaced tiles”. The cost function g(n) is: “the depth” as we expand the tree towards a solution. Also the agent can move one step at a time and either horizontally or vertically i.e. no diagonal movements.
