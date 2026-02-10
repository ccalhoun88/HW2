# searchAgents.py
# ---------------
# Helper classes for implementing heuristics and map definitions.

from search import SearchProblem

class PositionSearchProblem(SearchProblem):
    """
    A search problem defines the state space, start state, goal test, successor
    function and cost function.  This search problem can be used to find paths
    to a particular point on the pacman board.
    """

    def __init__(self, gameState, costFn = lambda x: 1, goal=(1,1), start=None):
        self.walls = gameState
        self.startState = start
        self.goal = goal
        self.costFn = costFn
        # For display purposes
        self._visited, self._visitedlist, self._expanded = {}, [], 0

    def getStartState(self):
        return self.startState

    def isGoalState(self, state):
        isGoal = state == self.goal
        return isGoal

    def getSuccessors(self, state):
        successors = []
        for action in [(-1, 0), (1, 0), (0, 1), (0, -1)]: # West, East, North, South
            x, y = state
            dx, dy = action
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]: # If not a wall
                nextState = (nextx, nexty)
                cost = self.costFn(nextState)
                successors.append( ( nextState, action, cost) )
        return successors

def manhattanHeuristic(position, problem, info={}):
    """
    The Manhattan distance heuristic for a PositionSearchProblem
    """
    "*** YOUR CODE HERE ***"
    return 0