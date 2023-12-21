import math
import numpy as np
import matplotlib.pyplot as plt
import tkinter

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
        "JEREMY": "#5D3FD3",
        "JESSIE": "#b23c17",
        "MAX": "#b23c17",
        "HAYWAD": "#8c564b",
        "SAMSON": "#17becf",
        "WILSON": "#b23c17",
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
    "WILSON": "WIL"
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
    ["PAUL", "JACK", 15, 3, None],
    ["JUSTIN", "ANTHONY", 15, 10, None],
    ["JUSTIN", "PREM", 8, 15, None],
    ["JACK", "GAB", 15, 8, None],
    ["PREM", "PAUL", 15, 5, None],
    ["PREM", "ANNA", 15, 7, None],
    ["PAUL", "ANTHONY", 15, 5, None],
    ["PAUL", "ANNA", 14, 16, None],
    ["PREM", "ANNA", 15, 7, None],
    ["PREM", "GAB", 15, 4, None],
    ["NESMA", "GRACEZ", 12, 15, None],
    ["PAUL", "PHILLIP", 15, 11, None],
    ["PHILLIP", "PREM", 11, 15, None],
    ["PREM", "GRACEZ", 15, 9, None],
    ["PREM", "ANTHONY", 15, 4, None],
    ["GAB", "PHILLIP", 2, 15, None],
    ["ANTHONY", "GAB", 11, 15, None],
    ["JUSTIN", "PAUL", 7, 15, None],
    # Monday October 16
    ["PREM", "ANNA", 15, 9, None],
    ["ANNA", "PREM", 10, 15, None],
    ["PAUL", "PHILLIP", 15, 10, None],
    ["PREM", "PHILLIP", 15, 7, None],
    ["PHILLIP", "PREM", 15, 10, None],
    ["TUSHAR", "ANTHONY", 15, 7, None],
    ["TUSHAR", "ANNA", 15, 9, None],
    ["PHILLIP", "TUSHAR", 5, 15, None],
    ["PHILLIP", "ANNA", 15, 11, None],
    ["ANNA", "PHILLIP", 15, 10, None],
    ["PHILLIP", "ANNA", 15, 10, None],
    ["TUSHAR", "PREM", 10, 15, None],
    ["PREM", "TUSHAR", 15, 8, None],
    ["GAB", "JACK", 14, 16, None],
    ["GRACEZ", "GAB", 17, 15, None],
    # Tuesday October 17
    ["PHILLIP", "JUSTIN", 12, 15, None],
    ["PAUL", "PHILLIP", 16, 18, None],
    ["TUSHAR", "GRACEY", 15, 11, None],
    ["TUSHAR", "ANNA", 15, 10, None],
    ["PHILLIP", "ANNA", 15, 11, None],
    ["ANNA", "PHILLIP", 4, 15, None],
    ["JACK", "GAB", 15, 6, None],
    ["PHILLIP", "GRACEY", 15, 10, None],
    ["PAUL", "ANNA", 13, 15, None],
    ["JUSTIN", "GAB", 15, 5, None],
    ["JUSTIN", "GRACEY", 15, 17, None],
    ["TUSHAR", "ANTHONY", 15, 8, None],
    ["PAUL", "GAB", 15, 10, None],
    ["ANTHONY", "GAB", 15, 10, None],
    ["PAUL", "PHILLIP", 17, 15, None],
    ["GRACEZ", "JACK", 13, 15, None],
    ["JUSTIN", "ANTHONY", 15, 13, None],
    ["TUSHAR", "GAB", 15, 9, None],
    ["ANNA", "PAUL", 13, 15, None],
    ["JUSTIN", "ANTHONY", 13, 15, None],
    # Wednesday October 18
    ["JUSTIN", "ANTHONY", 5, 15, None],
    ["GRACEZ", "GAB", 7, 15, None],
    ["ANNA", "GRACEY", 15, 13, None],
    ["PHILLIP", "PAUL", 11, 15, None],
    ["PREM", "GRACEZ", 15, 6, None],
    ["GAB", "JACK", 15, 13, None],
    ["GAB", "NESMA", 15, 17, None],
    ["PREM", "ANNA", 15, 12, None],
    ["PREM", "PHILLIP", 15, 10, None],
    ["TUSHAR", "PREM", 15, 2, None],
    ["ANTHONY", "GAB", 10, 15, None],
    ["NESMA", "GRACEZ", 6, 15, None],
    ["ANNA", "PAUL", 15, 7, None],
    ["JUSTIN", "PHILLIP", 12, 15, None],
    ["PREM", "ANNA", 9, 15, None],
    ["PREM", "GRACEY", 15, 5, None],
    ["ANTHONY", "JUSTIN", 11, 15, None],
    ["GAB", "GRACEY", 15, 12, None],
    ["GAB", "GRACEY", 15, 12, None],
    ["PHILLIP", "PAUL", 22, 20, None],
    ["PAUL", "PHILLIP", 16, 14, None],
    # Thursday October 19
    ["BOGDAN", "TUSHAR", 11, 6, None],
    ["JUSTIN", "ANTHONY", 10, 15, None],
    ["ANNA", "GRACEY", 15, 3, None],
    ["PHILLIP", "PAUL", 11, 15, None],
    ["ANNA", "TUSHAR", 11, 15, None],
    ["GAB", "TUSHAR", 11, 15, None],
    ["PREM", "TUSHAR", 17, 15, None],
    ["GAB", "NESMA", 11, 15, None],
    ["ANNA", "GAB", 15, 7, None],
    ["GRACEZ", "JACK", 12, 15, None],
    ["PAUL", "PREM", 13, 15, None],
    ["GRACEY", "GRACEZ", 15, 11, None],
    ["PAUL", "PHILLIP", 15, 4, None],
    ["PAUL", "PREM", 11, 15, None],
    # Friday October 20
    ["PAUL", "TUSHAR", 11, 15, None],
    ["JUSTIN", "ANTHONY", 16, 14, None],
    ["GAB", "ANTHONY", 15, 13, None],
    ["JUSTIN", "ANTHONY", 16, 14, None],
    ["PREM", "PAUL", 15, 11, None],
    ["GAB", "PHILLIP", 16, 14, None],
    ["GAB", "ANTHONY", 15, 7, None],
    ["JACK", "GAB", 13, 15, None],
    ["NESMA", "GAB", 13, 15, None],

    # TOURNAMENT GAME
    #   ["PAUL", "TUSHAR", 13, 15, None],

    # Monday October 23
    ["JUSTIN", "GRACEY", 15, 7, None],
    ["PHILLIP", "ANNA", 11, 15, None],
    ["PREM", "ANNA", 15, 3, None],
    ["PREM", "TUSHAR", 15, 5, None],
    ["TUSHAR", "GRACEZ", 15, 3, None],
    ["PAUL", "PHILLIP", 15, 12, None],
    ["GRACEZ", "JACK", 9, 15, None],
    ["GAB", "JACK", 8, 15, None],
    ["GRACEZ", "JUSTIN", 15, 12, None],
    ["GAB", "JUSTIN", 16, 14, None],
    ["PHILLIP", "PAUL", 7, 15, None],
    #   ["JUSTIN", "ANTHONY", , , None],
    ["PREM", "GAB", 15, 0, None],
    ["PREM", "PAUL", 15, 0, None],
    ["JACK", "PHILLIP", 7, 15, None],
    ["PREM", "GRACEY", 15, 1, None],
    ["ANNA", "TUSHAR", 11, 15, None],
    ["ANTHONY", "TUSHAR", 4, 15, None],
    ["PHILLIP", "TUSHAR", 10, 15, None],
    ["TUSHAR", "PHILLIP", 15, 8, None],

    # Tuesday October 24
    ["JACK", "PAUL", 8, 15, None],
    ["PAUL", "ANTHONY", 15, 8, None],
    ["TUSHAR", "GRACEY", 15, 4, None],
    ["PHILLIP", "TUSHAR", 13, 15, None],
    ["PAUL", "ANNA", 16, 14, None],
    ["PREM", "TUSHAR", 10, 15, None],
    ["GAB", "NESMA", 15, 13, None],
    ["GAB", "ANTHONY", 15, 9, None],
    ["PHILLIP", "ANNA", 18, 16, None],
    ["PREM", "ANTHONY", 15, 7, None],
    ["GRACEZ", "CARMEN", 8, 15, None],
    ["PAUL", "PHILLIP", 8, 15, None],
    ["ANTHONY", "JUSTIN", 15, 7, None],
    ["JACK", "GRACEY", 6, 15, None],
    ["TUSHAR", "GRACEZ", 15, 11, None],
    ["PHILLIP", "GRACEY", 12, 15, None],
    ["ANNA", "PAUL", 15, 10, None],
    ["ANTHONY", "ANNA", 0, 15, None],
    ["JUSTIN", "ANTHONY", 15, 13, None],

  # Wednesday October 25
  ["PHILLIP", "PAUL", 11, 15, None],
  ["GAB", "PAUL", 9, 15, None],
  ["JUSTIN", "ANTHONY", 15, 17, None],
  ["JUSTIN", "PREM", 5, 15, None],
  ["GRACEZ", "GAB", 15, 8, None],
  ["GRACEZ", "TUSHAR", 5, 15, None],
  ["ANNA", "PHILLIP", 15, 10, None],
  ["ANNA", "PHILLIP", 15, 9, None],
  ["PREM", "TUSHAR", 15, 10, None],
  ["GAB", "NESMA", 15, 8, None],
  ["JACK", "GAB", 15, 13, None],
  ["ANTHONY", "PAUL", 9, 15, None],
  ["JACK", "PHILLIP", 9, 15, None],
  ["PREM", "PHILLIP", 9, 15, None],
  ["ANTHONY", "GAB", 15, 8, None],
  ["PREM", "PAUL", 10, 15, None],
  ["PREM", "ANNA", 15, 9, None],
  ["GRACEY", "PHILLIP", 15, 11, None],
  # Thursday October 26
  ["GRACEZ", "JACK", 7, 15, None],
  ["PHILLIP", "PAUL", 11, 15, None],
  ["GAB", "TUSHAR", 1, 15, None],
  ["PAUL", "PHILLIP", 13, 15, None],
  ["PREM", "TUSHAR", 11, 15, None],
  ["TUSHAR", "GRACEZ", 15, 7, None],
  ["ANTHONY", "JUSTIN", 15, 12, None],
  ["ANTHONY", "PREM", 6, 15, None],
  ["PHILLIP", "ANNA", 19, 21, None],
  ["ANNA", "PHILLIP", 15, 12, None],
  ["ANTHONY", "GRACEZ", 15, 7, None],
  ["GAB", "CARMEN", 15, 13, None],
  ["ANTHONY", "PAUL", 7, 15, None],
  ["PREM", "PAUL", 15, 8, None],
  ["GRACEY", "GAB", 15, 8, None],
  ["ANNA", "GRACEY", 15, 10, None],
  ["ANNA", "ANTHONY", 15, 9, None],
  ["ANNA", "PREM", 12, 15, None],
  ["TUSHAR", "JUSTIN", 15, 6, None],
  ["JUSTIN", "GAB", 15, 6, None],
  ["ANTHONY", "TUSHAR", 5, 15, None],
#   ["NESMA", "CERI", 15, 5, None],
  ["GAB", "GRACEZ", 5, 15, None],
  # Friday October 27
  ["PAUL", "JACK", 15, 6, None],
  ["TUSHAR", "PHILLIP", 15, 11, None],
  ["ANTHONY", "PREM", 12, 15, None],
  ["GAB", "JACK", 15, 13, None],
  ["GAB", "GRACEZ", 12, 15, None],
  ["ANTHONY", "GAB", 15, 17, None],
  ["PREM", "TUSHAR", 7, 15, None],
  ["GRACEZ", "PHILLIP", 5, 15, None],
  ["JACK", "PHILLIP", 8, 15, None],
  ["JUSTIN", "GAB", 12, 15, None],
  ["ANNA", "PAUL", 17, 15, None],
  ["ANNA", "PHILLIP", 15, 5, None],
  ["GRACEY", "TUSHAR", 2, 15, None],
  ["PHILLIP", "GAB", 15, 13, None],
  ["GAB", "PHILLIP", 11, 15, None],
  ["PAUL", "JUSTIN", 15, 12, None],
  ["ANTHONY", "JUSTIN", 15, 9, None],
  ["ANTHONY", "GRACEY", 20, 18, None],
  # Monday October 30
  ["PAUL", "PHILLIP", 15, 13, None],
  ["JACK", "GAB", 8, 15, None],
  ["ANTHONY", "PREM", 12, 15, None],
  ["JUSTIN", "ANTHONY", 10, 15, None],
  ["PHILLIP", "ANNA", 12, 15, None],
  ["ANNA", "PHILLIP", 15, 5, None],
  # Tuesday October 31
  ["ANTHONY", "TUSHAR", 13, 15, None],
  ["GAB", "PREM", 6, 15, None],
  ["ANTHONY", "PREM", 5, 15, None],
  ["ANNA", "PHILLIP", 15, 13, None],
  ["PHILLIP", "ANNA", 10, 15, None],
  ["PHILLIP", "PAUL", 10, 15, None],
  ["TUSHAR", "PREM", 9, 15, None],
  ["PAUL", "PHILLIP", 15, 12, None],
  ["ANTHONY", "TUSHAR", 7, 15, None],
  ["GAB", "PAUL", 7, 15, None],
  ["GAB", "PHILLIP", 6, 15, None],
  ["GAB", "ANTHONY", 5, 15, None],
  ["PHILLIP", "ANNA", 9, 15, None],
  ["ANNA", "PHILLIP", 15, 13, None],
  ["JUSTIN", "ANTHONY", 17, 19, None],
  ["GAB", "GRACEZ", 19, 17, None],
  # Wednesday November 1
  ["ANTHONY", "JUSTIN", 15, 12, None],
  ["PHILLIP", "GAB", 15, 12, None],
  ["GAB", "ANTHONY", 15, 13, None],
  ["GAB", "GRACEZ", 1, 15, None],
  ["PHILLIP", "GRACEZ", 15, 9, None],
  ["GAB", "ANTHONY", 8, 15, None],
  ["PAUL", "ANTHONY", 15, 12, None],
  ["ANNA", "PHILLIP", 15, 4, None],
  ["PHILLIP", "ANNA", 16, 14, None],
  ["PREM", "ANNA", 15, 17, None],
  ["JUSTIN", "TUSHAR", 13, 15, None],
  ["PAUL", "TUSHAR", 14, 16, None],
  ["ANNA", "PAUL", 15, 10, None],
  ["PHILLIP", "TUSHAR", 10, 15, None],
  ["ANNA", "TUSHAR", 15, 7, None],
  ["JUSTIN", "GAB", 15, 7, None],
  # Thursday November 2
  ["JACK", "PAUL", 5, 15, None],
  ["GRACEZ", "GAB", 16, 14, None],
  ["PAUL", "PHILLIP", 15, 11, None],
  ["PHILLIP", "PAUL", 15, 13, None],
  ["PREM", "PHILLIP", 15, 9, None],
  ["JUSTIN", "ANTHONY", 15, 13, None],
  ["GAB", "JACK", 13, 15, None],
  ["GAB", "ANNA", 15, 8, None],
  ["PAUL", "PHILLIP", 12, 15, None],
  ["TUSHAR", "ANTHONY", 16, 14, None],
  ["TUSHAR", "GAB", 15, 10, None],
  ["PREM", "TUSHAR", 15, 11, None],
  ["TUSHAR", "PREM", 15, 13, None],
  ["PAUL", "GAB", 15, 4, None],
  ["PHILLIP", "ANNA", 9, 15, None],
  ["ANNA", "PHILLIP", 5, 15, None],
  ["PHILLIP", "ANNA", 6, 15, None],
  ["GRACEZ", "JACK", 15, 10, None],
  ["TUSHAR", "JUSTIN", 15, 10, None],
  ["ANTHONY", "PAUL", 14, 16, None],
  ["ANTHONY", "GAB", 15, 13, None],
  ["ANTHONY", "JACK", 15, 7, None],
  # Friday November 3
  ["JUSTIN", "ANTHONY", 6, 15, None],
  ["PAUL", "PHILLIP", 15, 11, None],
  ["PHILLIP", "PAUL", 12, 15, None],
  ["PAUL", "ANNA", 10, 15, None],
  ["TUSHAR", "ANTHONY", 15, 8, None],
  ["ANTHONY", "GAB", 13, 15, None],
  ["GAB", "ANTHONY", 13, 15, None],
  ["PHILLIP", "PAUL", 14, 16, None],
  ["PHILLIP", "ANNA", 10, 15, None],
  ["PHILLIP", "ANNA", 10, 15, None],
  ["PREM", "ANTHONY", 15, 3, None],
  ["PREM", "GAB", 15, 5, None],
  ["PREM", "TUSHAR", 15, 11, None],
  ["PAUL", "PREM", 12, 15, None],
  ["PHILLIP", "GAB", 15, 12, None],
  ["GAB", "PHILLIP", 11, 15, None],
  ["ANTHONY", "TUSHAR", 10, 15, None],
  ["PHILLIP", "GRACEZ", 10, 15, None],
  ["GRACEZ", "PHILLIP", 7, 15, None],
  ["PHILLIP", "PREM", 15, 9, None],
  ["GAB", "JUSTIN", 11, 15, None],
  # Monday November 6
  ["PHILLIP", "PAUL", 15, 11, None],
  ["PAUL", "PHILLIP", 15, 8, None],
#   ["GAB", "JACK", , , None],
  ["JUSTIN", "ANTHONY", 15, 13, None],
  ["PREM", "ANTHONY", 15, 7, None],
  ["ANTHONY", "TUSHAR", 6, 15, None],
  ["JUSTIN", "TUSHAR", 7, 15, None],
  ["TUSHAR", "PREM", 11, 15, None],
  ["PREM", "TUSHAR", 15, 13, None],
  ["PHILLIP", "TUSHAR", 16, 18, None],
  ["PREM", "GAB", 15, 5, None],
  ["GAB", "PREM", 9, 15, None],
  ["JUSTIN", "ANTHONY", 18, 16, None],
  ["PHILLIP", "PAUL", 12, 15, None],
  ["PAUL", "PHILLIP", 15, 9, None],
  ["TUSHAR", "ANTHONY", 15, 13, None],
  ["GAB", "ANTHONY", 12, 15, None],
  ["ANTHONY", "GAB", 15, 13, None],
  ["ANNA", "PHILLIP", 2, 15, None],
  ["PHILLIP", "ANNA", 12, 15, None],
  ["ANNA", "PHILLIP", 15, 10, None],
  # Tuesday November 7
  ["GAB", "GRACEZ", 7, 15, None],
  ["ANTHONY", "GAB", 15, 6, None],
  ["JUSTIN", "ANTHONY", 7, 15, None],
  ["PREM", "JUSTIN", 15, 3, None],
  ["GRACEY", "TUSHAR", 15, 15, None],
  ["ANNA", "PREM", 16, 14, None],
  ["JUSTIN", "GAB", 15, 12, None],
  ["TUSHAR", "GAB", 15, 4, None],
  ["PAUL", "JUSTIN", 12, 15, None],
  ["GRACEY", "GRACEZ", 13, 15, None],
  ["JACK", "GAB", 12, 15, None],
  ["GAB", "JACK", 15, 6, None],
  ["PREM", "PHILLIP", 15, 3, None],
  ["GRACEZ", "PHILLIP", 6, 15, None],
  ["GAB", "ANTHONY", 15, 12, None],
  ["ANTHONY", "GAB", 13, 12, None],
  # Wednesday November 8
  ["JUSTIN", "ANTHONY", 14, 16, None],
  ["TUSHAR", "ANNA", 15, 3, None],
  ["JUSTIN", "PHILLIP", 15, 9, None],
  ["GAB", "GRACEZ", 11, 15, None],
  ["GRACEZ", "PREM", 4, 15, None],
  ["GRACEZ", "JACK", 15, 7, None],
  ["JACK", "GAB", 13, 15, None],
  ["ANTHONY", "PAUL", 15, 11, None],
  ["ANTHONY", "ANNA", 11, 15, None],
  ["PAUL", "PHILLIP", 15, 12, None],
  ["PAUL", "ANNA", 15, 11, None],
  ["PREM", "PAUL", 15, 9, None],
  ["ANTHONY", "JUSTIN", 15, 9, None],
  ["JUSTIN", "JACK", 15, 8, None],
  # Thursday November 9
  ["JUSTIN", "PREM", 12, 15, None],
  ["PAUL", "PHILLIP", 9, 15, None],
  ["PHILLIP", "PAUL", 11, 15, None],
  ["JUSTIN", "ANTHONY", 15, 17, None],
  ["PREM", "ANTHONY", 15, 4, None],
  ["PREM", "GRACEY", 15, 5, None],
  ["GRACEZ", "CARMEN", 9, 15, None],
  ["GAB", "JACK", 10, 15, None],
  ["PHILLIP", "PAUL", 11, 15, None],
  ["GAB", "PAUL", 8, 15, None],
  ["ANTHONY", "PAUL", 13, 15, None],
  ["GRACEZ", "ANTHONY", 10, 15, None],
  ["ANTHONY", "PHILLIP", 13, 15, None],
  ["PREM", "PHILLIP", 15, 7, None],
  ["TUSHAR", "PREM", 15, 13, None],
  ["GAB", "GRACEY", 15, 13, None],
  ["GRACEZ", "GAB", 7, 15, None],
  ["ANTHONY", "GAB", 15, 3, None],
  # Friday November 10
  ["JUSTIN", "ANTHONY", 15, 13, None],
  ["PHILLIP", "TUSHAR", 7, 15, None],
  ["JACK", "GAB", 10, 15, None],
  ["GAB", "PAUL", 9, 15, None],
  ["TUSHAR", "PAUL", 15, 7, None],
  ["JACK", "PHILLIP", 7, 15, None],
  ["PREM", "PHILLIP", 16, 14, None],
  ["PREM", "ANNA", 15, 6, None],
  ["TUSHAR", "PREM", 14, 16, None],
  ["PREM", "ANTHONY", 15, 4, None],
  ["ANTHONY", "TUSHAR", 15, 17, None],
  ["PAUL", "PHILLIP", 11, 15, None],
  ["ANTHONY", "PHILLIP", 7, 15, None],
#   ["ANTHONY", "GAB", 7, 15, None],
  # Monday November 13
  ["ANTHONY", "TUSHAR", 14, 16, None],
  ["JUSTIN", "TUSHAR", 14, 16, None],
  ["PHILLIP", "PAUL", 11, 15, None],
  ["PAUL", "PHILLIP", 13, 15, None],
  ["GRACEZ", "JACK", 10, 15, None],
  ["PREM", "ANTHONY", 15, 10, None],
  ["PHILLIP", "GRACEY", 18, 16, None],
  ["GRACEY", "PHILLIP", 7, 15, None],
  ["GRACEZ", "GAB", 15, 13, None],
  ["JUSTIN", "ANTHONY", 15, 13, None],
  ["ANTHONY", "PREM", 3, 15, None],
  ["PHILLIP", "PAUL", 16, 14, None],
  ["PHILLIP", "ANNA", 15, 12, None],
  ["GAB", "JACK", 5, 15, None],
  ["JUSTIN", "TUSHAR", 13, 15, None],
  ["TUSHAR", "ANTHONY", 15, 11, None],
  # Tuesday November 14
  ["JUSTIN", "ANTHONY", 13, 15, None],
  ["TUSHAR", "PREM", 15, 7, None],
  ["PAUL", "PHILLIP", 12, 15, None],
  ["JACK", "GRACEZ", 15, 8, None],
  ["GRACEZ", "JACK", 15, 13, None],
#   ["TUSHAR", "GRACEY", 15, 13, None],
#   ["JUSTIN", "TUSHAR", 12, 15, None],
#   ["ANNA", "GRACEY", 15, 13, None],
#   ["TUSHAR", "GRACEY", 15, 13, None],
  ["PAUL", "PHILLIP", 15, 11, None],
  ["PAUL", "GRACEZ", 15, 5, None],
  ["GRACEZ", "JACK", 15, 11, None],
  ["GAB", "ANTHONY", 9, 15, None],
  ["ANNA", "PAUL", 10, 15, None],
  ["JUSTIN", "GRACEZ", 10, 15, None],
  ["JACK", "GAB", 11, 15, None],
  ["GAB", "GRACEZ", 13, 15, None],
  # Wednesday November 15
  ["GRACEZ", "GRACEY", 6, 15, None],
  ["GRACEZ", "GAB", 9, 15, None],
  ["JUSTIN", "ANTHONY", 15, 11, None],
  ["JUSTIN", "PAUL", 15, 12, None],
  ["ANTHONY", "GAB", 12, 15, None],
  ["GAB", "ANTHONY", 15, 12, None],
  ["ANNA", "JUSTIN", 15, 6, None],
  ["JUSTIN", "ANTHONY", 15, 17, None],
  ["PAUL", "ANTHONY", 15, 11, None],
  ["JACK", "GRACEZ", 9, 15, None],
  # Thursday November 16
  ["JUSTIN", "ANTHONY", 11, 15, None],
  ["JUSTIN", "GRACEY", 15, 12, None],
  ["PREM", "ANTHONY", 15, 3, None],
  ["GAB", "GRACEZ", 13, 15, None],
  ["JUSTIN", "ANTHONY", 10, 15, None],
  ["PREM", "ANTHONY", 15, 5, None],
  ["PAUL", "JACK", 15, 11, None],
  ["PAUL", "PHILLIP", 11, 15, None],
  ["PREM", "GRACEZ", 15, 3, None],
  ["PAUL", "PREM", 7, 15, None],
  ["GRACEZ", "TUSHAR", 11, 15, None],
  ["GAB", "ANTHONY", 14, 16, None],
  ["ANTHONY", "PREM", 5, 15, None],
  ["ANTHONY", "PREM", 6, 15, None],
  # Friday November 17
  ["ANTHONY", "GAB", 15, 11, None],
  ["PREM", "ANTHONY", 15, 7, None],
  ["ANTHONY", "JUSTIN", 17, 15, None],
  ["JUSTIN", "ANTHONY", 13, 15, None],
#   ["TUSHAR", "ANTHONY", 15, 15, None],
  ["ANTHONY", "TUSHAR", 13, 15, None],
  ["PAUL", "JUSTIN", 15, 12, None],
  ["PAUL", "PREM", 13, 15, None],
#   ["PREM", "TUSHAR", 15, 15, None],
  ["GRACEZ", "GAB", 10, 15, None],
  ["GRACEZ", "JACK", 15, 8, None],
  ["GAB", "JACK", 14, 16, None],
  ["PHILLIP", "ANNA", 15, 10, None],
  ["ANNA", "PHILLIP", 15, 8, None],
  ["PHILLIP", "ANNA", 15, 13, None],
  # Monday November 20
  ["GRACEZ", "JACK", 13, 15, None],
  ["JUSTIN", "ANTHONY", 11, 15, None],
  ["PAUL", "ANTHONY", 18, 16, None],
  ["ANTHONY", "TUSHAR", 8, 15, None],
  ["GRACEZ", "GRACEY", 15, 7, None],
  ["GRACEZ", "TUSHAR", 8, 15, None],
  # Tuesday November 21
  ["PAUL", "JUSTIN", 15, 7, None],
  ["ANTHONY", "TUSHAR", 11, 15, None],
  ["JUSTIN", "GRACEY", 15, 10, None],
  ["JUSTIN", "GAB", 15, 7, None],
  ["JACK", "GAB", 15, 13, None],
  ["JUSTIN", "TUSHAR", 9, 15, None],
  ["GAB", "TUSHAR", 9, 15, None],
  ["PREM", "GRACEY", 15, 7, None],
  ["JACK", "PAUL", 15, 13, None],
  ["GRACEZ", "PAUL", 13, 15, None],
  ["GRACEZ", "GAB", 15, 10, None],
  ["PREM", "PAUL", 15, 6, None],
  ["PREM", "ANNA", 12, 15, None],
  ["ANTHONY", "GRACEZ", 15, 5, None],
  ["ANTHONY", "PREM", 10, 15, None],
  ["GAB", "GRACEZ", 12, 15, None],
  ["GRACEZ", "GAB", 15, 13, None],
  # Wednesday November 22
  ["GRACEZ", "PREM", 5, 15, None],
  ["ANTHONY", "GAB", 15, 7, None],
  ["PREM", "JUSTIN", 15, 7, None],
  ["GAB", "ANTHONY", 5, 15, None],
  ["JACK", "GAB", 12, 15, None],
  ["GAB", "JACK", 13, 15, None],
  ["GRACEZ", "PAUL", 13, 15, None],
  ["ANTHONY", "GAB", 15, 8, None],
  ["ANTHONY", "PAUL", 13, 15, None],
  ["ANTHONY", "JACK", 15, 7, None],
  ["PREM", "ANTHONY", 15, 11, None],
  ["PREM", "ANNA", 10, 15, None],
  # Thursday November 23
  ["PAUL", "JACK", 15, 9, None],
  ["PAUL", "GAB", 15, 3, None],
  ["PREM", "TUSHAR", 15, 11, None],
  ["GRACEZ", "GAB", 8, 15, None],
  ["TUSHAR", "GAB", 15, 13, None],
  ["ANTHONY", "JUSTIN", 15, 13, None],
  ["ANTHONY", "GAB", 15, 11, None],
  ["ANTHONY", "PAUL", 11, 15, None],
  ["GRACEY", "TUSHAR", 15, 13, None],
  ["GAB", "PREM", 2, 15, None],
  ["GAB", "PREM", 4, 15, None],
  ["PAUL", "PREM", 11, 15, None],
  ["ANNA", "PREM", 10, 15, None],
  ["GRACEZ", "JACK", 12, 15, None],
#   ["GAB", "JACK", 12, 15, None],
  ["ANTHONY", "TUSHAR", 18, 20, None],
  ["PREM", "JUSTIN", 15, 7, None],
  ["PREM", "ANTHONY", 15, 3, None],
  ["ANTHONY", "TUSHAR", 12, 15, None],
  ["PAUL", "TUSHAR", 11, 15, None],
  ["PREM", "ANTHONY", 15, 3, None],
  # Monday November 27
  ["GAB", "PAUL", 12, 15, None],
  ["GRACEZ", "PAUL", 17, 19, None],
  ["ANTHONY", "TUSHAR", 16, 18, None],
  ["ANTHONY", "PREM", 7, 15, None],
  ["GAB", "ANTHONY", 13, 15, None],
  ["TUSHAR", "ANTHONY", 15, 12, None],
  ["GAB", "GRACEZ", 17, 15, None],
  # Tuesday November 28
  ["PAUL", "JACK", 15, 12, None],
  ["JUSTIN", "ANTHONY", 13, 15, None],
  ["PREM", "GRACEY", 15, 0, None],
  ["ANNA", "GRACEY", 15, 13, None],
  ["GAB", "PAUL", 12, 15, None],
  ["JUSTIN", "PAUL", 15, 11, None],
  ["GRACEZ", "JACK", 10, 15, None],
  ["GRACEZ", "PREM", 3, 15, None],
  ["ANTHONY", "GAB", 15, 12, None],
  ["GAB", "ANTHONY", 9, 15, None],
  ["TUSHAR", "ANTHONY", 15, 12, None],
  ["PREM", "ANTHONY", 15, 8, None],
  ["JUSTIN", "ANTHONY", 15, 13, None],
  # Wednesday November 29
  ["TUSHAR", "ANTHONY", 15, 12, None],
  ["PHILLIP", "PAUL", 15, 17, None],
  ["JUSTIN", "ANTHONY", 15, 13, None],
  ["GRACEY", "CERI", 15, 5, None],
  ["JUSTIN", "PREM", 7, 15, None],
  ["GRACEY", "PREM", 3, 15, None],
  ["ANNA", "PREM", 15, 11, None],
  ["ANTHONY", "PAUL", 13, 15, None],
  ["PAUL", "GRACEZ", 15, 6, None],
  ["JUSTIN", "ANTHONY", 15, 11, None],
  ["GAB", "GRACEZ", 15, 12, None],
  ["PAUL", "JACK", 15, 6, None],
  ["GRACEY", "JUSTIN", 13, 15, None],
  ["GAB", "JACK", 12, 15, None],
  ["GAB", "JUSTIN", 12, 15, None],
  ["TUSHAR", "ANNA", 15, 8, None],
  # Thursday November 30
  ["GAB", "JUSTIN", 15, 17, None],
  ["PAUL", "JUSTIN", 14, 16, None],
  ["PREM", "TUSHAR", 15, 7, None],
  ["GAB", "PAUL", 12, 15, None],
  ["PREM", "PAUL", 15, 17, None],
  ["PAUL", "ANNA", 15, 13, None],
  ["JUSTIN", "JACK", 15, 11, None],
  ["ANTHONY", "GAB", 17, 15, None],
  ["GAB", "ANTHONY", 13, 15, None],
#   ["JUSTIN", "ANTHONY", 13, 15, None],
#   ["TUSHAR", "ANTHONY", 13, 15, None],
#   ["TUSHAR", "GRACEY", 13, 15, None],
  ["PREM", "ANTHONY", 15, 9, None],
  ["TUSHAR", "ANTHONY", 13, 15, None],
  ["PAUL", "ANTHONY", 15, 13, None],
  ["PAUL", "ANNA", 13, 15, None],
  # Friday December 1
  ["ANTHONY", "JUSTIN", 15, 1, None],
  ["PHILLIP", "GRACEZ", 15, 18, None],
  ["GRACEZ", "PHILLIP", 15, 12, None],
  ["GAB", "PHILLIP", 15, 11, None],
  ["GAB", "GRACEY", 13, 15, None],
  ["GAB", "JACK", 16, 14, None],
  ["GAB", "ANTHONY", 18, 16, None],
  ["WILSON", "PREM", 3, 15, None],
  ["PREM", "WILSON", 15, 1, None],
  ["PHILLIP", "ANNA", 20, 18, None],
  ["ANNA", "PHILLIP", 13, 15, None],
  ["PHILLIP", "ANNA", 14, 16, None],
  ["GRACEZ", "TUSHAR", 13, 15, None],
#   # Monday December 4
  ["ANTHONY", "JUSTIN", 15, 13, None],
  ["PHILLIP", "JEREMY", 15, 13, None],
  ["GAB", "ANTHONY", 11, 15, None],
  ["PHILLIP", "JEREMY", 9, 15, None],
  ["PAUL", "JEREMY", 15, 10, None],
  ["ANNA", "JEREMY", 13, 15, None],
  ["PREM", "JEREMY", 13, 15, None],
  ["ANTHONY", "TUSHAR", 13, 15, None],
  ["JUSTIN", "ANTHONY", 15, 13, None],
  ["PREM", "TUSHAR", 14, 16, None],
  ["GRACEZ", "JUSTIN", 13, 15, None],
  ["PHILLIP", "PAUL", 11, 15, None],
  ["PHILLIP", "GAB", 15, 6, None],
  ["PHILLIP", "PREM", 10, 15, None],
  ["JEREMY", "ANNA", 15, 10, None],
  ["ANTHONY", "TUSHAR", 11, 15, None],
  ["ANTHONY", "JUSTIN", 11, 15, None],
  ["ANTHONY", "GAB", 15, 8, None],
  ["GAB", "ANTHONY", 15, 7, None],
  ["GRACEZ", "JACK", 15, 7, None],
  ["PHILLIP", "ANNA", 15, 13, None],
  ["PHILLIP", "JEREMY", 11, 15, None],
#   # Tuesday December 5
  ["JUSTIN", "ANTHONY", 6, 15, None],
  ["PHILLIP", "JEREMY", 15, 13, None],
  ["PAUL", "GAB", 15, 10, None],
  ["ANTHONY", "GAB", 15, 10, None],
  ["ANNA", "JEREMY", 15, 13, None],
  ["GRACEY", "TUSHAR", 9, 15, None],
  ["GRACEY", "PREM", 3, 15, None],
  ["PREM", "JEREMY", 15, 12, None],
  ["PAUL", "ANNA", 16, 14, None],
  ["JEREMY", "GAB", 15, 6, None],
  ["JEREMY", "GAB", 15, 9, None],
  ["JUSTIN", "TUSHAR", 7, 15, None],
  ["PAUL", "JEREMY", 7, 15, None],
  ["PHILLIP", "JEREMY", 13, 15, None],
  ["TUSHAR", "JEREMY", 15, 12, None],
  ["PAUL", "JUSTIN", 15, 10, None],
  ["GRACEZ", "JACK", 11, 15, None],
  ["GRACEZ", "PAUL", 5, 15, None],
  ["GRACEZ", "TUSHAR", 10, 15, None],
  ["GRACEY", "GRACEZ", 14, 16, None],
  ["JEREMY", "ANNA", 15, 12, None],
  ["ANNA", "JEREMY", 15, 12, None],
  ["ANTHONY", "JUSTIN", 15, 7, None],
#   # Wednesday December 6
  ["GRACEZ", "PHILLIP", 15, 7, None],
  ["PHILLIP", "GRACEZ", 15, 4, None],
  ["GRACEY", "GAB", 13, 15, None],
  ["GRACEZ", "GAB", 7, 15, None],
  ["PHILLIP", "PREM", 6, 15, None],
  ["WILSON", "GAB", 7, 15, None],
  ["JEREMY", "ANNA", 12, 15, None],
  ["JEREMY", "ANNA", 11, 15, None],
  ["TUSHAR", "ANTHONY", 10, 15, None],
  ["ANTHONY", "PREM", 6, 15, None],
  ["PREM", "TUSHAR", 15, 9, None],
  ["ANTHONY", "GAB", 13, 15, None],
  ["GAB", "JUSTIN", 9, 15, None],
  ["PAUL", "JUSTIN", 15, 9, None],
  ["PAUL", "GAB", 15, 9, None],
  ["ANTHONY", "PAUL", 16, 14, None],
  ["PHILLIP", "ANNA", 10, 15, None],
  ["JUSTIN", "ANTHONY", 10, 15, None],
  ["JUSTIN", "GRACEZ", 15, 11, None],
  ["JUSTIN", "PREM", 14, 16, None],
  ["JUSTIN", "TUSHAR", 15, 11, None],
  ["ANTHONY", "ANNA", 9, 15, None],
  ["GRACEY", "PHILLIP", 15, 13, None],
  ["GRACEZ", "GAB", 15, 12, None],
  ["TUSHAR", "ANNA", 15, 7, None],
#   # Thursday December 7
  ["JEREMY", "PHILLIP", 15, 4, None],
  ["JEREMY", "ANNA", 15, 7, None],
  ["ANNA", "JEREMY", 9, 15, None],
  ["PAUL", "JACK", 16, 14, None],
  ["PREM", "JUSTIN", 15, 9, None],
  ["GAB", "GRACEZ", 15, 9, None],
  ["TUSHAR", "PHILLIP", 15, 11, None],
  ["PHILLIP", "GRACEY", 15, 9, None],
  ["GRACEZ", "GAB", 10, 15, None],
  ["JEREMY", "PAUL", 15, 12, None],
  ["PAUL", "ANNA", 15, 11, None],
  ["ANTHONY", "GAB", 15, 7, None],
  ["ANTHONY", "GRACEY", 15, 13, None],
  ["GRACEZ", "GRACEY", 15, 4, None],
  ["JEREMY", "PREM", 15, 13, None],
#   # Friday December 8
  ["GRACEY", "GAB", 15, 9, None],
  ["PREM", "JUSTIN", 15, 13, None],
  ["ANNA", "JEREMY", 9, 15, None],
  ["TUSHAR", "JUSTIN", 15, 0, None],
  ["PAUL", "PREM", 15, 13, None],
  ["JEREMY", "PAUL", 15, 9, None],
  ["GRACEZ", "JUSTIN", 15, 13, None],
  ["ANTHONY", "PHILLIP", 10, 15, None],
  ["GAB", "JACK", 15, 9, None],
  ["JACK", "GRACEZ", 15, 13, None],
  ["PHILLIP", "PAUL", 12, 15, None],
  ["TUSHAR", "ANTHONY", 15, 1, None],
  ["ANNA", "GRACEY", 17, 15, None],
  ["JEREMY", "ANNA", 15, 11, None],
  ["GRACEY", "PREM", 6, 15, None],
  ["ANNA", "JEREMY", 15, 13, None],
  ["JEREMY", "PHILLIP", 9, 15, None],
  ["PHILLIP", "JEREMY", 20, 18, None],
  ["ANNA", "JEREMY", 7, 15, None],
  ["WILSON", "GAB", 8, 15, None],
  ["WILSON", "GAB", 10, 15, None],
  ["PREM", "JEREMY", 11, 15, None],
#   # Monday December 11
  ["JACK", "GAB", 14, 16, None],
  ["JEREMY", "TUSHAR", 4, 15, None],
  ["JEREMY", "PHILLIP", 13, 15, None],
  ["JUSTIN", "ANTHONY", 15, 17, None],
  ["GRACEZ", "GRACEY", 7, 15, None],
  ["GAB", "WILSON", 15, 5, None],
  ["PHILLIP", "JEREMY", 14, 16, None],
  ["GRACEZ", "GAB", 7, 15, None],
  ["JEREMY", "PHILLIP", 11, 15, None],
  ["ANTHONY", "GAB", 12, 15, None],
  ["PAUL", "ANNA", 16, 14, None],
  ["WILSON", "GRACEZ", 13, 15, None],
  ["WILSON", "GAB", 13, 15, None],
  ["PHILLIP", "PAUL", 15, 11, None],
  ["GRACEZ", "JACK", 11, 15, None],
  ["GRACEZ", "JUSTIN", 15, 11, None],
  ["TUSHAR", "BOGDAN", 15, 6, None],
  ["BOGDAN", "TUSHAR", 4, 15, None],
  ["GAB", "GRACEY", 9, 15, None],
#   # Tuesday December 12
  ["PHILLIP", "ANNA", 16, 14, None],
  ["PHILLIP", "JEREMY", 6, 15, None],
  ["GRACEZ", "GAB", 15, 17, None],
  ["ANTHONY", "PREM", 5, 15, None],
  ["JEREMY", "PHILLIP", 11, 15, None],
  ["PHILLIP", "JEREMY", 10, 15, None],
  ["GAB", "JACK", 15, 4, None],
  ["JUSTIN", "ANTHONY", 12, 15, None],
  ["ANTHONY", "TUSHAR", 7, 15, None],
  ["JEREMY", "ANNA", 15, 4, None],
  ["ANNA", "JEREMY", 10, 15, None],
  ["GAB", "WILSON", 15, 4, None],
  ["GAB", "ANTHONY", 15, 13, None],
  ["GAB", "ANNA", 5, 15, None],
  ["JACK", "PAUL", 9, 15, None],
  ["PAUL", "JUSTIN", 18, 16, None],
  ["PHILLIP", "PAUL", 15, 13, None],
  ["ANTHONY", "GAB", 15, 13, None],
  ["JEREMY", "PHILLIP", 15, 11, None],
  ["PHILLIP", "JEREMY", 19, 21, None],
  ["ANNA", "JEREMY", 6, 15, None],
  ["JEREMY", "PAUL", 12, 15, None],
#   # Wednesday December 13
  ["JEREMY", "TUSHAR", 13, 15, None],
  ["JEREMY", "PHILLIP", 9, 15, None],
  ["PHILLIP", "JEREMY", 8, 15, None],
  ["JEREMY", "PHILLIP", 15, 10, None],
  ["PREM", "TUSHAR", 6, 15, None],
  ["GRACEZ", "JACK", 15, 11, None],
  ["PAUL", "PHILLIP", 15, 6, None],
  ["JEREMY", "PAUL", 15, 6, None],
  ["JUSTIN", "TUSHAR", 14, 16, None],
  ["JEREMY", "PHILLIP", 13, 15],
  ["PHILLIP", "JEREMY", 13, 15],
  ["JEREMY", "PHILLIP", 15, 12],
  ["GRACEZ", "JACK", 17, 15, None],
  ["GRACEZ", "PHILLIP", 7, 15, None],
  ["GRACEZ", "JEREMY", 12, 15, None],
  ["JUSTIN", "ANTHONY", 9, 15, None],
  ["GAB", "GRACEZ", 15, 5, None],
  ["JACK", "GAB", 6, 15, None],
  ["GAB", "TUSHAR", 12, 15, None],
  ["WILSON", "GAB", 4, 15, None],
  ["GAB", "ANTHONY", 13, 15, None],
  ["ANTHONY", "GAB", 16, 18, None],
  ["TUSHAR", "ANTHONY", 15, 12, None],
  # Thursday December 13
  ["JEREMY", "PHILLIP", 15, 10, None],
  ["GRACEZ", "WILSON", 15, 6, None],
  ["JEREMY", "PHILLIP", 15, 10, None],
  ["JEREMY", "ANNA", 12, 15, None],
  ["GAB", "WILSON", 15, 7, None],
  ["GRACEZ", "GAB", 10, 15, None],
  ["GAB", "ANTHONY", 15, 12, None],
  ["GAB", "JACK", 15, 7, None],
  ["JEREMY", "PAUL", 6, 15, None],
  ["PAUL", "JEREMY", 15, 10, None],
  ["PAUL", "TUSHAR", 10, 15, None],
  ["GRACEZ", "JACK", 15, 12, None],
  ["GRACEY", "PHILLIP", 16, 14, None],
  ["PHILLIP", "GRACEY", 16, 14, None],
  ["PHILLIP", "ANNA", 15, 10, None],
  ["JACK", "PAUL", 14, 16, None],
  ["PREM", "JEREMY", 15, 12, None],
  ["JEREMY", "PREM", 9, 15, None],
  ["JEREMY", "ANNA", 15, 9, None],
  ["ANNA", "JEREMY", 15, 13, None],
  ["PHILLIP", "TUSHAR", 15, 11, None],
  ["BOGDAN", "TUSHAR", 7, 11, None],
  ["ANTHONY", "TUSHAR", 10, 15, None],
  ["PREM", "ANTHONY", 15, 5, None],
  ["JEREMY", "TUSHAR", 15, 11, None],
  # Friday December 14
  ["JEREMY", "ANTHONY", 15, 12, None],
  ["GAB", "GRACEY", 9, 15, None],
  ["TUSHAR", "JUSTIN", 15, 12, None],
  ["WILSON", "GAB", 13, 15, None],
  ["WILSON", "GAB", 10, 15, None],
  ["ANTHONY", "WILSON", 15, 4, None],
  ["JACK", "GRACEZ", 16, 14, None],
  ["GAB", "ANTHONY", 13, 15, None],
  ["GAB", "ANTHONY", 20, 22, None],
  ["TUSHAR", "JACK", 15, 11, None],
  ["GRACEZ", "GAB", 14, 16, None],
  ["GAB", "GRACEY", 15, 7, None],
  ["GAB", "JACK", 8, 15, None],
  ["GRACEY", "GRACEZ", 12, 15, None],
  ["GRACEZ", "GRACEY", 15, 8, None],
  ["GAB", "ANTHONY", 14, 16, None],
  ["ANTHONY", "GAB", 13, 15, None],
  ["GAB", "WILSON", 15, 8, None],
  ["WILSON", "GAB", 14, 16, None],
  # Monday December 18
  ["PAUL", "PHILLIP", 15, 11, None],
  ["PREM", "PHILLIP", 10, 15, None],
  ["ANNA", "PHILLIP", 10, 15, None],
  ["JUSTIN", "TUSHAR", 14, 16, None],
  ["JUSTIN", "ANTHONY", 14, 16, None],
  ["PAUL", "ANTHONY", 15, 13, None],
  ["GRACEY", "TUSHAR", 5, 15, None],
  ["GRACEY", "PREM", 9, 15, None],
  ["ANNA", "GRACEY", 15, 11, None],
  ["ANNA", "PHILLIP", 15, 11, None],
  ["PHILLIP", "ANNA", 15, 13, None],
  ["ANNA", "PHILLIP", 15, 9, None],
  ["GRACEY", "GAB", 15, 11, None],
  ["PAUL", "JACK", 15, 11, None],
  ["GRACEZ", "JACK", 15, 11, None],
  ["PREM", "TUSHAR", 15, 11, None],
  ["PREM", "GRACEY", 20, 18, None],
  ["TUSHAR", "GRACEY", 15, 8, None],
  ["GRACEZ", "GRACEY", 8, 15, None],
  ["GAB", "ANTHONY", 15, 8, None],
  ["ANTHONY", "GAB", 4, 15, None],
  ["PREM", "GAB", 14, 16, None],
  # Wednesday December 20
  ["JUSTIN", "TUSHAR", 15, 17, None],
  ["WILSON", "GAB", 15, 8, None],
  ["GRACEZ", "GRACEY", 10, 15, None],
  ["GRACEY", "TUSHAR", 10, 15, None],
  ["GAB", "GRACEY", 15, 13, None],
  ["JUSTIN", "TUSHAR", 15, 13, None],
  ["PHILLIP", "ANTHONY", 16, 14, None],
  ["PAUL", "ANTHONY", 15, 17, None],
  ["ANTHONY", "PAUL", 11, 15, None],

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
    "JEREMY": [1500],
    "ANTHONY": [1500],
    "CERI": [1500],
    "WILSON": [1500]
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
    pickradius = 5
    map_legend_to_ax = {}
    map_legend_to_text = {}
    fig, ax = plt.subplots()

    plt.subplots_adjust(bottom=0.05, top=0.95, right=0.95, left=0.05)
    all_lines = []
    all_texts = []
    for key, value in regular_match_rankings_array.items():
        # exclude people who don't play often to avoid clutter
        if key not in ["MAX", "SHUOTONG", "BOGDAN", "CHRISTIAN", "JESSIE", "SAMSON", "HAYWAD", "NESMA", "CARMEN"]:
            start_index = next((i for i, v in enumerate(value) if v != value[0]), len(value))
            modified_value = value
            if start_index > 10:
                start_index = start_index - 3
                modified_value = [None] * start_index + list(value[start_index:])

            line,  = ax.plot(range(len(regular_match_array) + 1), modified_value, color=color_dict[key], label=key)
            all_lines.append(line)
            for index, element in enumerate(value):
                if index == len(regular_match_array):
                    text = ax.text(index + 0.3, element - 1.5, f"{key}\n({element.round()})", color=color_dict[key])
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

head_to_head = {}
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

if __name__ == '__main__':
    # plot_tournament_results()

    # plot_most_common_matchups_bar()

    # plot_most_common_matchup_pie()

    plot_regular_match_results()