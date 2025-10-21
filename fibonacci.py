#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def fibonacci(depth):
    if depth == 0:
        return 0
    if depth == 1:
        return 1
    else:
        return fibonacci(depth - 1) + fibonacci(depth - 2)
        
# Loop until the user inputs a valid, positive integer
def get_input():
    while(True):
        depth = input("Enter your desired depth: ")
        if depth.lstrip('-').isdigit() and int(depth) >= 0:
            depth = int(depth)
            break
        else:
            print("Invalid Input")
    print_out(depth)

# Actually print everything out
def print_out(depth):
    counter = 0
    while(counter<=depth):
        print(fibonacci(counter), end = " ")
        counter = counter + 1
        
get_input()
