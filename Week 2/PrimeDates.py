# Given the following function findPrimeDates(), debug it so that it correctly
# determines the number of dates divisible by 4 and 7 between its two input
# dates.  The inputs will be concatenated into agglomerate integers with leading
# zeroes removed (i.e. "09-16-1978" = "9161978").

# NOTE: the problem handler for this question on Hackerrank is known to be incorrect.

# The following is the incorrect code:

def findPrimeDates_incorrect(d1, m1, y1, d2, m2, y2):
    storeMonth()
    result = 0

    while(True):
        x = d1
        x = x * 100 + m1
        x = x * 1000 + y1
        if x % 4 == 0 and x % 7 == 0:
            result = result + 1
        if d1 == d2 and m1 == m2 and y1 == y2:
            break
        updateLeapYear(y1)
        d1 = d1 + 1
        if d1 > month[m1]:
            m1 = m1 + 1
            d1 = 1
            if m1 > 12:
                y1 = y1 + 1
                m1 = m1 + 1
    return result

# The following is the correct code, with debug points marked:

def findPrimeDates(d1, m1, y1, d2, m2, y2):
    storeMonth()
    result = 0

    while(True):
        x = d1
        x = x * 100 + m1
        x = x * 10000 + y1  # Change 3: "x * 1000" to "x * 10000", since we need to shift by 4 digits for a year
        if x % 4 == 0 or x % 7 == 0:  # Change 2: "and" to "or", since dates divisible by either 4 or 7 are valid
            result = result + 1
        if d1 == d2 and m1 == m2 and y1 == y2:
            break
        updateLeapYear(y1)
        d1 = d1 + 1
        if d1 > month[m1]:
            m1 = m1 + 1
            d1 = 1
            if m1 > 12:
                y1 = y1 + 1
                m1 = 1  # Change 3: "m1 + 1" to "1" if the month exceeds 12, we reset it to January
    return result

# Below are the referenced functions and variables:

month = []

def updateLeapYear(year):
    if year % 400 == 0:
        month[2] = 28
    elif year % 100 == 0:
        month[2] = 29
    elif year % 4 == 0:
        month[2] = 29
    else:
        month[2] = 28


def storeMonth():
    month[1] = 31
    month[2] = 28
    month[3] = 31
    month[4] = 30
    month[5] = 31
    month[6] = 30
    month[7] = 31
    month[8] = 31
    month[9] = 30
    month[10] = 31
    month[11] = 30
    month[12] = 31




