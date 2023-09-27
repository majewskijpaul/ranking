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

regularGameMatchArray = [
  ["PREM", "HAYWAD", 13, 15, None],
  ["PREM", "SAMSON", 6, 11, None],
  ["PREM", "SAMSON", 11, 7, None],
  ["PREM", "SAMSON", 11, 5, None],
  ["SAMSON", "PREM", 6, 11, None],
  ["PAUL", "PHILLIP", 12, 15, None],
  ["PREM", "PHILLIP", 12, 3, None],
  ["JUSTIN", "ANNA", 7, 11, None],
  ["ANNA", "GRACEY", 15, 7, None],
  ["SAMSON", "PREM", 11, 13, None],
  ["PHILLIP", "SAMSON", 12, 15, None],
  ["PREM", "SAMSON", 11, 5, None],
  ["PREM", "SAMSON", 12, 10, None],
  ["HAYWAD", "SAMSON", 11, 15, None],
  ["PAUL", "SAMSON", 11, 15, None],
  ["ANNA", "SAMSON", 12, 15, None],
  ["PHILLIP", "PAUL", 8, 15, None],
  ["PHILLIP", "PAUL", 10, 15, None],
  ["PAUL", "SAMSON", 12, 15, None],
  ["BOGDAN", "PREM", 14, 12, None],
  ["JUSTIN", "GRACEZ", 15, 10, None],
  ["JUSTIN", "ANNA", 8, 15, None],
  ["PHILLIP", "PAUL", 14, 16, None],
  ["PREM", "HAYWAD", 15, 8, None],
  ["PAUL", "PHILLIP", 11, 15, None],
  ["ANNA", "PHILLIP", 10, 15, None],
  ["GRACEZ", "SAMSON", 8, 11, None],
  ["PAUL", "HAYWAD", 10, 15, None],
  ["TUSHAR", "ANNA", 15, 12, None],
  ["PAUL", "PHILLIP", 15, 7, None],
  ["PHILLIP", "ANNA", 15, 8, None],
  ["PREM", "ANNA", 16, 14, None],
  ["PHILLIP", "GRACEY", 19, 17, None],
  ["PREM", "PAUL", 15, 13, None],
  ["PHILLIP", "ANNA", 12, 15, None],
  ["PREM", "TUSHAR", 15, 13, None],
  ["PAUL", "PHILLIP", 16, 14, None],
  ["PAUL", "ANNA", 13, 15, None],
  ["PREM", "ANNA", 15, 13, None],
  ["PAUL", "PHILLIP", 15, 10, None],
  ["JUSTIN", "GRACEY", 18, 16, None],
  # Thursday September 28
  ["PREM", "HAYWAD", 15, 12, None],
  ["PAUL", "PHILLIP", 15, 12, None],
  ["ANNA", "TUSHAR", 11, 15, None],
  ["PREM", "TUSHAR", 11, 15, None],
  ["TUSHAR", "PAUL", 10, 15, None],
  ["PHILLIP", "ANNA", 12, 15, None],
  ["PHILLIP", "JUSTIN", 16, 14, None],
  ["GRACEZ", "CARMEN", 9, 11, None],
  ["JUSTIN", "CARMEN", 11, 9, None],
  ["GRACEZ", "GRACEY", 5, 11, None],
  ["PREM", "HAYWAD", 15, 11, None],
  ["HAYWAD", "PREM", 12, 15, None],
  ["ANNA", "GRACEY", 15, 5, None],

  # Friday September 29
  ["ANNA", "BOGDAN", 14, 16, None],
  ["PHILLIP", "JUSTIN", 11, 7, None],
  ["PHILLIP", "ANNA", 9, 15, None],
  ["PHILLIP", "PREM", 15, 1, None],
  ["PHILLIP", "PREM", 15, 2, None],
  ["GRACEY", "ANNA", 15, 11, None],
  ["JUSTIN", "CARMEN", 7, 11, None],
  ["ANNA", "PAUL", 15, 11, None],
  ["JUSTIN", "TUSHAR", 7, 15, None],
  ["JUSTIN", "ANNA", 8, 15, None],
  ["PAUL", "TUSHAR", 9, 15, None],
]


def calculate_tournament_ranking_array(player_a, player_b, score_a, score_b, tournament_round):

    rating_a = initialScoresArray[player_a][len(initialScoresArray[player_a]) - 1]
    rating_b = initialScoresArray[player_b][len(initialScoresArray[player_b]) - 1]

    expected_a = 1 / (1 + pow(10, (rating_b - rating_a) / 400))
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

def calculate_match_ranking(player_a, player_b, score_a, score_b):
    rating_a = after_tournament_rankings[player_a][len(after_tournament_rankings[player_a]) - 1]
    rating_b = after_tournament_rankings[player_b][len(after_tournament_rankings[player_b]) - 1]

    expected_a = 1 / (1 + pow(10, (rating_b - rating_a) / 400))
    expected_b = 1 - expected_a

    # margin_of_victory_multiplier = np.sqrt(abs((score_a - score_b) / 2))
    margin_of_victory_multiplier = np.sqrt(max(abs((score_a - score_b)/2), 2))

    #TODO: Add in some kind of overtime bonus that rewards the winner, but doesn't punish the loser.
    #TODO: Phillip vs Prem 12/3 has wayyy too many points on the line.

    k_constant = 16

    if score_a > score_b:
        points_gained_a = k_constant * margin_of_victory_multiplier * (1 - expected_a)
        points_lost_b = k_constant * margin_of_victory_multiplier * (0 - expected_b)
        new_a = rating_a + points_gained_a
        new_b = rating_b + points_lost_b
        print(f"MATCH: {player_a}({round(rating_a, 2)},{round(expected_a, 3)}) vs {player_b}({round(rating_b, 2)},{round(expected_b, 3)}): {player_a} WINS!  +{round(points_gained_a, 2)}({round(new_a, 2)}) /  {round(points_lost_b, 2)}({round(new_b, 2)})")
        after_tournament_rankings[player_a].append(new_a)
        after_tournament_rankings[player_b].append(new_b)
    else:
        points_lost_a = k_constant * margin_of_victory_multiplier * (0 - expected_a)
        points_gained_b = k_constant * margin_of_victory_multiplier * (1 - expected_b)
        new_a = rating_a + points_lost_a
        new_b = rating_b + points_gained_b
        print(f"MATCH: {player_a}({round(rating_a, 2)},{round(expected_a, 3)}) vs {player_b}({round(rating_b, 2)},{round(expected_b, 3)}): {player_b} WINS!  {round(points_lost_a, 2)}({round(new_a, 2)})  /  +{round(points_gained_b, 2)}({round(new_b, 2)})")
        after_tournament_rankings[player_a].append(new_a)
        after_tournament_rankings[player_b].append(new_b)

def plot_tournament_results():
    figure, axis = plt.subplots(1, 2)

    tournament_scores = {}
    for key, value in sorted_tournament_results.items():
        tournament_scores[key] = initialScoresArray[key]

    for key, value in tournament_scores.items():
        # if the player lost the first round, then do not plot their score (will produce clutter)
        if value[1] != 1500:
            axis[0].plot(value, label=key)
            axis[0].set(ylim=[1490, 1610])


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
        # print(points[i])
        axis[1].bar(players, points[i], 0.5, label=tournament_labels[i], bottom=bottom)
        axis[1].set(ylim=[1490, 1610])
        bottom += points[i]

    axis[0].legend()
    axis[0].set_title("Points Gained after Each Round")

    axis[1].legend()
    axis[1].set_title("Points Gained After Each Round")


    plt.setp(axis[1].get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    plt.setp(axis[0].get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    axis[0].set_xticks(np.arange(7), ('Initial Score', 'Round 1', 'Quarterfinals', 'Semifinals G1', 'Semifinals G2', 'Finals G1', 'Finals G2'))
    plt.show()

if __name__ == '__main__':
    # calculate the results of the tournament.
    # this populates initialScoresArray and pointsGainedArray
    for match in matchArray:
        player_a = match[0]
        player_b = match[1]
        score_a = match[2]
        score_b = match[3]
        tournament_round = match[4]
        calculate_tournament_ranking_array(player_a, player_b, score_a, score_b, tournament_round)


    # After the tournament is over, the matches are where you gain and lost points
    after_tournament_rankings = {}
    for key, value in initialScoresArray.items():
        after_tournament_rankings[key] = [value[-1]]

    # Add Tushar to the rankings (he didn't participate in the tournament)
    after_tournament_rankings["TUSHAR"] = [1500]

    for match in regularGameMatchArray:
        player_a = match[0]
        player_b = match[1]
        score_a = match[2]
        score_b = match[3]
        tournament_round = match[4]
        calculate_match_ranking(player_a, player_b, score_a, score_b)

    final_tournament_scores = []
    keys = list(initialScoresArray.keys())
    values = list(initialScoresArray.values())
    for value in values:
        final_tournament_scores.append(value[len(value) - 1])

    sorted_value_index = np.argsort(final_tournament_scores)[::-1]
    # This is just the final score
    sorted_tournament_results = {keys[i]: final_tournament_scores[i] for i in sorted_value_index}

    fig, ax = plt.subplots()

    # for key, value in after_tournament_rankings.items():
    #     if len(value) > 1:
    #         line, = ax.plot(after_tournament_rankings[key], label=key)
    #         ax.text(len(value) - 1, value[-1], key, color=line.get_color())

    counter = 0
    # we need a counter for each person so we know who has played or naw.
    timesShowedUp = {}
    colorDict = {
        "PREM": "#1f77b4",
        "BOGDAN": "#ff7f0e",
        "ANNA": "#2ca02c",
        "PAUL": "#d62728",
        "PHILLIP": "#9467bd",
        "HAYWAD": "#8c564b",
        "GRACEY": "#e377c2",
        "GRACEZ": "#7f7f7f",
        "JUSTIN": "#bcbd22",
        "SAMSON": "#17becf",
        "TUSHAR": "#b23c17",
        "CARMEN": "#b23c17",
        "MAX": "#b23c17",
        "SHUOTONG": "#b23c17",
        "JESSIE": "#b23c17",
        "CHRISTIAN": "#b23c17"
    }
    for game_number, item in enumerate(regularGameMatchArray):
        if timesShowedUp.get(item[0], 0) == 0:
            timesShowedUp[item[0]] = 0
        if timesShowedUp.get(item[1], 0) == 0:
            timesShowedUp[item[1]] = 0
        line, = ax.plot([game_number, game_number+1], [after_tournament_rankings[item[0]][timesShowedUp[item[0]]], after_tournament_rankings[item[0]][timesShowedUp[item[0]] + 1]], label=item[0], color=colorDict[item[0]])
        line, = ax.plot([game_number, game_number+1], [after_tournament_rankings[item[1]][timesShowedUp[item[1]]], after_tournament_rankings[item[1]][timesShowedUp[item[1]] + 1]], label=item[1], color=colorDict[item[1]])
        if timesShowedUp[item[0]] + 1 == len(after_tournament_rankings[item[0]]) - 1:
            ax.text(game_number + 1.2, after_tournament_rankings[item[0]][-1] - 1.5, item[0], color=colorDict[item[0]])
        if timesShowedUp[item[1]] + 1 == len(after_tournament_rankings[item[1]]) - 1: \
            ax.text(game_number + 1.2, after_tournament_rankings[item[1]][-1] - 1.5, item[1], color=colorDict[item[1]])


        timesShowedUp[item[0]] += 1
        timesShowedUp[item[1]] += 1


        # this is how we plot out a single player's journey:
        # if (item[0] == "PREM" and item[1] == "SAMSON") or (item[1] == "PREM" and item[0] == "SAMSON"):
        #     print(index, after_tournament_rankings["PREM"][counter], counter)
        #     line, = ax.plot([index, index+1], [after_tournament_rankings["PREM"][counter], after_tournament_rankings["PREM"][counter + 1]], label="PREM")
        #     line, = ax.plot([index, index + 1], [after_tournament_rankings["SAMSON"][counter], after_tournament_rankings["SAMSON"][counter + 1]], label="SAMSON")
        #     counter += 1
        # else:
        #     line, = ax.plot(np.nan)

    ax.set_xlabel("Games Played")
    ax.set_ylabel("Player Rating")
    plt.show()