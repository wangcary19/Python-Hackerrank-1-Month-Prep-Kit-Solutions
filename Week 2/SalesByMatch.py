# Given an array of n integers, return the number of matching integer pairs.

# Solution: we use the special "counting sort" method, wherein we set up an array
#           of 100 zeroes, then increment at the index that equals the number in
#           the given array.  For instance, if 56 occurs, we increment counting
#           array at index 56.  Then, we iterate through our counting array and
#           return the total number of even elements.
#           Time complexity: O(N)

def sockMerchant(n, ar):
    counting = [0] * 101
    for i in ar:
        counting[i] += 1

    pairs = 0
    for x in counting:
        pairs += int(x/2)

    return pairs

