# Given an integer array of length n, print to the 6th decimal place the
# fraction of positive, negative, and zero values in the array.

# Solution: we loop through the array and increment counters for positive and negative numbers, respectively.
#           When printing, we use string literals and the format() method to decapitate the output at 6 digits
#           past the decimal.
#           When printing, we can calculate the number of zeroes by subtracting the amount of positive and neg-
#           ative numbers from the length of the array.
#           Time complexity: O(N)

def plusMinus(arr):
    numPos = 0;
    numNeg = 0;
    for x in arr:
        if x > 0:
            numPos += 1
        elif x < 0:
            numNeg += 1

    print("{0:.6f}".format(numPos / len(arr)))
    print("{0:.6f}".format(numNeg / len(arr)))
    print("{0:.6f}".format((len(arr) - numPos - numNeg) / len(arr)))

