# Given an array of n integers, return the frequency array (in increasing order).
# All numbers within the array will be positive and less than 100.

# Solution: we use the special "counting sort" method, wherein we set up an array
#           of 100 zeroes, then increment at the index that equals the number in
#           the given array.  For instance, if 56 occurs, we increment counting
#           array at index 56.
#           Time complexity: O(N)

def countingSort(arr):
    freq = [0] * 100
    for x in arr:
        freq[x] += 1
    return freq


