# Given an integer n, invert its binary string and return the resultant integer.

# Solution: we use bitwise not (the "~" operator) to flip all 1s to 0s and vice versa
#           in the binary representation of n, then bitwise shift by 32 to obtain the
#           unsigned equivalent (since Python automatically merges all int types into
#           one).  Read more about how computers implement integers here at
#           https://cs.indstate.edu/sternfl/pu2/2W/compInt.html
#           Time complexity: O(N)

def flippingBits(n):
    return ~n + (1 << 32)

