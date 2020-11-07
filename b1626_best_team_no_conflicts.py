"""
sort list in increasing order by age, then score
iterate through players
    1st player goes into group
    next player goes into same group if no conflict
        otherwise create new group
    keep going until have at most n groups
calculate sum of scores

(5,1), (1,8), (2,9), (3,10)

10 9 8 1
 3 2 1 5

 3 

"""

def best_team(scores, ages):
    #
    """
    """
    score_pair = sorted([*zip(ages, scores)], reverse=True)
    score_tracker = [score for age, score in score_pair]

    max_score = 0

    for i in range(len(score_pair)):
        current_score = score_tracker[i]

        for age in range(i):
            if score_pair[age][1] >= current_score:
                score_tracker[i] = max(score_tracker[i], score_tracker[age] + current_score)

        max_score = max(max_score, score_tracker[i])

    return max_score


if __name__ == "__main__":
    print(best_team([1,2,3,5], [8,9,10,1]))
