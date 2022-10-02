# Given a 2D array that simulates a field, we play the following game with the
# character Bomberman:
#
# 1) Initially, Bomberman arbitrarily plants bombs in some cells, the initial state.
# 2) After one second, Bomberman does nothing.
# 3) After one more second, Bomberman plants bombs in all cells without bombs, thus
#    filling the whole grid with bombs. No bombs detonate at this point.
# 4) After one more second, any bombs planted exactly three seconds ago will detonate.
#    Here, Bomberman stands back and observes.
# 5) Bomberman then repeats steps 3 and 4 indefinitely.
#
# Bombs behave according to the following rules:
# 1) When a bomb at arr[i][j] detonates, it only destroys the cardinal squares around it,
#    i.e. arr[i +/- 1][j +/- 1]
# 2) If a bomb destroys another bomb during detonation, the destroyed bomb does not
#    detonate; chain reactions are not possible
#
# Simulate what the 2D array looks like after any amount of time.  Bombs are "O"s and empty
# squares are filled with "."s.

# Solution: because the problem involves string manipulation and Python strings are
#           immutable, the program is rather tedious to write in Python.  Please see the sol-
#           ution in C++.
#           Note that due to Bomberman placing bombs in all empty spaces, the 2D array
#           essentially inverts its contents with every detonation cycle.  There are 3 phases
#           in a cycle for any given array, these being: 1) the initial state, 2) first deto-
#           nation, and 3) second detonation.  Try it for yourself in the given 6x7 grid ex-
#           ample on Hackerrank!
#           We implement this by using a function that determines which phase the given time
#           correlates to, a function that detonates individual bombs, and a function that
#           keeps track of where to place new bombs after detonating old ones.
#           Time complexity: O(N^2)

