# python3 -m pip install pandas
# python3 -m pip install numpy
# python3 -m pip install openpyxl
## to run : python3 HW3.py

# git init
# git remote add origin https://github.com/arpettey/CS340---Artificial-Intelligence.git
# git remote -v
# git add filename.py
# git commit -m "Your descriptive commit message"
# git push

### pathname : /Users/avapettey/Downloads/AI

### sources : https://docs.python.org/3/library/heapq.html , https://www.geeksforgeeks.org/python/python-get-a-list-as-input-from-user/ , https://www.w3schools.com/python/python_dsa_bubblesort.asp , https://www.geeksforgeeks.org/python/a-search-algorithm-in-python/ , https://code.visualstudio.com/docs/sourcecontrol/overview, https://www.geeksforgeeks.org/artificial-intelligence/8-puzzle-problem-in-ai/

import heapq

## what functions will I need?
### move_tile, moves a tile & therefore creates a new puzzlestate
### calculate_h_value, calculates the heuristic value
### is_goal_state?, checks whether the puzzlestate is the goal state
### is_solvable?, checks the inversions to see if puzzle is solvable
### print_state, prints the board in a clear way user can read
### search_a_star, searches the board using a star algorithm
### trace_path, traces the path from the goal state -> initial state, displays each move & its resulting puzzlestate

## what classes / objects will I need?
### PuzzleState, the current state of the puzzle (board, what move did I just do?, depth & cost, parent state)

#------------the PuzzleState class stores the board_state, the parent_board_state, move (N, S, W, or E?), g (depth), and f (cost)----------------#
class PuzzleState:
    def __init__(self, board, parent, move, g, f):
        self.board = board
        self.parent = parent
        self.move = move
        self.g = g
        self.f = f

    ## can't use less than on objects, so define it
    def __lt__(self, other):
        return self.f < other.f

#------------------------------------heuristics-----------------------------------#
def calculate_h_value(board, h):
    ## calculates the distance of each tile to its destination
    if h == "distance":
        distance = 0
        for i in range(9):
            if board[i] != 0:
                x1, y1 = divmod(i, 3) ## divide and mod value at position i by 3, store the values
                x2, y2 = divmod(board[i] - 1, 3) ## divide and mod value-1 at position i by 3, store the values
                distance += abs(x1 - x2) + abs(y1 - y2)
        return distance
    ## calculates the number of tiles out of place
    else:
        count = 0
        for i in range(9):
            if board[i] != 0:
                if board[i] != i-1:
                    count += 1
        return count

#-------------------------------------move tile function----------------------------------#
def move_tile(board, move, blank_pos):
    new_board = board[:]
    new_blank_pos = blank_pos + moves[move]
    new_board[blank_pos], new_board[new_blank_pos] = new_board[new_blank_pos], new_board[blank_pos] ## swap the empty tile with the one in desired cardinal direction
    return new_board

#-------------------------function to reconstruct the path------------------------------#
## saves moves from goal -> source then reverses the path
def trace_path(solution):
    path = []
    cur = solution
    while cur:
        path.append(cur)
        cur = cur.parent
    path.reverse()

    for step in path:
        print(f"Move: {step.move}")
        print_state(step.board)
    

#-----------------------------a_star_search function---------------------------------#
def a_star_search(start_state, heuristic):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, PuzzleState(start_state, None, None, 0, calculate_h_value(start_state, heuristic)))

    while open_list:
        cur_state = heapq.heappop(open_list)

        if cur_state.board == goal_state:
            return cur_state

        closed_list.add(tuple(cur_state.board))

        blank_pos = cur_state.board.index(0)

        for move in moves: ## invalid moves are ignored
            if move == 'N' and blank_pos < 3:
                continue
            if move == 'S' and blank_pos > 5:
                continue
            if move == 'W' and blank_pos % 3 == 0:
                continue
            if move == 'E' and blank_pos % 3 == 2:
                continue

            new_board = move_tile(cur_state.board, move, blank_pos)

            if tuple(new_board) in closed_list:
                continue

            new_state = PuzzleState(new_board, cur_state, move, cur_state.g + 1, cur_state.g + 1 + calculate_h_value(new_board, heuristic))
            heapq.heappush(open_list, new_state)

    return None

#-----------------------defining the inversion count function--------------------------#

def sort_count(mylist, count):
    mylist = mylist.copy()
    mylist.remove(0)
    n = len(mylist)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
                count += 1
                swapped = True
        if not swapped:
            break
    if count % 2 == 0:
        return True
    else:
        return False

#---------------------------print board state function--------------------------------#

def print_state(mylist):
    n = len(mylist)
    for i in range(n):
        if i % 3 == 0:
            print("\n", end = "| ")
        print(mylist[i], end= " | ")

#--------------------------------MAIN - validate input---------------------------------------#
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

moves = {
    'N': -3,
    'S': 3,
    'W': -1,
    'E': 1
}

y = True
while y == True:
    heuristic = input("Which heuristic would you like? (distance/number): ").strip().lower()
    if heuristic == "distance" or heuristic == "number":
        y = False
    else:
        print("Wrong input, please try again.")

print(f"You chose {heuristic}!")

li = input("Enter the starting board. Elements should be separated by space. Use 0 for the blank: ").split()
myli = [int(i) for i in li]
print_state(myli)
solvable = sort_count(myli, 0)

if not solvable:
    print("Puzzle not solvable.")
else:
    solution = a_star_search(myli, heuristic)
    if solution:
        print("Solution found:")
        trace_path(solution)
    else:
        print("Error.")