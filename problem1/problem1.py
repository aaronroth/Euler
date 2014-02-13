#!/usr/bin/env python

# Answer to problem 1 in the Euler Project problems.
# Written by Aaron Roth on 2/12/14.

sum = 0

for i in range(1, 1000):
    if i % 3 == 0:
        sum = sum + i
    elif i % 5 ==  0:
        sum = sum + i

print sum