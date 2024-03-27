#!/usr/bin/env python3

def print_fibonacci(length):
    a, b = 0, 1
    count  = 0
    sol = []

    while count < length:
        sol.append(a)
        c = a + b
        a = b
        b = c
        count += 1
    print(sol)

print_fibonacci(9)