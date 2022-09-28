# Given a user string and a user offset input, encrypt the string using a Caeser cipher by
# the offset amount.

# Solution: we use Python's ord() function to convert from string to ASCII integer, apply the
#           shift with overflow logic, and convert back from ASCII value to string using
#           chr().  Read more about ASCII values here (https://en.wikipedia.org/wiki/ASCII)
#           Time complexity: O(N)

def caesarCipher(s, k):
    out = ""
    shift = k % 26
    # Write your code here
    for i in range(0, len(s)):
        if 65 <= ord(s[i]) <= 90:  # capital letters
            if ord(s[i]) + shift > 90:
                out += str(chr(65 + ord(s[i]) + shift - 91))
            else:
                out += str(chr(ord(s[i]) + shift))
        elif 97 <= ord(s[i]) <= 122:  # lowercase letters
            if ord(s[i]) + shift > 122:
                out += str(chr(97 + ord(s[i]) + shift - 123))
            else:
                out += str(chr(ord(s[i]) + shift))
        else:
            out += s[i]

    return out


