import numpy as np


def create_board():
    board = np.zeros((40, 40))

    old_probabilities = [
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

    # (1/6)^3 chance of rolling 3 pairs in a row --> jail. Refactored probabilities on paper

    probabilities = [
        0.02753703259259259,
        0.0556,
        0.0825120437037037,
        0.1111,
        0.1375861088888889,
        0.1667,
        0.1375861088888889,
        0.1111,
        0.0825120437037037,
        0.0556,
        0.02753703259259259,
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

    # 2 - community chest, 7 - chance, 17 - community chest, 22 - chance, 30 - jail, 33 - community chest, 36 - chance

    # Community Chest: 1/16 go, 1/16 jail. Subtract (2*1/16)/6 from probabilities, add go/jail:
    chest_probabilities = [p * (14 / 16) for p in probabilities]
    chest_squares = [2, 17, 33]

    # Chance: 1/16: boardwalk, Go, Illinois, St. Charles, nearest Utility, Go Back 3, Jail, Reading Railroad, 2/16: nearest Railroad
    # Subtract (10/16)/11 from probabilities
    chance_probabilities = [p * (6 / 16) for p in probabilities]
    chance_squares = [7, 22, 36]

    for i in range(40):
        if i in chest_squares:
            for j, prob in enumerate(chest_probabilities):
                board[i, (i + j + 2) % 40] = prob
            board[i, 0] += 215 / 3456
            board[i, 30] += 215 / 3456

        elif i in chance_squares:
            for j, prob in enumerate(chance_probabilities):
                board[i, (i + j + 2) % 40] = prob
            board[i, 39] += 1075 / 17280
            board[i, 0] += 1075 / 17280
            board[i, 24] += 1075 / 17280
            board[i, 11] += 1075 / 17280
            board[i, i - 3] += 1075 / 17280
            board[i, 30] += 1075 / 17280
            board[i, 5] += 1075 / 17280

            if i == 7:  # Chance near Oriental
                board[i, 12] += 1075 / 17280
                board[i, 15] += 1075 / 8640
            elif i == 36:  # Chance near Park Place
                board[i, 12] += 1075 / 17280
                board[i, 5] += 1075 / 8640
            else:  # Chance near Kentucky
                board[i, 28] += 1075 / 17280
                board[i, 25] += 1075 / 8640

        else:  # Normal Squares
            for j, prob in enumerate(probabilities):
                board[i, (i + j + 2) % 40] = prob

        # add (1/216) in the Jail cell (column 30)
        board[i, 30] += 1 / 216

        print(f"Sum of entries in row {i}: {board[i].sum()}")


def transition_matrix():
    pass


create_board()
