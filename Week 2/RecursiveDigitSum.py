# Define the super digit of a number x as follows:
#   a) If x is a single-digit number, it is its own super digit
#   b) Otherwise, let x = the sum of its digits
# Write a function that returns the super digit of any input number
# repeated a given k amount of times.

# Solution: Note that the super digit is always equal to the original
#           number % 9, and when the number is divisible by 9, its
#           super digit is 9.
#           Time complexity: O(N)

def superDigit(n, k):
    # Write your code here
    sum = 0
    for i in range(0, len(n)):
        sum += int(n[i])
    if (k * sum) % 9 == 0:
        return 9
    else:
        return (k * sum) % 9


