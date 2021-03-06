# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    s = problem.getStartState()    
    if (problem.isGoalState(s)): return []

    
    source = problem.getStartState()
    st = util.Stack()
    st.push(source)

    invalid = tuple((tuple((-1,-1)), "none"))
    trace = {source: invalid,}
    """
    while (target == (-1,-1)):
        u = st.pop()
        successors = problem.getSuccessors(u)

        for sucs in successors:
            if (sucs[0] not in trace): 
                st.push(sucs[0])
                trace[sucs[0]] = (u, sucs[1])
                if (problem.isGoalState(u)): 
                    target = u
                    break
    """
    
    def dfs():
        u = st.pop()
        if problem.isGoalState(u): return u    

        successors = problem.getSuccessors(u)
        for sucs in successors:
            if (sucs[0] not in trace): 
                st.push(sucs[0])
                trace[sucs[0]] = (u, sucs[1])
                find = dfs()
                if find != (-1,-1): return find 

        return (-1,-1)

    target = dfs()
    actions = []
    while (target != source):
        actions.append(trace[target][1])
        target = trace[target][0]

    actions.reverse()
    return actions

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    s = problem.getStartState()    
    if (problem.isGoalState(s)): return []

    
    source = problem.getStartState()
    q = util.Queue()
    q.push(source)

    invalid = tuple((tuple((-1,-1)), "none"))
    trace = {source: invalid,}
    target = tuple()
    
    while (not q.isEmpty()):
        u = q.pop()
        if (problem.isGoalState(u)): 
            target = u
            break
        successors = problem.getSuccessors(u)
        for sucs in successors:
            if (sucs[0] not in trace): 
                q.push(sucs[0])
                trace[sucs[0]] = (u, sucs[1])

    actions = []    
    while (target != source):
        actions.append(trace[target][1])
        target = trace[target][0]

    actions.reverse()
    return actions

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    source = problem.getStartState()
    pq = util.PriorityQueue()
    pq.push(source, 0)
    cost = {source: 0,}
    trace = {}
    target = tuple()

    while not pq.isEmpty():
        u = pq.pop()
        if problem.isGoalState(u): 
            target = u
            break
        successors = problem.getSuccessors(u)
        for sucs in successors:
            v = sucs[0]
            #new_cost_v = cost[u] + problem.getCostOfActions([sucs[1]])
            new_cost_v = cost[u] + sucs[2]
            if v not in cost or cost[v] > new_cost_v: 
                cost[v] = new_cost_v
                pq.push(v, new_cost_v)
                trace[v] = (u, sucs[1])

    actions = []    
    while target != source:
        actions.append(trace[target][1])
        target = trace[target][0]
    
    actions.reverse()

    return actions

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    source = problem.getStartState()
    pq = util.PriorityQueue()
    pq.push(source, 0)
    cost = {source: heuristic(source, problem),}
    trace = {}
    target = tuple()

    while not pq.isEmpty():
        u = pq.pop()
        if problem.isGoalState(u): 
            target = u
            break
        successors = problem.getSuccessors(u)
        for sucs in successors:
            v = sucs[0]
            #new_cost_v = cost[u] + problem.getCostOfActions([sucs[1]])
            new_cost_v = cost[u] + sucs[2] + heuristic(v, problem) - heuristic(u, problem)
            if v not in cost or cost[v] > new_cost_v: 
                cost[v] = new_cost_v
                pq.push(v, new_cost_v)
                trace[v] = (u, sucs[1])

    actions = []    
    while target != source:
        actions.append(trace[target][1])
        target = trace[target][0]
    
    actions.reverse()

    return actions

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
