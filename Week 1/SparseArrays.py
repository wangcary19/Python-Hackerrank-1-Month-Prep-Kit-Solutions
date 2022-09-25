# Given an array of text and an array of queries, find how many times each query occurs
# in the text array.  Return answers as an integer array of occurrences for each query.

# Solution: we use the Python count() function to loop through the text array for us.  We
#           do this for every query.
#           Time complexity: O(N^2), because we are looping through a list for every element
#                                    of another list.

def matchingStrings(strings, queries):
    freq = []
    for x in queries:
        freq.append(strings.count(x))

    return freq

