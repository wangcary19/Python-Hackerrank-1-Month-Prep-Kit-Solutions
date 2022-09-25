# Given an array of positive integers with less than 100 members, find the integer that occurs only once.

# Solution: we use a counting array and increment the index equivalent to
#           the value of the integer, then return the index of the counting
#           array that only has a value of n.
#           Time commplexity: O(N)

def lonelyinteger(a):
    count_arr = [0] * 100
    for x in a:
        count_arr[x] += 1
    for y in range(0, len(count_arr)):
        if count_arr[y] == 1:
            return y


