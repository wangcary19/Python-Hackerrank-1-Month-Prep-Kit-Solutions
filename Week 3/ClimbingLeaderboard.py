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
    player_ranks = []

    r = list(sorted(set(ranked), reverse=True))

    for i in range(0, len(player)):
        for x in range(0, len(r)):
            if player[i] < r[-1]:
                player_ranks.append(len(r) + 1)
                break
            elif player[i] > r[0]:
                player_ranks.append(1)
                break
            elif player[i] >= r[x]:
                player_ranks.append(x + 1)
                break
            else:
                continue

    print(player_ranks)

    return player_ranks


t_ranked = [100, 100, 50, 40, 40, 20, 10]  # 100, 50, 40, 20, 10
t_play = [5, 25, 50, 120]
climbingLeaderboard(t_ranked, t_play)

