# Given a string, determine whether it is considered valid or not based on the
# following criteria:
#   1) all characters within the string appear an equal amount of times
#   OR
#   2) one character within the string appears at max one time more than
#      any other character within the string

# Solution: we count the number of each character in the string by using a
#           counting hash array, creating a frequency table.  Then, we apply
#           set() to the frequency table.  If there are less than 2 frequen-
#           cies, all characters within the string appeared the same amount.
#           If there are more than 2 frequencies, the string is not valid.
#           If there are exactly 2 frequencies, we check if the 2 frequen-
#           cies are within 1 count of each other; if so, the string is valid,
#           and if not, the string fails.
#           Time complexity: O(N)

def isValid(s):
    n = len(set(s))
    hashtable = [0] * n

    for i in s:
        hashtable[ord(i) % n] += 1

    sethash = list(set(hashtable))
    for k in sethash:
        if k == 0:
            sethash.remove(0)

    if len(sethash) < 2:
        return "YES"
    elif len(sethash) > 2:
        return "NO"
    else:
        if hashtable.count(1) > 1 or abs(sethash[0] - sethash[1]) > 1:
            return "NO"
        else:
            return "YES"

