# Given an array of 5 elements, print the minimum possible sum
# and the maximum possible sum, separated by a space.

# Solution: we sort the array and print its sum without its last member (i.e. highest value)
#           - which produces the minimum sum - and then the sum without its first member
#           (i.e. lowest value) - which produces the maximum sum.
#           We can use sorted() and sum() since the array is of set size 5.
#           Time complexity: O(1)

def miniMaxSum(arr):
    a = sorted(arr)
    s = sum(arr)
    print(s - a[-1], s - a[0], sep=" ")



