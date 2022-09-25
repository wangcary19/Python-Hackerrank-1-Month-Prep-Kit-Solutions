# Given a 12-hour time in a string, return the string in military time.

# Solution: we use string comprehension to detect AM or PM and parse out
#           the individual cases.
#           If the time is in the AM, we only need to change instances of
#           "12:xx:xxAM" to "'00:xx:xx'."
#           If the time is in the PM, we need to let instances of "12:xx:xxPM"
#           remain as "'12:xx:xx'."  For all other PM cases, we need to add 12
#           to the hour.
#           Time complexity: O(1), since the strings are of set length

def timeConversion(s):
    if s[-2:] == "AM":
        if s[0:2] == "12":
            return "00" + s[2:-2]
        else:
            return s[0:-2]
    else:
        if s[0:2] == "12":
            return s[0:-2]
        else:
            return str(int(s[0:2]) + 12) + s[2:-2]


