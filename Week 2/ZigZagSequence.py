# Given the following code, debug it so that it properly creates a "zig-zag sequence," or
# an array in mountain order all values are descending to the left and right of the middle
# term.

# Solution: see the inline comments for details.  Assume we test using the array
#           [1, 2, 3, 4, 5, 6, 7]
#           Time Complexity: O(N^2)

# Original Code (note: this file will not run due to the errors below)
def findZigZagSequence_wrong(a, n):
    a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return


#Debugged Code
def findZigZagSequence(a, n):
    a.sort()
    # Original: mid = int((n + 1)/2)
    mid = int(n/2)  # change middle, the previous middle was one to the right
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    # Original: ed = n - 1
    ed = n - 2  # ed is n - 2, not n - 1, because a[n - 1] is already the smallest value right of the middle
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        # Original: ed = ed + 1
        ed = ed - 1  # we are swapping values down, if it was ed + 1 we will exceed array range

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return

