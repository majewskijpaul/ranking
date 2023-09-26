import math
import numpy as np
import matplotlib.pyplot as plt

initialScores = {
    'MAX': 1500,
    'GRACEY': 1500,
    'BOGDAN': 1500,
    'CHRISTIAN': 1500,
    'HAYWAD': 1500,
    'JESSIE': 1500,
    'GRACEZ': 1500,
    'JUSTIN': 1500,
    'PAUL': 1500,
    'SAMSON': 1500,
    'PHILLIP': 1500,
    'PREM': 1500,
    'SHUOTONG': 1500,
    'ANNA': 1500,
    'CARMEN': 1500,
}

initialScoresArray = {
    'MAX': [1500],
    'GRACEY': [1500],
    'BOGDAN': [1500],
    'CHRISTIAN': [1500],
    'HAYWAD': [1500],
    'JESSIE': [1500],
    'GRACEZ': [1500],
    'JUSTIN': [1500],
    'PAUL': [1500],
    'SAMSON': [1500],
    'PHILLIP': [1500],
    'PREM': [1500],
    'SHUOTONG': [1500],
    'ANNA': [1500],
    'CARMEN': [1500],
}

# pointsGainedArray = {
#     'MAX': [1500],
#     'GRACEY': [1500],
#     'BOGDAN': [1500],
#     'CHRISTIAN': [1500],
#     'HAYWAD': [1500],
#     'JESSIE': [1500],
#     'GRACEZ': [1500],
#     'JUSTIN': [1500],
#     'PAUL': [1500],
#     'SAMSON': [1500],
#     'PHILLIP': [1500],
#     'PREM': [1500],
#     'SHUOTONG': [1500],
#     'ANNA': [1500],
#     'CARMEN': [1500],
# }

pointsGainedArray = {
    'BOGDAN': [1500],
    'PREM': [1500],
    'ANNA': [1500],
    'HAYWAD': [1500],
    'SAMSON': [1500],
    'GRACEZ': [1500],
    'MAX': [1500],
    'CARMEN': [1500],
    'CHRISTIAN': [1500],
    'GRACEY': [1500],
    'JESSIE': [1500],
    'JUSTIN': [1500],
    'PAUL': [1500],
    'PHILLIP': [1500],
    'SHUOTONG': [1500],
}

matchArray = [
    ["MAX", "GRACEY", 15, 13, 1],
    ["BOGDAN", "CHRISTIAN", 15, 1, 1],
    ["JESSIE", "HAYWAD", 13, 15, 1],
    ["GRACEZ", "JUSTIN", 15, 10, 1],
    ["PAUL", "SAMSON", 5, 15, 1],
    ["PHILLIP", "PREM", 8, 15, 1],
    ["SHUOTONG", "ANNA", 5, 15, 1],
    ["MAX", "BOGDAN", 6, 15, 2],
    ["HAYWAD", "GRACEZ", 15, 9, 2],
    ["SAMSON", "PREM", 9, 15, 2],
    ["ANNA", "CARMEN", 15, 3, 2],
    ["BOGDAN", "HAYWAD", 15, 4, 3],
    ["BOGDAN", "HAYWAD", 15, 1, 3],
    ["PREM", "ANNA", 15, 8, 4],
    ["PREM", "ANNA", 15, 6, 4],
    ["BOGDAN", "PREM", 15, 10, 5],
    ["BOGDAN", "PREM", 15, 7, 5],
]


def calculate_tournament_ranking_array(player_a, player_b, score_a, score_b, tournament_round):

    rating_a = initialScoresArray[player_a][len(initialScoresArray[player_a]) - 1]
    rating_b = initialScoresArray[player_b][len(initialScoresArray[player_b]) - 1]

    expected_a = 1 / (1 + pow(10, (rating_a - rating_b) / 400))
    expected_b = 1 - expected_a

    # the value of the mov_multiplier is [2, 2.7386]
    # This may need to be changed for non-tournament games. Old formula was np.sqrt(abs((score_a - score_b)/2))
    margin_of_victory_multiplier = np.sqrt(max(abs((score_a - score_b)/2), 2))

    # In round 1, the tournament multiplier is 1. Then it decreases each round, to 2/3, then 1/2, then 2/5
    tournament_multiplier = 1 if tournament_round is None else 2 / (1 + tournament_round)

    k_constant = 24

    win_multiplier = 1.15

    if score_a > score_b:
        points_gained = (k_constant * win_multiplier * margin_of_victory_multiplier * tournament_multiplier * (
                    1 - expected_a))
        new_a = rating_a + (k_constant * win_multiplier * margin_of_victory_multiplier * tournament_multiplier * (
                    1 - expected_a))
        initialScoresArray[player_a].append(new_a)
        initialScoresArray[player_b].append(initialScoresArray[player_b][len(initialScoresArray[player_b]) - 1])
        pointsGainedArray[player_a].append(points_gained)
        pointsGainedArray[player_b].append(0)
    else:
        points_gained = (k_constant * win_multiplier * margin_of_victory_multiplier * tournament_multiplier * (
                    1 - expected_b))
        new_b = rating_b + (k_constant * win_multiplier * margin_of_victory_multiplier * tournament_multiplier * (
                    1 - expected_b))
        initialScoresArray[player_b].append(new_b)
        initialScoresArray[player_a].append(initialScoresArray[player_a][len(initialScoresArray[player_a]) - 1])
        pointsGainedArray[player_b].append(points_gained)
        pointsGainedArray[player_a].append(0)


if __name__ == '__main__':
    for match in matchArray:
        player_a = match[0]
        player_b = match[1]
        score_a = match[2]
        score_b = match[3]
        tournament_round = match[4]
        calculate_tournament_ranking_array(player_a, player_b, score_a, score_b, tournament_round)

    final_tournament_scores = []
    keys = list(initialScoresArray.keys())
    values = list(initialScoresArray.values())
    for value in values:
        final_tournament_scores.append(value[len(value) - 1])

    sorted_value_index = np.argsort(final_tournament_scores)[::-1]
    # This is just the final score
    sorted_tournament_results = {keys[i]: final_tournament_scores[i] for i in sorted_value_index}



    figure, axis = plt.subplots(1, 2)

    tournament_scores = {}
    for key, value in sorted_tournament_results.items():
        tournament_scores[key] = initialScoresArray[key]

    for key, value in tournament_scores.items():
        # if the player lost the first round, then do not plot their score (will produce clutter)
        if value[1] != 1500:
            axis[0].plot(value, label=key)
            axis[0].set(ylim=[1490, 1620])

    for key, value in pointsGainedArray.items():
        while len(value) < 7:
            value.append(0)
        pointsGainedArray[key] = np.array(value)

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    players = list(pointsGainedArray.keys())
    points = np.array(list(pointsGainedArray.values())).T
    bottom = np.zeros(len(players))

    tournament_labels = ("Initial Score", "Round 1", "Quarterfinals", "Semifinals G1", "Semifinals G2", "Finals G1", "Finals G2")

    for i in range(len(points)):
        axis[1].bar(players, points[i], 0.5, label=tournament_labels[i], bottom=bottom)
        axis[1].set(ylim=[1490, 1620])
        bottom += points[i]

    axis[0].legend()
    axis[0].set_title("Points Gained after Each Round")

    axis[1].legend()
    axis[1].set_title("Points Gained After Each Round")


    plt.setp(axis[1].get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    plt.setp(axis[0].get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    axis[0].set_xticks(np.arange(7), ('Initial Score', 'Round 1', 'Quarterfinals', 'Semifinals G1', 'Semifinals G2', 'Finals G1', 'Finals G2'))
    plt.show()