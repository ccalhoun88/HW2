# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    
    Your algorithm must use a PriorityQueue (found in util.py).
    
    Inputs:
        problem: A SearchProblem instance
        heuristic: A function that takes (state, problem) and returns a number
        
    Returns:
        A list of actions (e.g., ['North', 'South', 'East']) that leads to the goal.
    """
    "*** YOUR CODE HERE ***"

    from util import Queue,PriorityQueue
    stateQueue = PriorityQueue()                    # stateQueue to manage which states to expand
    stateQueue.push(problem.getStartState(),0)
    currState = stateQueue.pop()
    visited = []                                # Store paths that have been explored
    tempPath=[]                                 # Store the temporary paths
    path=[]                                     # Store our final sequence of directions 
    pathToCurrent=PriorityQueue()               # Queue to store direction to children (currState and pathToCurrent go hand in hand)
    while not problem.isGoalState(currState):
        if currState not in visited:
            visited.append(currState)
            successors = problem.getSuccessors(currState)
            for child,direction,cost in successors:
                tempPath = path + [direction]
                costToGo = problem.getCostOfActions(tempPath) + heuristic(child,problem)
                if child not in visited:
                    stateQueue.push(child,costToGo)
                    pathToCurrent.push(tempPath,costToGo)
        currState = stateQueue.pop()
        path = pathToCurrent.pop()    
    return path
    
    # util.raiseNotDefined()  - Commented out, because we're using this method

# Testing the aStarSearch logic
if __name__ == '__main__':
    # Quick test of A* with a simple grid
    from search import aStarSearch
    
    # Create a simple 3x3 grid (False = open, True = wall)
    simple_grid = [
        [False, False, False],
        [False, True, False],
        [False, False, False]
    ]
    
    problem = PositionSearchProblem(
        gameState=simple_grid,
        start=(0, 0),
        goal=(2, 2)
    )
    
    print("Start:", problem.getStartState())
    print("Goal:", problem.goal)
    print("Running A*...")
    
    path = aStarSearch(problem, manhattanHeuristic)
    print("Path found:", path)
    print("Path length:", len(path))