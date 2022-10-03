# Given an array of past arcade game scores and a sorted array of
# current player scores, return an array of the ranks of each of the
# current player's scores using dense ranking (i.e. tied scores re-
# ceive the same rank placement).

# Solution: we create a dictionary that keeps track of the existing
#           ranks and compare it to the player scores, incrementing
#           the rank counter whenever the player score is less than
#           an existing rank.
#           Time complexity: O(N^2)


def climbingLeaderboard(ranked, player):
    player_ranks = [-1] * len(player)  # initiate array

    if ranked[0] < player[-1]:  # exit case: player score > current rank 1
        player_ranks[-1] = 1

    start = 0
    end = len(player)

    if player_ranks[-1] == 1:
        end = len(player) - 1

    ranked_set = list(sorted(set(ranked), reverse=True))
    ranked_dict = {}

    for idx, x in enumerate(ranked_set):
        ranked_dict[idx + 1] = x

    print(ranked_dict)

    dict_keys = list(ranked_dict.keys())
    r_start = len(dict_keys) - 1

    for x in range(start, end):
        found = 0
        for y in range(r_start, -1, -1):
            rk = dict_keys[y]

            if player[x] < ranked_dict[rk]:
                player_ranks[x] = rk + 1

                ranked_dict[rk + 1] = player[x]
                found = 1
                r_start = y

                break
        if found == 0:
            player_ranks[x] = 1

    return player_ranks


