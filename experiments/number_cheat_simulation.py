#!/usr/bin/env python3
"""Monte Carlo simulation of two 'cheating' strategies when picking
the higher number from two secret random values (1..n).

This is an old curiosity experiment. The second strategy's logic is
a bit convoluted and may not demonstrate what the original author intended.

Run: python number_cheat_simulation.py
"""

import random

n = 10

print("strategy 1")
s1_points = 0
for i in range(100000):
    num1 = random.randint(1,n)
    num2 = num1
    while num2==num1:
        num2 = random.randint(1,n)
    choice = random.randint(1,2)
    if choice == 1:
            if num1 > num2:
                s1_points = s1_points +1
    if choice == 2:
            if num2 > num1:
                s1_points = s1_points +1
print("points",s1_points)

print("strategy 2")
s2_points = 0
for i in range(100000):
    num1 = random.randint(1,n)
    num2 = num1
    while num2==num1:
        num2 = random.randint(1,n)
    num3 = random.randint(1,n)
    choice = random.randint(1,2)
    if choice == 1:
        if num3 > num1:
            if num2 > num1:
                s2_points = s2_points + 1
        elif num1 > num2:
            s2_points = s2_points +1
    if choice == 2:
        if num3 > num2:
            if num1 > num2:
                s2_points = s2_points + 1
                
        elif num2 > num1:
            s2_points = s2_points + 1
        
        
print("points",s2_points)
