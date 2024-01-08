import math
import numpy as np
import matplotlib.pyplot as plt
import tkinter
from matches_2023 import regular_match_array, regular_match_rankings_array, tournament_match_array, tournament_rankings_array, points_gained_after_each_round

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
head_to_head = {}

color_dict = {
        "PREM": "#1f77b4",
        "ANNA": "#ff7f0e",
        "PAUL": "#2ca02c",
        "PHILLIP": "#d62728",
        "TUSHAR": "#9467bd",
        "GRACEY": "#e377c2",
        "GRACEZ": "#8C52FF",
        "JUSTIN": "#E1C16E",
        "CARMEN": "#17becf",
        "SHUOTONG": "#b23c17",
        "CHRISTIAN": "#b23c17",
        "GAB": "#8c564b",
        "JACK": "#097969",
        "BOGDAN": "#ff7f0e",
        "NESMA": "#2ca02c",
        "ANTHONY": "#17becf",
        "JEREMY": "#5D3FD3",
        "JESSIE": "#b23c17",
        "MAX": "#b23c17",
        "HAYWAD": "#8c564b",
        "SAMSON": "#17becf",
        "WILSON": "	#00A36C",
        "CERI": "#b23c17",
        "JONATHAN": "#000000",
        "GARY": "#097969"
}

name_abbrev = {
    "PREM": "PREM",
    "ANNA": "ANNA",
    "PAUL": "PAUL",
    "PHILLIP": "PHIL",
    "TUSHAR": "TUSH",
    "GRACEY": "GY",
    "GRACEZ": "GZ",
    "JUSTIN": "JUST",
    "CARMEN": "CARM",
    "SHUOTONG": "SHUO",
    "CHRISTIAN": "CHR",
    "GAB": "GAB",
    "JACK": "JACK",
    "BOGDAN": "BODG",
    "NESMA": "NES",
    "ANTHONY": "ANTH",
    "JESSIE": "JESS",
    "MAX": "MAX",
    "HAYWAD": "HAY",
    "SAMSON": "SAM",
    "WILSON": "WIL",
    "CERI": "CERI",
    "JEREMY": "JER",
    "JONATHAN": "JON",
    "GARY": "GARY",
}

regular_match_rankings_array_2024 = {
    "BOGDAN": [1500],
    "PREM": [1500],
    "ANNA": [1500],
    "GRACEZ": [1500],
    "GRACEY": [1500],
    "MAX": [1500],
    "CARMEN": [1500],
    "CHRISTIAN": [1500],
    "JESSIE": [1500],
    "JUSTIN": [1500],
    "PAUL": [1500],
    "PHILLIP": [1500],
    "TUSHAR": [1500],
    "JACK": [1500],
    "ANTHONY": [1500],
    "CERI": [1500],
    "WILSON": [1500],
    "JONATHAN": [1500],
    "GARY": [1500],
}

regular_match_array_2024 = [
    ["PAUL", "PHILLIP", 13, 15, "2024-01-02"],
    ["JUSTIN", "ANTHONY", 16, 14, "2024-01-02"],
    ["GRACEZ", "JACK", 15, 13, "2024-01-02"],
    ["GRACEY", "JACK", 15, 12, "2024-01-02"],
    ["PREM", "PHILLIP", 15, 6, "2024-01-02"],
    ["ANTHONY", "TUSHAR", 8, 15, "2024-01-02"],
    ["PAUL", "PHILLIP", 15, 12, "2024-01-02"],
    ["JUSTIN", "TUSHAR", 6, 15, "2024-01-02"],
    ["ANTHONY", "JUSTIN", 11, 15, "2024-01-02"],
    ["GRACEZ", "PAUL", 5, 15, "2024-01-02"],
    ["TUSHAR", "PREM", 19, 17, "2024-01-02"],

    ["ANTHONY", "JUSTIN", 13, 15, "2024-01-03"],
    ["ANNA", "GRACEY", 15, 9, "2024-01-03"],
    ["GRACEZ", "GRACEY", 15, 5, "2024-01-03"],
    ["GRACEY", "GRACEZ", 15, 6, "2024-01-03"],
    ["GARY", "JUSTIN", 11, 9, "2024-01-03"],
    ["GARY", "PHILLIP", 15, 8, "2024-01-03"],
    ["ANNA", "PAUL", 12, 15, "2024-01-03"],
    ["JONATHAN", "ANNA", 2, 15, "2024-01-03"],
    ["JUSTIN", "ANTHONY", 15, 8, "2024-01-03"],
    ["PAUL", "ANTHONY", 15, 11, "2024-01-03"],
    ["PHILLIP", "GRACEY", 13, 15, "2024-01-03"],

    ["ANTHONY", "TUSHAR", 2, 15, "2024-01-04"],
    ["JUSTIN", "TUSHAR", 13, 15, "2024-01-04"],
    ["JUSTIN", "PREM", 9, 15, "2024-01-04"],
    ["PHILLIP", "ANNA", 15, 11, "2024-01-04"],
    ["ANNA", "PHILLIP", 15, 10, "2024-01-04"],
    ["PHILLIP", "ANNA", 5, 15, "2024-01-04"],
    ["GRACEZ", "JACK", 15, 13, "2024-01-04"],
    ["GRACEZ", "PAUL", 12, 15, "2024-01-04"],
    ["TUSHAR", "GRACEY", 15, 5, "2024-01-04"],
    ["GRACEY", "TUSHAR", 4, 15, "2024-01-04"],
    ["GRACEY", "PREM", 6, 15, "2024-01-04"],
    ["ANTHONY", "JUSTIN", 15, 13, "2024-01-04"],
    ["PAUL", "PHILLIP", 15, 7, "2024-01-04"],
    ["GRACEZ", "PHILLIP", 7, 15, "2024-01-04"],

    ["GRACEZ", "JACK", 14, 16, "2024-01-05"],
    ["PAUL", "PHILLIP", 16, 14, "2024-01-05"],
    ["PAUL", "ANNA", 15, 12, "2024-01-05"],
    ["JUSTIN", "TUSHAR", 6, 15, "2024-01-05"],
    ["PAUL", "JUSTIN", 15, 9, "2024-01-05"],
    ["GRACEZ", "JUSTIN", 9, 15, "2024-01-05"],
    ["PHILLIP", "JUSTIN", 9, 15, "2024-01-05"],
    ["PHILLIP", "PAUL", 12, 15, "2024-01-05"],
    ["PAUL", "PHILLIP", 15, 13, "2024-01-05"],
    ["GRACEZ", "TUSHAR", 3, 15, "2024-01-05"],
    ["JACK", "TUSHAR", 7, 15, "2024-01-05"],
    ["ANNA", "JUSTIN", 15, 8, "2024-01-05"],
    ["GRACEZ", "JACK", 10, 15, "2024-01-05"],
    ["JACK", "GRACEZ", 15, 9, "2024-01-05"],
    ["PREM", "JUSTIN", 15, 13, "2024-01-05"],

    ["GRACEZ", "JACK", 12, 15, "2024-01-08"],
    ["ANTHONY", "JUSTIN", 15, 13, "2024-01-08"],
    ["PHILLIP", "ANNA", 11, 15, "2024-01-08"],
    ["ANNA", "PHILLIP", 12, 15, "2024-01-08"],
    ["PHILLIP", "ANNA", 16, 14, "2024-01-08"],
    ["PAUL", "PHILLIP", 15, 7, "2024-01-08"],
    ["PHILLIP", "PAUL", 13, 15, "2024-01-08"],
    ["ANTHONY", "GRACEZ", 15, 13, "2024-01-08"],

    # ["", "", 2, 15, "2024-01-09"],

    # ["", "", 2, 15, "2024-01-10"],

    # ["", "", 2, 15, "2024-01-11"],

    # ["", "", 2, 15, "2024-01-12"],

    # ["", "", 2, 15, "2024-01-15"],
]

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
    print("before: ", points_gained_after_each_round)
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

    print("after: ", points_gained_after_each_round)
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    players = list(points_gained_after_each_round.keys())
    points = np.array(list(points_gained_after_each_round.values())).T
    bottom = np.zeros(len(players))


    tournament_labels = ("Initial Score", "Round 1", "Quarterfinals", "Semifinals G1", "Semifinals G2", "Finals G1", "Finals G2")
    print(len(players), points.shape, len(tournament_labels), bottom.shape)

    for i in range(len(points)):
        # print(points[i])
        axis[1].bar(players, points[i], 0.5, label=tournament_labels[i], bottom=bottom)
        axis[1].set(ylim=[1490, 1610])
        bottom += points[i]

    # print("players", players, players.shape),
    print("points", points, points.shape),
    print("bottom", bottom, bottom.shape)
    # print("tournament labels", tournament_labels, tournament_labels.shape)

    axis[0].legend()
    axis[0].set_title("Points Gained after Each Round")

    axis[1].legend()
    axis[1].set_title("Points Gained After Each Round")


    plt.setp(axis[1].get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    plt.setp(axis[0].get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    axis[0].set_xticks(np.arange(7), ('Initial Score', 'Round 1', 'Quarterfinals', 'Semifinals G1', 'Semifinals G2', 'Finals G1', 'Finals G2'))
    plt.show()

# Returns the new ratings of two players after a game using the game's score.
def calculate_match_rankings(player_a, player_b, score_a, score_b, initial_array):
    rating_a = initial_array[player_a][-1]
    rating_b = initial_array[player_b][-1]

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

def update_regular_match_rankings_array(ranking_array, initial_array):
    for match in ranking_array:
        # update the scores of each player and append it to the end of their ranking array.
        player_a, player_b, score_a, score_b = match[0], match[1], match[2], match[3]
        new_a, new_b = calculate_match_rankings(player_a, player_b, score_a, score_b, initial_array)
        initial_array[player_a].append(new_a)
        initial_array[player_b].append(new_b)

        for player, score_array in initial_array.items():
            # if the player was not present in the current game, their score stays the same
            if player not in [player_a, player_b]:
                initial_array[player].append(initial_array[player][-1])

def plot_regular_match_results():
    update_regular_match_rankings_array(regular_match_array_2024, regular_match_rankings_array_2024)
    pickradius = 5
    map_legend_to_ax = {}
    map_legend_to_text = {}
    fig, ax = plt.subplots()

    plt.subplots_adjust(bottom=0.05, top=0.95, right=0.95, left=0.05)
    all_lines = []
    all_texts = []
    for key, value in regular_match_rankings_array_2024.items():
        # exclude people who don't play often to avoid clutter
        if key not in ["MAX", "SHUOTONG", "BOGDAN", "CHRISTIAN", "JESSIE", "SAMSON", "HAYWAD", "NESMA", "CARMEN", "CERI", "WILSON"]:
            start_index = next((i for i, v in enumerate(value) if v != value[0]), len(value))
            modified_value = value
            if start_index > 5:
                start_index = start_index - 3
                modified_value = [None] * start_index + list(value[start_index:])

            line,  = ax.plot(range(len(regular_match_array_2024) + 1), modified_value, color=color_dict[key], label=key)
            all_lines.append(line)
            for index, element in enumerate(value):
                if index == len(regular_match_array_2024):
                    text = ax.text(index + 0.3, element - 1.5, f"{key}\n({int(element)})", color=color_dict[key])
                    all_texts.append(text)

    leg = ax.legend(fancybox=True, shadow=True)

    for legend_line, ax_line, ax_text in zip(leg.get_lines(), all_lines, all_texts):
        legend_line.set_picker(pickradius)
        map_legend_to_ax[legend_line] = ax_line
        map_legend_to_text[legend_line] = ax_text

    def on_pick(event):
        legend_line = event.artist

        if legend_line not in map_legend_to_ax:
            return

        ax_line = map_legend_to_ax[legend_line]
        ax_text = map_legend_to_text[legend_line]
        visible = not ax_line.get_visible()
        ax_line.set_visible(visible)
        ax_text.set_visible(visible)

        legend_line.set_alpha(1.0 if visible else 0.2)
        fig.canvas.draw()

    fig.canvas.mpl_connect('pick_event', on_pick)

    leg.set_draggable(True)

    plt.show()

def most_common_matchups():
    for match in regular_match_array:
        player_a, player_b, score_a, score_b = match[0], match[1], match[2], match[3]
        match_tuple = SymmetricTuple((player_a, player_b))
        if number_of_unique_matchups.get(match_tuple, 0) == 0:
            number_of_unique_matchups[match_tuple] = 1
        else:
            number_of_unique_matchups[match_tuple] += 1

def plot_most_common_matchup_pie():
    most_common_matchups()
    calculate_head_to_head()
    fig, ax = plt.subplots()

    labels = []
    games = []
    exclusion_array = ["HAYWAD", "SAMSON", "NESMA"]
    for key, value in number_of_unique_matchups.items():
        if str(key.first_item()) not in exclusion_array and key.second_item() not in exclusion_array:
            if str(key.first_item()) not in head_to_head:
                first_player_wins = head_to_head[str(key.second_item())][str(key.first_item())][1]
                second_player_wins = head_to_head[str(key.second_item())][str(key.first_item())][0]
            else:
                first_player_wins = head_to_head[str(key.first_item())][str(key.second_item())][0]
                second_player_wins = head_to_head[str(key.first_item())][str(key.second_item())][1]
            if value > 3:
                labels.append(
                    f"{str(key.first_item())}({first_player_wins}) VS. {str(key.second_item())}({second_player_wins})")
                games.append(value)

    ax.pie(games, labels=labels)
    plt.show()

def plot_most_common_matchups_bar():
    most_common_matchups()
    calculate_head_to_head()
    fig, ax = plt.subplots(1, 2)

    plt.subplots_adjust(bottom=0.05, top=0.95, right=0.99, left=0.08)

    labels = []
    games = []
    matchup_array = []
    matchup_array_abbrev = []
    first_player_wins_array = []
    second_player_wins_array = []
    wins_array = []
    wins_array_1 = []
    wins_array_2 = []
    exclusion_array = ["HAYWAD", "SAMSON", "NESMA", "BOGDAN"]
    for key, value in number_of_unique_matchups.items():
        if str(key.first_item()) not in exclusion_array and key.second_item() not in exclusion_array:
            if str(key.first_item()) not in head_to_head:
                first_player_wins = head_to_head[str(key.second_item())][str(key.first_item())][1]
                second_player_wins = head_to_head[str(key.second_item())][str(key.first_item())][0]
            else:
                first_player_wins = head_to_head[str(key.first_item())][str(key.second_item())][0]
                second_player_wins = head_to_head[str(key.first_item())][str(key.second_item())][1]
            if value > 3:
                labels.append(f"{str(key.first_item())}({first_player_wins}) VS. {str(key.second_item())}({second_player_wins})")
                games.append(value)
            matchup_array.append(f"{str(key.first_item())} {str(key.second_item())}")
            matchup_array_abbrev.append(f"{name_abbrev[str(key.first_item())]} {name_abbrev[str(key.second_item())]}")
            first_player_wins_array.append(first_player_wins)
            second_player_wins_array.append(second_player_wins)

    half_length = len(matchup_array) // 2
    matchup_array_1 = matchup_array[:-half_length]
    matchup_array_2 = matchup_array[(half_length + 1):]
    matchup_array_1_abbrev = matchup_array_abbrev[:-half_length]
    matchup_array_2_abbrev = matchup_array_abbrev[(half_length + 1):]
    matchup_array_1_player_1_color_array, matchup_array_1_player_2_color_array, matchup_array_2_player_1_color_array, matchup_array_2_player_2_color_array = [], [], [], []
    ma_1_color_array, ma_2_color_array = [], []
    ma_1_info_array = []

    for full_name in matchup_array_1:
        player_1, player_2 = full_name.split(" ", 1)
        matchup_array_1_player_1_color_array.append(color_dict[player_1])
        matchup_array_1_player_2_color_array.append(color_dict[player_2])

    for full_name in matchup_array_2:
        player_1, player_2 = full_name.split(" ", 1)
        matchup_array_2_player_1_color_array.append(color_dict[player_1])
        matchup_array_2_player_2_color_array.append(color_dict[player_2])

    for i, names in enumerate(matchup_array):
        total_games = first_player_wins_array[i] + second_player_wins_array[i]
        p1_wins = first_player_wins_array[i]
        p2_wins = second_player_wins_array[i]
        p1_wr = first_player_wins_array[i]/total_games
        p2_wr =second_player_wins_array[i]/total_games
        ma_1_info_array.append([total_games, p1_wins, p2_wins, p1_wr, p2_wr])

    ma_1_color_array.extend([matchup_array_1_player_1_color_array, matchup_array_1_player_2_color_array])
    ma_2_color_array.extend([matchup_array_2_player_1_color_array, matchup_array_2_player_2_color_array])

    wins_array_1.extend([first_player_wins_array[:-half_length], second_player_wins_array[:-half_length]])
    wins_array_2.extend([first_player_wins_array[(half_length + 1):], second_player_wins_array[(half_length + 1):]])

    bottom_1 = np.zeros(len(matchup_array_1))
    bottom_2 = np.zeros(len(matchup_array_2))
    temp_points_1 = np.array(wins_array_1)
    temp_points_2 = np.array(wins_array_2)

    wins_array.extend([first_player_wins_array, second_player_wins_array])

    custom_labels = ("player 1 wins", "player 2 wins")

    for i in range(len(temp_points_1)):
        ax[0].barh(matchup_array_1_abbrev, temp_points_1[i], 0.8, label=custom_labels[i], left=bottom_1, color=ma_1_color_array[i])
        bottom_1 += temp_points_1[i]

    for i in range(len(temp_points_1)):
        ax[1].barh(matchup_array_2_abbrev, temp_points_2[i], 0.8, label=custom_labels[i], left=bottom_2, color=ma_2_color_array[i])
        bottom_2 += temp_points_2[i]

    for c in ax[0].containers:
        ax[0].bar_label(c, label_type="center")

    for c in ax[1].containers:
        ax[1].bar_label(c, label_type="center")

    plt.show()

def calculate_head_to_head():
    for match in regular_match_array:
        player_a, player_b, score_a, score_b, round = match
        # player_1 will always be the alphabetical player
        # for example, Alice vs Bob (player_a vs player_b) => Alice (player_1), Bob (player_2)
        # alternatively, Bob vs Alice (player_a vs player_b) => Bob (player_2), Alice (player_1)
        if player_a < player_b:
            player_1, player_2 = player_a, player_b
        else:
            player_1, player_2 = player_b, player_a

        if player_1 not in head_to_head:
            head_to_head[player_1] = {}
        if player_2 not in head_to_head[player_1]:
            head_to_head[player_1][player_2] = [0, 0]

        # player_a wins.
        if score_a > score_b:
            head_to_head[player_1][player_2][0 if player_a < player_b else 1] += 1
        else:
            head_to_head[player_1][player_2][1 if player_a < player_b else 0] += 1

def calculate_number_of_matchups():
    fig, ax = plt.subplots()
    games_counter_object = {}
    percent_games_played_object = {}
    total_games_recorded = len(regular_match_array)
    labels = []
    values = []
    colors = []
    exclusion_array = ["MAX", "SHUOTONG", "BOGDAN", "CHRISTIAN", "JESSIE", "SAMSON", "HAYWAD", "NESMA", "CARMEN", "CERI"]
    for match in regular_match_array:
        player_a, player_b, score_a, score_b, round = match
        if player_a not in games_counter_object:
            games_counter_object[player_a] = 1
        else:
            games_counter_object[player_a] += 1
        if player_b not in games_counter_object:
            games_counter_object[player_b] = 1
        else:
            games_counter_object[player_b] += 1

    sorted_dict = dict(sorted(games_counter_object.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_dict.items():
        if key not in exclusion_array:
            colors.append(color_dict[key])
            new_value = (value/total_games_recorded) * 100
            rounded_number = "{:.1f}".format(new_value)
            labels.append(f"{key}: {value} games, ({rounded_number}%)")
            percent_games_played_object[key] = (value/total_games_recorded) * 100
            values.append(((value/total_games_recorded) * 100))
    ax.pie(values, labels=labels, colors=colors)
    plt.show()

if __name__ == '__main__':
    # plot_tournament_results()

    # plot_most_common_matchups_bar()

    # plot_most_common_matchup_pie()

    plot_regular_match_results()

    # calculate_number_of_matchups()