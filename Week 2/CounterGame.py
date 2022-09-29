# Given a number, do the following:
#   a) If the number is a power of 2, divide by 2
#   b) If the number is not a power of 2, subtract from it the nearest power of 2
# Players Louise and Richard must follow these rules and Louise always goes first.
# The winner is the first person who reduces the number to 1.  Determine which
# player will win the game.

# Solution: we need an auxiliary function to find the nearest power of 2.  Then,
#           we repeat the steps until we get the total number of turns.  Since
#           Louise goes first, she will win on any game with an odd number of
#           turns; likewise, Richard will win on any game with an even number of
#           turns.
#           Time complexity: O(N^2)


def lp2(n):
    k = 0
    while (2 ** k < n):
        k += 1
    return k - 1


def counterGame(n):
    if n == 1:
        return "Richard"

    turns = 0
    while n != 1:
        if 2 ** lp2(n) == n:
            break
        else:
            turns += 1
            n = n - 2 ** lp2(n)

    if turns % 2 == 1:
        return "Louise"
    else:
        return "Richard"


