# Given an array of indeterminate length, find the minimum difference between
# the max and min values of a subarray of length k.

# Solution: we sort the given array, then iterate through whilst comparing
#           the differences between terms that are k indices apart (this is
#           equivalent to evaluating the max and min values in a subarray of
#           length k).  We save and return the minimum value.
#           Time complexity: O(N log N) (limited by Python's internal .sort() method)

def maxMin(k, arr):
    # Write your code here
    arr.sort()
    unfairness = int(arr[k - 1] - arr[0])
    for x in range(0, len(arr) - k + 1):
        if (arr[x + k - 1] - arr[x]) < unfairness:
            unfairness = arr[x + k - 1] - arr[x]
    return unfairness



