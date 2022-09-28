# Given a game where there are n towers each of size m, determine whether Player 1 or Player 2
# will win when the rules are as follows: 1) Player 1 always moves first; 2) each player can
# reduce the size of a tower to some y where x % y == 0 (i.e. 1 <= y < 0); and 3) each player
# always plays the best decision possible.  A player loses when no towers can be reduced further
# on their turn.

# Solution: the key here is rule #3, where each player is forced to play the best decision
#           possible.  This means that aside from 2 special cases (where n = 1 and when m = 1),
#           Player 1 always wins when there are an odd amount of towers , likewise for Player 2
#           when there are an even amount of towers.  Player 1 starts first and goes on the
#           odd-numbered turns; an odd-numbered amount of towers implies Player 1 has an extra
#           "last tower" to break before handing the turn over to Player 2.  The same goes for
#           Player 2 with an even-numbered amount of towers.
#           Time complexity: O(1)

def towerBreakers(n, m):
    if n == 1:  # Special Case 1: Player 1 instantly reduces the single tower to 1 and wins
        return 1
    elif m == 1:  # Special Case 2: Player 1 cannot do anything, so Player 2 wins by default
        return 2
    elif n % 2 == 1:
        return 1
    else:
        return 2

