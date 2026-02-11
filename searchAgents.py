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
            if 0 <= nextx < len(self.walls) and 0 <= nexty < len(self.walls[0]):
                if not self.walls[nextx][nexty]: # If not a wall
                    nextState = (nextx, nexty)
                    cost = self.costFn(nextState)
                    successors.append( ( nextState, action, cost) )
        return successors
    
    def getCostOfActions(self, actions):
        """
        Returns the cost of a particular sequence of actions. 
        """
        if actions == None: 
            return 999999
        x,y= self.getStartState()
        cost = 0
        for action in actions:
            # Calc next position
            dx, dy = action
            x, y = int(x + dx), int(y + dy)
            if x < 0 or x >= len(self.walls) or y < 0 or y >= len(self.walls[0]):
                return 999999
            if self.walls[x][y]: 
                return 999999
            cost += self.costFn((x,y))
        return cost

def manhattanHeuristic(position, problem, info={}):
    """
    The Manhattan distance heuristic for a PositionSearchProblem
    """
    "*** YOUR CODE HERE ***"

    xy1 = position
    xy2 = problem.goal
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

   # why are we hard returning 0? Commenting This line out
    # return 0


