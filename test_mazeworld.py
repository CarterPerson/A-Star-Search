from MazeworldProblem import MazeworldProblem
from MazeworldWithTimeFactorProblem import MazeworldProblemWithTimeFactor
from Maze import Maze

from astar_search import astar_search



# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

test_maze3 = Maze("maze3.maz")
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

# print(test_mp.get_successors(test_mp.start_state))

# this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_mp, null_heuristic)
print(result)

# this should do a bit better:
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
# test_mp.animate_path(result.path)

# Your additional tests here:
maze_four = Maze("maze4corridor.maz")
test_corridor = MazeworldProblem(maze_four, (2, 4, 2, 5, 2, 6))
result = astar_search(test_corridor, test_corridor.manhattan_heuristic)
print("\n maze 4 \n")
print(result)
# test_corridor.animate_path(result.path)

maze_five = Maze("maze5.maz")
test_corridor = MazeworldProblem(maze_five, (39, 17))
result = astar_search(test_corridor, test_corridor.manhattan_heuristic)
print("\n maze 5 \n")
print(result)
#test_corridor.animate_path(result.path)

maze_six = Maze("maze6.maz")
test_corridor = MazeworldProblem(maze_six, (1, 24))
result = astar_search(test_corridor, test_corridor.manhattan_heuristic)
print("\n maze 6 \n")
print(result)
# test_corridor.animate_path(result.path)

maze_seven = Maze("maze7.maz")
test_corridor = MazeworldProblem(maze_seven, (3, 2, 1, 2))
result = astar_search(test_corridor, test_corridor.manhattan_heuristic)
print("\n maze 7 \n")
print(result)
# test_corridor.animate_path(result.path)

maze_eight = Maze("maze8.maz")
test_corridor = MazeworldProblem(maze_eight, (5, 3, 1, 1))
result = astar_search(test_corridor, test_corridor.manhattan_heuristic)
print("\n maze 8 \n")
print(result)
# test_corridor.animate_path(result.path)



