# Pacman Project 1: Search

Source project link: http://ai.berkeley.edu/search.html  <br />
Name: Bui Quang Long <br />
MSSV: 18020029

### Overall results: 22/25

### Question 1 (3/3): DFS
I implemented the basic depth first search algorithm through a dfs() function which returns the goal state if found otherwise returns (-1,-1). This helps prevent visiting redundant state when goal state has already been found.
Also, I stored the previous state of each state in a dictionary in order to trace back the path from start state to goal state. This techique 

### Question 2 (3/3): DFS
Similar to DFS, this time I use a queue instead of a stack. My implementation is generical enough to run on eightpuzzel.py without any changes.

### Question 3 (3/3): UCS
This time I use a priority queue, searching from the lowest-cost state.

### Question 4 (3/3): A star search
Similar to UCS, but this time the estimated cost from the current state to the goal state is added to the cost function.

### Question 5 (3/3): Finding all corners problem
The game state has changed in this problem. Apart from maintaining current manhattan position, I also maintain visited information of each corner in a 4-element tuple, which indicates if the corresponding corner is visisted or not. <br />
For example, a game state looks like this: some_state = ( (x,y), (0,1,0,0) ), where (x,y) is the manhattan position and tuple's element i = 0/1 means corner[i] is unvisited/visisted.

### Question 6 (2/3): Corners Problem: Heuristic
We need to find a heuristic cost function to speed up the question 5. Here I define the heuristic cost equal to the manhattan distance between the current state and the closest unvisited corners.

### Question 7 (2/4): Eating All The Dots
e need to find a heuristic function to speed up the eating process. Here I define the heuristic cost equal to the manhattan distance between the current state and the closest available food.

### Question 8 (3/3): Suboptimal Search
In this problem, we need to find the closest food. I just simply modified the GoalState of AnyFoodSearchProblem function to a available food and use BFS to find the closest one.

#### Future work: Find a better heuristic function for question 6 and 7.
