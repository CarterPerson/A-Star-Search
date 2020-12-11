from Maze import Maze
from time import sleep

class SensorlessProblem:

    def __init__(self, maze, goal_location):
        self.robotloc = []
        for x in range(maze.width):
            for y in range(maze.height):
                if maze.is_floor(x, y):
                    self.robotloc += (x, y)
        self.goal = goal_location
        self.start_state = self.robotloc
        self.width = maze.width
        self.height = maze.height
        self.maze = maze



    def success(self, state):
        x = 0
        while x < len(state):
            if not state[x] == self.goal[divmod(x, 2)[1]]:
                return False
            x += 1
        return True



    def get_successors(self, state):
        returner = []
        pos = 0

        # For eastward movement
        temp = set()
        while pos < len(state):
            if self.maze.is_floor(state[pos] + 1, state[pos + 1]):
                temp.add((state[pos] + 1, state[pos + 1]))
            else:
                temp.add((state[pos], state[pos + 1]))
            pos += 2

        newstate = []
        for x in temp:
            newstate += x
        tempstate = tuple(newstate)
        adder = (tempstate, 1)
        returner.append(adder)


        # For westward movement
        pos = 0
        temp = set()
        while pos < len(state):
            if self.maze.is_floor(state[pos] - 1, state[pos + 1]):
                temp.add((state[pos] - 1, state[pos + 1]))
            else:
                temp.add((state[pos], state[pos + 1]))
            pos += 2

        newstate = []
        for x in temp:
            newstate += x
        tempstate = tuple(newstate)
        adder = (tempstate, 1)
        returner.append(adder)


        # For northward movement
        pos = 1
        temp = set()
        while pos < len(state):
            if self.maze.is_floor(state[pos - 1], state[pos] + 1):
                temp.add((state[pos - 1], state[pos] + 1))
            else:
                temp.add((state[pos - 1], state[pos]))
            pos += 2

        newstate = []
        for x in temp:
            newstate += x
        tempstate = tuple(newstate)
        adder = (tempstate, 1)
        returner.append(adder)


        # For southward movement
        pos = 1
        temp = set()
        while pos < len(state):
            if self.maze.is_floor(state[pos - 1], state[pos] - 1):
                temp.add((state[pos - 1], state[pos] - 1))
            else:
                temp.add((state[pos - 1], state[pos]))
            pos += 2

        newstate = []
        for x in temp:
            newstate += x
        tempstate = tuple(newstate)
        adder = (tempstate, 1)
        returner.append(adder)

        return returner



    def cummulative_heuristic(self, state):
        total = 0
        for x in range(len(state)):
            total += abs(state[x] - state[divmod(x,2)[1]])
        total /= len(state)
        total *= 2
        return total




    def __str__(self):
        string =  "Blind robot problem: "
        return string


        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))


## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
