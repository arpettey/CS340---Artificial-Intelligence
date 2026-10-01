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

### sources : https://docs.python.org/3/library/heapq.html , https://www.geeksforgeeks.org/python/python-get-a-list-as-input-from-user/ , https://www.w3schools.com/python/python_dsa_bubblesort.asp , https://www.geeksforgeeks.org/python/a-search-algorithm-in-python/ , https://code.visualstudio.com/docs/sourcecontrol/overview

import pandas as pd
import numpy as np
import heapq

#------------the cell class stores the f, g, h values and parent position for each grid cell----------------#
class Cell:
    def __init__(self):
        self.parent_i = 0
        self.parent_j = 0
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

#-----------------------defining the inversion count function--------------------------#

def sort_count(mylist, count):
    mylist = mylist.copy()
    mylist.remove('0')
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
    print(" | ", end=None)
    n = len(mylist)
    for i in range(n):
        if i % 3 == 0:
            print("\n" + "")
        print(mylist[i], end= " | ")

#--------------------------------validate input---------------------------------------#

y = True
while y == True:
    heuristic = input("Which heuristic would you like? (distance/number): ").strip().lower()
    if heuristic == "distance" or heuristic == "number":
        y = False
    else:
        print("Wrong input, please try again.")

print(f"You chose {heuristic}!")

#-------------------------------distance heuristic------------------------------------#

if heuristic == "distance":
    li = input("Enter the starting board. Elements should be separated by space. Use 0 for the blank: ").split()
    print(li)
    solvable = sort_count(li, 0)
    if not solvable:
        print("Puzzle not solvable.")
    else:
        heapq.heapify(li)

#-------------------------------number heuristic-------------------------------------#

else:
    li = input("Enter the starting board. Elements should be separated by space. Use 0 for the blank: ").split()
    print(li)
    print_state(li)
    solvable = sort_count(li, 0)
    if not solvable:
        print("Puzzle not solvable.")
    else:
        heapq.heapify(li)

#---------------------------print board start state---------------------------------#

# heap[0] : the smallest item / the root

# heap invariant : min-heaps are binary trees for which every parent node
## has a value less than or equal to any of its children. We refer to this condition
### as the heap invariant.

# heap.sort() : maintains the heap invariant, this implementation uses only the < operator for comparisons

# How A* Search ALgorithm Works
## A* calculates three values for each cell:
### g: Cost of reaching the current cell from the source.
### h: Estimated cost from the current cell to the destination.
### f: Total estimated cost, calculated as f = g + h.
## The algorithm selects the cell with the lowest f value and continues searching until the destination is reached.