import numpy as np


def create_board():
    board = np.zeros((40, 40))

    probabilities = [
        0.0278,
        0.0556,
        0.0833,
        0.1111,
        0.1389,
        0.1667,
        0.1389,
        0.1111,
        0.0833,
        0.0556,
        0.0278,
    ]

    monopoly_squares = [
        "Go",
        "Mediterranean Avenue",
        "Community Chest (near Mediterranean Avenue)",
        "Baltic Avenue",
        "Income Tax",
        "Reading Railroad",
        "Oriental Avenue",
        "Chance (near Oriental Avenue)",
        "Vermont Avenue",
        "Connecticut Avenue",
        "Jail / Just Visiting",
        "St. Charles Place",
        "Electric Company",
        "States Avenue",
        "Virginia Avenue",
        "Pennsylvania Railroad",
        "St. James Place",
        "Community Chest (near St. James Place)",
        "Tennessee Avenue",
        "New York Avenue",
        "Free Parking",
        "Kentucky Avenue",
        "Chance (near Kentucky Avenue)",
        "Indiana Avenue",
        "Illinois Avenue",
        "B&O Railroad",
        "Atlantic Avenue",
        "Ventnor Avenue",
        "Water Works",
        "Marvin Gardens",
        "Go To Jail",
        "Pacific Avenue",
        "North Carolina Avenue",
        "Community Chest (near North Carolina Avenue)",
        "Pennsylvania Avenue",
        "Short Line Railroad",
        "Chance (near Pennsylvania Avenue)",
        "Park Place",
        "Luxury Tax",
        "Boardwalk",
    ]

    nonstandard_squares = [2, 7, 17, 22, 30, 33, 36]  # 0-indexed

    for i in range(40):
        if i in nonstandard_squares:
            continue
        start_index = i + 2
        for j, prob in enumerate(probabilities):
            board[i, (start_index + j) % 40] = prob

    print(board[-1])


def transition_matrix():
    pass


create_board()
