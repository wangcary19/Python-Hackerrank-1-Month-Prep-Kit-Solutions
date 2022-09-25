# Given a string, determine if it contains all the letters of the English
# alphabet regardless of case and one or more spaces (i.e. a pangram).

# Solution: we use Python to remove all spaces within the string.  Then,
#           we turn the entire string to lowercase and use the set oper-
#           ation, which removes duplicates.  In effect, we filter the
#           string down to its alphabetic components.  Now, all we do is
#           count if there are 26 elements (i.e. the alphabet) within the
#           set.
#           Time complexity: O(N^2)

def pangrams(s):
    if len(set(s.replace(" ","").lower())) == 26:
        return "pangram"
    else:
        return "not pangram"
