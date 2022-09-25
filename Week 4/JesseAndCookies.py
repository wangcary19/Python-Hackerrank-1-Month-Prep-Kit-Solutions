# Given an array of integers, return the minimum amount of operations
# needed such that all values within the array are larger than a given k.
# The minimum and second minimum are continuously popped out, sum-
# med in the manner of (minimum + 2 * second minimum) and pushed back in.

# Solution: we use a pre-built min-heap structure in Python so that the
#           two smallest values in the array are always readily avail-
#           able to access.  The "heapq" library converts any list object
#           into a min-heap equivalent array.
#
#           Time complexity: O(log N), since popping is always constant time
#                            but pushing to a min-heap is of big O(log N)

import heapq


def cookies(k, A):
    heapq.heapify(A)
    iters = 0
    while A[0] < k and len(A) > 1:
        a = heapq.heappop(A)
        b = heapq.heappop(A)
        c = a + 2 * b
        heapq.heappush(A, c)
        iters += 1

    if A[0] >= k:
        return iters
    else:
        return -1
