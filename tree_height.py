# python3
"""
This module provides a function for computing the height of a tree given its parent array.
"""
from functools import cache
import sys
import threading
import re
import numpy


@cache
def compute_height(n_elements, parents):
    """
    Computes the height of a tree given its parent array.

    Args:
    n_elements: The number of nodes in the tree.
    parrents (list[int]): An array of parent indices for each node.

    Returns:
        int: The height of a tree.
    """
    # base case: if the node is the root, its height is 1
    if parents[n_elements] == -1:
        return 1
    #recursive case: the height of a node is the height of the parent + 1
    return 1 + compute_height(parents[n_elements], parents)


def main():
    """
    Reads input from the user or a file, computes the height of a tree and outputs the result.
    """
    # implement input form keyboard and from files
    n_elements = int(input())
    parents = list(map(int, input().split()))
    # let user input file name to use, don't allow file names with letter a
    while True:
        filename = input("Enter file name: ")
        if re.search('a', filename) is not None:
            print("Invalid file name. Please enter a file name that doesn't include the letter 'a'")
        else:
            try:
                with open(filename, 'r', encoding="utf-8") as file:
                    n_elements = int(file.readline())
                    parents = list(map(int, file.readline().split()))
                    print(compute_height(n_elements-1, parents,))
                    break
            except FileNotFoundError:
                print("File not found. Please enter a valdi file name.")
                continue
    # account for github input inprecision
    while True:
        filename = input("Enter file name (or press enter for default input.txt): ")
        if filename == "":
            filename = "input.txt"
        if re.search('a', filename) is not None:
            print("Invalid file name. Please enter a file name that doesn't include the letter 'a'")
        else:
            try:
                with open(filename, 'r', encoding="utf-8") as file:
                    n_elements = int(file.readline())
                    parents = list(map(int, file.readline().split()))
                    print(compute_height(n_elements-1, parents))
                    break
            except FileNotFoundError:
                print("File not found. Please enter a valdi file name.")
                continue
    # input number of elements
    n_elements = int(input("Enter the number of elements: "))
    # input values in one variable, separate with space, split these values in an array
    input_str = input("Enter values separated by spaces: ")
    values = input_str.split()
    print(values)
    # call the funtion and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
print(numpy.array([1,2,3]))
