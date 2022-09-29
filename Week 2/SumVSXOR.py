# Given a number n, return the amount of values less than n but greater than or
# equal to 0 that fulfill n + x = n XOR x, where XOR is the bitwise XOR operator.

# Solution: n + x = n XOR x is true only when the bitstring of x is exactly the
#           opposite of the bitstring of n.  For instance, when n = 4 = 100, x
#           can equal 0, 1, 2, or 3 - 000, 001, 010, 011.  Closer inspection
#           reveals that the number of viable values for x depends on the
#           number of zeroes in n - for every 0 in the bitstring of n, x can
#           have either a 0 or a 1 and meet the condition, whereas for every
#           1 in the bitstring of n, x must be 0 in order to meet the condition.
#           We can count the amount of zeroes in the bitstring of n by
#           dividing by 2 and checking if the quotient is divisible by 2.  This
#           is possible because dividing by 2 is equal to shifting the bitstring
#           one digit to the right.  If the remaining bitstring has a "1" at the
#           rightmost position, then the number will be odd, hence the modulo
#           test.  After we get the number of zeroes, we raise 2 to the power of
#           that number to count the amount of acceptable values for x.
#           Time complexity: O(log N)


def sumXor(n):
    # Write your code here
    num_zeroes = 0
    while n > 0:
        if n % 2 == 0:
            num_zeroes += 1
        n = int(n/2)

    return 2 ** num_zeroes

