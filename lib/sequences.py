#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])  # Empty list for when the length 0
    elif length == 1:
        print([0])  # List with a single element '0' when the length is 1
    else:
        fibonacci_sequence = [0, 1]  # Initializes the sequence with the first two elements
        while len(fibonacci_sequence) < length:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)
        print(fibonacci_sequence)