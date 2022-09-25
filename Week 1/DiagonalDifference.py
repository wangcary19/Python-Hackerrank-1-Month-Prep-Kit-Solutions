# Given an n x n integer array, find the difference between the sums of its diagonals.

# Solution: we iterate through the array and continuously sum the difference between the
#           diagonals (top left - bottom left, next top left - next bottom left, etc.).
#           Then, we return the absolute value of this sum.
#           Time complexity: O(N)

def DiagonalDifference(arr):
    s = 0
    for i in range(0, len(arr)):
        s += arr[i][i] - arr[len(arr) - 1 - i][i]
    return abs(s)

