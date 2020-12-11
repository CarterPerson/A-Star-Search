from Maze import Maze
from time import sleep

class MazeworldProblemWithTimeFactor:

    ## you write the constructor, and whatever methods your astar function needs

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goals = goal_locations
        self.start_state = []
        self.start_state.append(1)
        self.start_state += maze.robotloc
        self.numrobots = int(len(maze.robotloc)/2)
        self.robotloc = maze.robotloc



    # based on what robot's turn it is

    def get_successors(self, state):
        robotnum = state[0] # Current robot that is moving
        nextrobot = robotnum + 1 # next robot to move
        if nextrobot > self.numrobots:
            nextrobot = 1

        returner = []
        baseadder = list(state)
        baseadder[0] = nextrobot

        for change in [-1, 1]: # adds movement options

            adder = baseadder.copy()
            adder[2*robotnum - 1] = adder[2*robotnum - 1] + change
            if self.maze.is_floor(adder[2*robotnum - 1], adder[2*robotnum]) and not self.is_robot(adder[2*robotnum - 1], adder[2*robotnum], state):
                returner.append((tuple(adder), 10))

            adder = baseadder.copy()
            adder[2*robotnum] = adder[2*robotnum] + change
            if self.maze.is_floor(adder[2*robotnum - 1], adder[2*robotnum]) and not self.is_robot(adder[2*robotnum - 1], adder[2*robotnum], state):
                returner.append((tuple(adder), 10))

        returner.append((tuple(baseadder), 1)) # adds the wait option

        return returner



    def success(self, state):
        for x in range(len(self.goals)):
            if not self.goals[x] == state[x+1]:
                return False
        return True



    def is_robot(self, x, y, state):
        for loc in range(self.numrobots):
            if x == state[2*loc + 1] and y == state[2*loc + 2]:
                return True
        return False



    # gives the cumulative heuristic distance of all of the robots

    def manhattan_heuristic(self, state):
        h = 0
        for x in range(len(self.goals)):
            h += abs(state[x+1] - self.goals[x])
        return h



    def __str__(self):
        string =  "Mazeworld problem: "
        return string



        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))


## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))
