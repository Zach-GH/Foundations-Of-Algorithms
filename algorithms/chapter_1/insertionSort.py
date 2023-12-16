#!/usr/bin/env python3
import array as array
"""
Insertion Sort algorithm
Page 17 section 2.1
Used for sorting a small amount of elements
Solves the sorting problem introduced in Chapter 1

Input: A sequence of n numbers <a1,a2,....,a(n)>
Output: A permutation (reordering) <a'1,a'2,....,a'(n)>
of the input sequence such that a'1 <= a'2 <= ... <= a'(n)
"""
# define the insertSort function
def insertSort(A: array.array, n: int) -> int:
    for i in range (1, n):
        key = A[i]
        print('array A step: ' + str(i), ' ' + str(A), '\n')
        j = i - 1
        while (j >= 0 and A[j] > key):
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    return 0

# Create two arrays
a = array.array('i', [5, 2, 4, 6, 1, 3]) # i here stands for integer type
print('Current cards held in your right hand: ' + str(a), '\n')

insertSort(a, len(a))

print('You are now holding the following cards in your left hand: ' + str(a), '\n')
