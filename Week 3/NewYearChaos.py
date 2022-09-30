# Given an array, determine the minimum amount of shifts made from a sorted
# start state if each element can be moved at max 2 indices away from its
# sorted position.  The array always contains values from 1 to some n.

# Solution: in a sorted array, the index is always equal to the value at that
#           index minus 1.  Thus, we first implement our catch condition: if a
#           value minus its current index is greater than 2, then the given
#           array is not a possible outcome of the above conditions.
#           To count the minimum amount of shifts made, we subject the array to
#           bubble sort and place each term back to its proper position, incre-
#           menting a counter each time we swap a term's position.
#           Time complexity: O(N^2)


def minimumBribes(q):
    result = 0
    for x in range(len(q)):
        if q[x] - x - 1 > 2:
            print("Too chaotic")
            return
        else:
            ck = x
            while (ck != 0 and q[ck] < q[ck - 1]) or (ck > 1 and q[ck] < q[ck - 2]):
                temp = q[ck]
                q[ck] = q[ck - 1]
                q[ck - 1] = temp
                ck -= 1
                result += 1
    print(result)

