#!/usr/bin/env python
import math

def compute_sum(tol = 1e-2):
    k = float(1.0)
    total = 1
    while(1/math.pow(k,2) > tol):
        k += 1
        total += (1/math.pow(k,2))
    return total


if __name__ == "__main__":
    print("Currently computing sum with tolerance 1e-2")
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