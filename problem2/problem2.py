#!/usr/bin/env python

# Answer to problem 2 in the Euler Project problems.
# Created by Aaron Roth on 2/13/14.

currentSum = 2
currentTerm = 3
priorTerm = 2

while currentTerm <= 4000000:
    if currentTerm % 2 == 0:
        currentSum = currentSum + currentTerm
    
    tempCurrentTerm = currentTerm
    currentTerm = currentTerm + priorTerm
    priorTerm = tempCurrentTerm

print currentSum
    