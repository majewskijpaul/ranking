import math
import numpy as np
import matplotlib.pyplot as plt

class SymmetricTuple:
    def __init__(self, items):
        self.items = tuple(sorted(items))

    def __eq__(self, other):
        return set(self.items) == set(other.items)

    def __hash__(self):
        return hash(self.items)

    def __str__(self):
        return str(self.items)

    def first_item(self):
        return self.items[0]

    def second_item(self):
        return self.items[1]

timesShowedUp = {}
tournament_scores = {}
number_of_unique_matchups = {}
color_dict = {
        "PREM": "#1f77b4",
        "ANNA": "#ff7f0e",
        "PAUL": "#2ca02c",
        "PHILLIP": "#d62728",
        "TUSHAR": "#9467bd",
        "GRACEY": "#e377c2",
        "GRACEZ": "#7f7f7f",
        "JUSTIN": "#bcbd22",
        "CARMEN": "#17becf",
        "SHUOTONG": "#b23c17",
        "CHRISTIAN": "#b23c17",
        "GAB": "#8c564b",
        "JACK": "#2f4f4f",
        "BOGDAN": "#ff7f0e",
        "NESMA": "#2ca02c",
        "ANTHONY": "#17becf",
        "JESSIE": "#b23c17",
        "MAX": "#b23c17",
        "HAYWAD": "#8c564b",
        "SAMSON": "#17becf",
}

tournament_rankings_array = {
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

points_gained_after_each_round = {
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

tournament_match_array = [
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

regular_match_array = [
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
  ["TUSHAR", "ANNA", 15, 12, None],
  ["PAUL", "PHILLIP", 15, 7, None],
  ["PHILLIP", "ANNA", 15, 8, None],
  ["PREM", "ANNA", 16, 14, None],
  ["PHILLIP", "GRACEY", 19, 17, None],
  ["PREM", "PAUL", 15, 13, None],
  ["PHILLIP", "ANNA", 12, 15, None],
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
  ["PHILLIP", "PREM", 1, 15, None],
  ["PHILLIP", "PREM", 2, 15, None],
  ["GRACEY", "ANNA", 15, 11, None],
  ["JUSTIN", "CARMEN", 7, 11, None],
  ["ANNA", "PAUL", 15, 11, None],
  ["JUSTIN", "TUSHAR", 7, 15, None],
  ["JUSTIN", "ANNA", 8, 15, None],
  ["PAUL", "TUSHAR", 9, 15, None],
  # Monday October 2
  # Tuesday October 3
  ["PREM", "ANNA", 15, 7, None],
  ["PREM", "ANNA", 15, 10, None],
  ["NESMA", "GRACEY", 7, 11, None],
  ["PAUL", "PHILLIP", 15, 8, None],
  ["PHILLIP", "PAUL", 15, 10, None],
  ["TUSHAR", "GRACEY", 15, 13, None],
  ["PHILLIP", "ANNA", 9, 15, None],
  ["JUSTIN", "CARMEN", 7, 11, None],
  ["PAUL", "TUSHAR", 15, 11, None],
  ["JUSTIN", "ANNA", 8, 15, None],
  ["ANNA", "JUSTIN", 15, 12, None],
  ["TUSHAR", "PAUL", 15, 10, None],
  ["PHILLIP", "JACK", 15, 7, None],
  ["PHILLIP", "GAB", 15, 6, None],
  ["GRACEY", "CARMEN", 15, 9, None],
  ["GAB", "JUSTIN", 8, 15, None],
  ["TUSHAR", "ANNA", 15, 9, None],
  ["PAUL", "ANNA", 13, 15, None],
  ["PAUL", "GRACEY", 15, 6, None],
  ["JUSTIN", "GRACEY", 15, 11, None],
  ["GAB", "GRACEY", 15, 11, None],
  ["PREM", "GRACEY", 15, 11, None],
#   Wednesday October 4
  ["PAUL", "TUSHAR", 9, 15, None],
  ["GRACEY", "ANNA", 9, 15, None],
  ["TUSHAR", "JUSTIN", 15, 7, None],
  ["PREM", "TUSHAR", 19, 17, None],
  ["PREM", "TUSHAR", 15, 11, None],
  ["PAUL", "ANNA", 15, 9, None],
  ["JUSTIN", "GRACEZ", 7, 11, None],
  ["JUSTIN", "CARMEN", 11, 7, None],
  ["GAB", "CHRISTIAN", 16, 14, None],
  ["PREM", "JUSTIN", 15, 13, None],
  ["ANNA", "PAUL", 12, 15, None],
  ["PREM", "PAUL", 15, 4, None],
  # Thursday October 5
  ["PREM", "JUSTIN", 15, 0, None],
  ["JUSTIN", "PREM", 6, 15, None],
  ["JUSTIN", "ANNA", 7, 15, None],
  ["GRACEY", "ANNA", 5, 15, None],
  ["GRACEY", "PHILLIP", 10, 15, None],
  ["JUSTIN", "PHILLIP", 10, 15, None],
  ["GAB", "JACK", 11, 15, None],
  ["GRACEY", "JACK", 15, 3, None],
  ["TUSHAR", "PHILLIP", 15, 7, None],
  ["ANNA", "PREM", 9, 15, None],
  ["BOGDAN", "TUSHAR", 17, 15, None],
  ["PAUL", "ANNA", 11, 15, None],
  ["GAB", "PHILLIP", 8, 15, None],
  ["PHILLIP", "PREM", 8, 15, None],
  ["GAB", "PREM", 7, 15, None],
  ["PREM", "PAUL", 15, 8, None],
  ["ANNA", "PAUL", 15, 10, None],
  # Friday October 6
  ["PHILLIP", "JUSTIN", 15, 7, None],
  ["JUSTIN", "GAB", 11, 3, None],
  ["GRACEY", "PREM", 6, 15, None],
  ["PREM", "TUSHAR", 15, 13, None],
  ["TUSHAR", "PREM", 15, 12, None],
  ["PHILLIP", "PREM", 7, 15, None],
  ["PREM", "PHILLIP", 16, 14, None],
  # Tuesday October 10
  ["PHILLIP", "PAUL", 15, 12, None],
  ["GAB", "JACK", 15, 12, None],
  ["GAB", "PAUL", 10, 15, None],
  ["NESMA", "PHILLIP", 6, 15, None],
  ["ANNA", "PHILLIP", 15, 7, None],
  ["PAUL", "PREM", 11, 15, None],
  # Wednesday October 11
  ["ANNA", "JUSTIN", 17, 15, None],
  ["ANNA", "PREM", 15, 10, None],
  ["PHILLIP", "PAUL", 15, 13, None],
  ["GRACEZ", "JACK", 14, 16, None],
  ["PAUL", "GAB", 15, 8, None],
  ["PAUL", "NESMA", 11, 6, None],
  ["PHILLIP", "PREM", 10, 15, None],
  ["ANNA", "GRACEY", 15, 7, None],
  ["PHILLIP", "ANNA", 14, 16, None],

  # Thursday October 12
  ["PHILLIP", "JUSTIN", 19, 17, None],
  ["PREM", "ANNA", 10, 15, None],
  ["ANNA", "PREM", 15, 12, None],
  ["ANNA", "TUSHAR", 13, 15, None],
  ["ANTHONY", "GRACEY", 7, 15, None],
  ["TUSHAR", "PAUL", 15, 11, None],
  ["PAUL", "PHILLIP", 15, 17, None],
  ["GAB", "PHILLIP", 8, 15, None],
  ["GAB", "ANNA", 4, 15, None],
  ["JUSTIN", "GAB", 15, 8, None],
  ["TUSHAR", "PREM", 15, 13, None],
  ["GRACEY", "JUSTIN", 15, 10, None],
  ["PHILLIP", "PAUL", 12, 15, None],
  ["ANTHONY", "JUSTIN", 10, 15, None],
  # Friday October 13
  # Monday October 16
]

# static rating given to players after the tournament (TUSHAR was added after the fact)
regular_match_rankings_array = {
    "BOGDAN": [1602],
    "PREM": [1564],
    "ANNA": [1551],
    "HAYWAD": [1536],
    "SAMSON": [1531],
    "GRACEZ": [1521],
    "GRACEY": [1500],
    "MAX": [1520],
    "CARMEN": [1500],
    "CHRISTIAN": [1500],
    "JESSIE": [1500],
    "JUSTIN": [1500],
    "PAUL": [1500],
    "PHILLIP": [1500],
    "SHUOTONG": [1500],
    "TUSHAR": [1500],
    "GAB": [1500],
    "JACK": [1500],
    "NESMA": [1500],
    "ANTHONY": [1500]
}

# Calculates the ratings of all players after the tournament.
def calculate_tournament_rankings(player_a, player_b, score_a, score_b, tournament_round):
    rating_a = tournament_rankings_array[player_a][-1]
    rating_b = tournament_rankings_array[player_b][-1]

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
        # initialScoresArray[player_a].append(new_a)
        # initialScoresArray[player_b].append(initialScoresArray[player_b][-1])
        # pointsGainedArray[player_a].append(points_gained)
        # pointsGainedArray[player_b].append(0)
        return new_a, tournament_rankings_array[player_b][-1], points_gained, 0
    else:
        points_gained = (k_constant * win_multiplier * margin_of_victory_multiplier * tournament_multiplier * (
                    1 - expected_b))
        new_b = rating_b + (k_constant * win_multiplier * margin_of_victory_multiplier * tournament_multiplier * (
                    1 - expected_b))
        # initialScoresArray[player_b].append(new_b)
        # initialScoresArray[player_a].append(initialScoresArray[player_a][-1])
        # pointsGainedArray[player_b].append(points_gained)
        # pointsGainedArray[player_a].append(0)
        return tournament_rankings_array[player_a][-1], new_b, 0, points_gained

def update_tournament_rankings_array():
    # populates initialScoresArray and pointsGainedArray with updated match results
    for match in tournament_match_array:
        player_a, player_b, score_a, score_b, tournament_round = match[0], match[1], match[2], match[3], match[4]
        rating_a, rating_b, gained_a, gained_b = calculate_tournament_rankings(player_a, player_b, score_a, score_b, tournament_round)
        tournament_rankings_array[player_a].append(rating_a)
        tournament_rankings_array[player_b].append(rating_b)
        points_gained_after_each_round[player_a].append(gained_a)
        points_gained_after_each_round[player_b].append(gained_b)
    final_tournament_scores = []
    keys = list(tournament_rankings_array.keys())
    values = list(tournament_rankings_array.values())
    for value in values:
        final_tournament_scores.append(value[-1])
    # The index location of the top score players in final_tournament_scores
    sorted_value_index = np.argsort(final_tournament_scores)[::-1]
    # use the sorted_value_index to sort the dictionary by value.
    sorted_tournament_results = {keys[i]: final_tournament_scores[i] for i in sorted_value_index}

    # tournament_scores is just initialScoresArray, but with the scores being in order
    for key, value in sorted_tournament_results.items():
        tournament_scores[key] = tournament_rankings_array[key]

def plot_tournament_results():
    update_tournament_rankings_array()

    print(tournament_rankings_array)
    print(points_gained_after_each_round)
    figure, axis = plt.subplots(1, 2)

    # the final score of each player (in the order of the keys of initialScoresArray)

    for key, value in tournament_scores.items():
        # if the player lost the first round, then do not plot their score (will produce clutter)
        if value[1] != 1500:
            axis[0].plot(value, label=key)
            axis[0].set(ylim=[1490, 1610])


    for key, value in points_gained_after_each_round.items():
        while len(value) < 7:
            value.append(0)
        points_gained_after_each_round[key] = np.array(value)

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    players = list(points_gained_after_each_round.keys())
    points = np.array(list(points_gained_after_each_round.values())).T
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

# Returns the new ratings of two players after a game using the game's score.
def calculate_match_rankings(player_a, player_b, score_a, score_b):
    rating_a = regular_match_rankings_array[player_a][-1]
    rating_b = regular_match_rankings_array[player_b][-1]

    expected_a = 1 / (1 + pow(10, (rating_b - rating_a) / 400))
    expected_b = 1 - expected_a

    # margin_of_victory_multiplier = np.sqrt(abs((score_a - score_b) / 2))
    margin_of_victory_multiplier = np.sqrt(max(abs((score_a - score_b)/2), 2))

    #TODO: Add in some kind of overtime bonus that rewards the winner, but doesn't punish the loser.

    k_constant = 16

    if score_a > score_b:
        points_gained_a = k_constant * margin_of_victory_multiplier * (1 - expected_a)
        points_lost_b = k_constant * margin_of_victory_multiplier * (0 - expected_b)
        new_a = rating_a + points_gained_a
        new_b = rating_b + points_lost_b
        # print(f"MATCH: {player_a}({round(rating_a, 2)},{round(expected_a, 3)}) vs {player_b}({round(rating_b, 2)},{round(expected_b, 3)}): {player_a} WINS!  +{round(points_gained_a, 2)}({round(new_a, 2)}) /  {round(points_lost_b, 2)}({round(new_b, 2)})")
        # regular_match_rankings_array[player_a].append(new_a)
        # regular_match_rankings_array[player_b].append(new_b)
        return new_a, new_b
    else:
        points_lost_a = k_constant * margin_of_victory_multiplier * (0 - expected_a)
        points_gained_b = k_constant * margin_of_victory_multiplier * (1 - expected_b)
        new_a = rating_a + points_lost_a
        new_b = rating_b + points_gained_b
        # print(f"MATCH: {player_a}({round(rating_a, 2)},{round(expected_a, 3)}) vs {player_b}({round(rating_b, 2)},{round(expected_b, 3)}): {player_b} WINS!  {round(points_lost_a, 2)}({round(new_a, 2)})  /  +{round(points_gained_b, 2)}({round(new_b, 2)})")
        # regular_match_rankings_array[player_a].append(new_a)
        # regular_match_rankings_array[player_b].append(new_b)
        return new_a, new_b

def update_regular_match_rankings_array():
    for match in regular_match_array:
        # update the scores of each player and append it to the end of their ranking array.
        player_a, player_b, score_a, score_b = match[0], match[1], match[2], match[3]
        new_a, new_b = calculate_match_rankings(player_a, player_b, score_a, score_b)
        regular_match_rankings_array[player_a].append(new_a)
        regular_match_rankings_array[player_b].append(new_b)

        for player, score_array in regular_match_rankings_array.items():
            # if the player was not present in the current game, their score stays the same
            if player not in [player_a, player_b]:
                regular_match_rankings_array[player].append(regular_match_rankings_array[player][-1])

def plot_regular_match_results():
    update_regular_match_rankings_array()
    fig, ax = plt.subplots()
    for key, value in regular_match_rankings_array.items():
        # exclude people who don't play often to avoid clutter
        if key not in ["MAX", "SHUOTONG", "BOGDAN", "CHRISTIAN", "JESSIE", "SAMSON", "HAYWAD", "NESMA", "JACK", "ANTHONY", "CARMEN"]:
            ax.plot(range(len(regular_match_array) + 1), value, color=color_dict[key])
            for index, element in enumerate(value):
                if index == len(regular_match_array):
                    ax.text(index + 0.3, element - 1.5, f"{key}\n({element.round()})", color=color_dict[key])
    plt.show()

def most_common_matchups():
    for match in regular_match_array:
        player_a, player_b, score_a, score_b = match[0], match[1], match[2], match[3]
        match_tuple = SymmetricTuple((player_a, player_b))
        if number_of_unique_matchups.get(match_tuple, 0) == 0:
            number_of_unique_matchups[match_tuple] = 1
        else:
            number_of_unique_matchups[match_tuple] += 1

def plot_most_common_matchups():
    most_common_matchups()
    fig, ax = plt.subplots()
    labels = []
    games = []
    for key, value in number_of_unique_matchups.items():
        if value > 1:
            labels.append(f"{str(key.first_item())} VS. {str(key.second_item())}, {value}")
            games.append(value)

    ax.pie(games, labels=labels)
    plt.show()

if __name__ == '__main__':
    # plot_tournament_results()

    # plot_most_common_matchups()

    plot_regular_match_results()