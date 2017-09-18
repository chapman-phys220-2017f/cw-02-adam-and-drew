#!/usr/bin/env python
                                                         ### Remember to specify python3
import math

def compute_sum(tol = 1e-2):
    k = float(1.0)
    total = 1
    while(1/math.pow(k,2) > tol):                        ### k**2 is the same as math.pow(k,2)
        k += 1
        total += (1/math.pow(k,2))                       ### Note this calculates k**2 a second time on each iteration
    return total


if __name__ == "__main__":
    print("Currently computing sum with tolerance 1e-2")   ### copy-pasting code is bad. Write a function and call it with different arguments.
    print(compute_sum(1e-2))
    print("Currently computing sum with tolerance 1e-2")
    print(compute_sum(1e-2))
    print("Currently computing sum with tolerance 1e-3:")
    print(compute_sum(1e-3))
    print("Currently computing sum with tolerance 1e-5:")
    print(compute_sum(1e-5))
    print("Currently computing sum with tolerance 1e-10:")
    print(compute_sum(1e-10))
    print("Currently computing sum with tolerance 1e-12:")
    print(compute_sum(1e-12))
