# Given two arrays A and B of equal length, verify whether A and B can be altered so that
# A[i] + B[i] >= k for some k and all values of i from 0 to n.

# Solution: this is a red herring for a question on mathematical averages.  If the sum
#           of A and the sum of B are both greater than half of k while the averages of
#           A and B add to up to be greater than k, then a permutation that fulfills the
#           problem requirements is feasible.
#           Time complexity: O(1)

def twoArrays(k, A, B):
    if (sum(A) / len(A) + sum(B) / len(B)) >= k and sum(A) > k / 2 and sum(B) > k / 2:
        return 'YES'
    else:
        return 'NO'

