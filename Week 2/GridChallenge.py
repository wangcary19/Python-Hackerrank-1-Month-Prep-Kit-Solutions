# Given an array of strings with equal length n, determine whether the n by n
# grid formed by the strings is in ascending alphabetical order down columns
# after sorting and ensuring that the strings are in ascending alphabetical order
# across rows.

# Solution: we first sort the strings in the array such that they are in alpha-
#           betical order (i.e. ensure the rows are in ascending order), then
#           iterate down the columns and check if there are any exceptions to
#           the ascending order.
#           Time complexity: O(N^2 log N)

def gridChallenge(grid):
    for i in range(0, len(grid)):
        grid[i] = sorted(grid[i])

    for row in range(0, len(grid) - 1):
        for col in range(0, len(grid[0])):
            if grid[row][col] > grid[row + 1][col]:
                return "NO"
            else:
                continue
    return "YES"






