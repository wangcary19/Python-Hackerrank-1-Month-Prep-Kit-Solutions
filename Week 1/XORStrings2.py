# Given an erroneous strings XOR function, debug at max 3 lines to allow the
# function to work as intended

# Solution: the XOR returns true when two values are different and false when
#           they are the same.  In the faulty function below (the first one),
#           the conditional comparing elements of the strings uses a single
#           equal (assignment) instead of a double equal (comparator).  Then,
#           under both the if and the else, res is set to either 0 or 1,
#           whereas insteaad 0 or 1 should be appended (in this case, because
#           res is a string, concatenated) to res.  The corrected function is
#           on line 24.
#           Note that this .py will not compile, it is only for demonstration.

def strings_xor_wrong(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] = t[i]:
            res = '0';
        else:
            res = '1';

    return res


def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

