<<<<<<< Updated upstream
import numpy as pd
import pandas as np
=======
test_ranked = [100, 100, 50, 40, 40, 20, 10]
test_player = [5, 25, 50, 120]
def climb(ranked, player):
    d = {}
    ranks = [0] * len(player)

    for idx, x in enumerate(sorted(set(ranked), reverse=True), 1):
        d[idx] = x

    for i in range(0, len(player) - 1):  # iterate backwards in player
        for j in range(1, len(d) + 1, 1):  # iterate through d
            if player[i] == d.get(j):
                ranks[i] = j
                break
            elif player[i] > d.get(j):
                if j == 1:
                    print("I'm here")  # debug
                    ranks[i] = 1
                    break
                else:
                    ranks[i] = j - 1
                    continue
            elif player[i] < d.get(j):
                ranks[i] = j + 1
                continue
            else:
                continue

    print(d)
    print(ranks)

    return ranks


climb(test_ranked, test_player)
>>>>>>> Stashed changes

