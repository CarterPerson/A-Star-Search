from SearchSolution import SearchSolution
from heapq import heappush, heappop

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        self.state = tuple(state)
        self.heuristic = heuristic
        self.parent = parent
        self.transition_cost = transition_cost


    def priority(self):
        return self.heuristic + self.transition_cost


    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result


def astar_search(search_problem, heuristic_fn):
    # I'll get you started:
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = []
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    visited_cost = {}
    visited_cost[tuple(start_node.state)] = 0

    while len(pqueue) > 0:

        curr = heappop(pqueue)
        solution.nodes_visited += 1

        # if it is complete
        if search_problem.success(curr.state):
            solution.path = backchain(curr)
            solution.cost = curr.transition_cost
            return solution

        # if not complete, adds children
        nextstates = search_problem.get_successors(curr.state)
        for state in nextstates:
            newnode = AstarNode(state[0], heuristic_fn(state[0]), curr, curr.transition_cost + state[1])
            if (newnode.state not in visited_cost) or visited_cost[newnode.state] > newnode.transition_cost:
                visited_cost[newnode.state] = newnode.transition_cost
                heappush(pqueue, newnode)

    return None # no solution found




    # you write the rest:
