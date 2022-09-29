# Given an array, determine if there is a point in the array where the sum of all values left of
# and not including said index equals the sum of all values right of and not including said index.

# Solution: we sum the array, then iterate through the array while subtracting each element
#           from the sum and adding it to a new sum.  If at any point the sum and the new sum
#           equate each other, then we have found the middle point and return "YES."
#           Time complexity: O(N)


def balancedSums(arr):
    right = sum(arr)
    left = 0

    if len(arr) == 0:
        return "NO"
    elif len(arr) == 1:
        return "YES"

    for i in range(0, len(arr)):
        right -= arr[i]
        if right == left:
            return "YES"
        else:
            left += arr[i]
            continue

    return "NO"

