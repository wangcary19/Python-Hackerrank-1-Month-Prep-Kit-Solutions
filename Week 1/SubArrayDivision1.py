# Given an array s of length n, determine how many continuous subarrays exist within
# that have a length of m and a sum of d.

# Solution: we use Python list splicing to check the sums of all possible subarrays
#           of a given length and increment a counter each time the condition is
#           fulfilled.
#           Time complexity: O(n)

def birthday(s, d, m):
    count = 0
    for i in range(0, len(s) - m + 1):
        if sum(s[i:i + m]) == d:
            count += 1
        else:
            continue
    return count



