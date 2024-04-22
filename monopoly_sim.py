import random
import matplotlib.pyplot as plt
import numpy as np

def roll_dice():
    return (random.randrange(1,7))

def chance_cards():
    card_pull = (random.randrange(1,16))
    #there are 16 possible community chest and chance cards
    #of those 16, there are 1 Get out of Jail Free Card and 1 Go to Jail Card
    return card_pull

def monopoly_simulation():
    curr_state = 0 #shows what the current square is
    NUM_OF_ROLLS = 250
    arr = [0] * 40
    doubles = 0
    jail_rolls = 0
    get_out = False
    for i in range(NUM_OF_ROLLS):
        #rolling dice
        roll_1 = roll_dice()
        roll_2 = roll_dice()
        #if you are in jail (or in go to jail square)
        if curr_state == 30:
            if roll_1 == roll_2 or jail_rolls > 2 or get_out == True:
                curr_state = 10 + roll_1 + roll_2
                jail_rolls = 0
                get_out = False
            else:
                jail_rolls = jail_rolls + 1
                curr_state = 30
        else:
            curr_state = curr_state + roll_1 + roll_2
        
        if roll_1 == roll_2:
            doubles = doubles + 1
        else:
            doubles = 0
        if doubles == 3:
            curr_state = 30
            doubles = 0
        
        #if you land on a chance card
        if curr_state == 7 or curr_state == 22 or curr_state == 36:
            p = chance_cards()
            #arbitrary get out of jail free and go to jail
            if p == 1:
                curr_state = 39
            elif p == 2:
                curr_state = 0
            elif p == 3:
                curr_state = 24
            elif p == 4:
                curr_state = 11
            elif p == 5 or p == 6:
                if curr_state <= 5:
                    curr_state = 5
                elif curr_state <= 15:
                    curr_state = 15
                elif curr_state <= 25:
                    curr_state = 25
                elif curr_state <= 35:
                    curr_state = 35
                else:
                    curr_state = 5
            elif p == 7:
                if curr_state <= 12:
                    curr_state = 12
                elif curr_state <= 28:
                    curr_state = 28
                else:
                    curr_state = 12
            elif p == 9:
                get_out = True
            elif p == 10:
                curr_state = curr_state-3
            elif p == 11:
                curr_state = 30
            elif p == 14:
                curr_state = 5

        if curr_state == 2 or curr_state == 17 or curr_state == 33: 
            p = chance_cards()
            if p == 1:
                curr_state = 0
            if p == 5:
                get_out = True
            if p == 6:
                curr_state = 30

        #looping through board
        if curr_state > 39:
            curr_state = curr_state - 40

        #keeping track of location
        arr[curr_state] = arr[curr_state] + 1
    property_map = {0: "Go", 1: "Mediterranean Avenue", 2: "Community Chest", 3: "Baltic Avenue", 4: "Income Tax",
                    5: "Reading Railroad", 6: "Oriental Avenue", 7: "Chance", 8: "Vermont Avenue", 9: "Connecticut Avenue", 
                    10: "Just Visiting", 11: "St. Charles Place", 12: "Electric Company", 13: "States Avenue", 14: "Virginia Avenue",
                    15: "Pennsylvania Railroad", 16: "St. James Place", 17: "Community Chest", 18: "Tennessee Avenue", 19: "New York Avenue",
                    20: "Free Parking", 21: "Kentucky Avenue", 22: "Chance", 23: "Indiana Avenue", 24: "Illinois Avenue", 
                    25: "B. & O. Railroad", 26: "Atlantic Avenue", 27: "Ventnor Avenue", 28: "Water Works", 29: "Marvin Gardens",
                    30: "Jail", 31: "Pacific Avenue", 32: "North Carolina Avenue", 33: "Community Chest", 34: "Pennsylvania Avenue",
                    35: "Short Line", 36: "Chance", 37: "Park Place", 38: "Luxury Tax", 39: "Boardwalk"}
    for i in range(len(arr)):
        arr[i] = arr[i] / NUM_OF_ROLLS
    
    return arr

def main():
    exp_num = input("How many times to run: ")
    property_map = {0: "GO", 1: "Mediterranean Avenue", 2: "Community Chest", 3: "Baltic Avenue", 4: "Income Tax",
                    5: "Reading Railroad", 6: "Oriental Avenue", 7: "Chance", 8: "Vermont Avenue", 9: "Connecticut Avenue", 
                    10: "Just Visiting", 11: "St. Charles Place", 12: "Electric Company", 13: "States Avenue", 14: "Virginia Avenue",
                    15: "Pennsylvania Railroad", 16: "St. James Place", 17: "Community Chest", 18: "Tennessee Avenue", 19: "New York Avenue",
                    20: "Free Parking", 21: "Kentucky Avenue", 22: "Chance", 23: "Indiana Avenue", 24: "Illinois Avenue", 
                    25: "B. & O. Railroad", 26: "Atlantic Avenue", 27: "Ventnor Avenue", 28: "Water Works", 29: "Marvin Gardens",
                    30: "Jail", 31: "Pacific Avenue", 32: "North Carolina Avenue", 33: "Community Chest", 34: "Pennsylvania Avenue",
                    35: "Short Line", 36: "Chance", 37: "Park Place", 38: "Luxury Tax", 39: "Boardwalk"}
    color_map = {"GO": "lightgray", "Mediterranean Avenue": "brown", "Community Chest": "lightgray",
                "Baltic Avenue": "brown", "Income Tax": "lightgray", "Reading Railroad": "black",
                "Oriental Avenue": "cyan", "Chance": "lightgray", "Vermont Avenue": "cyan",
                "Connecticut Avenue": "cyan", "Just Visiting": "lightgray", "St. Charles Place": "magenta",
                "Electric Company": "lightgray", "States Avenue": "magenta", "Virginia Avenue": "magenta",
                "Pennsylvania Railroad": "black", "St. James Place": "orange", "Tennessee Avenue": "orange",
                "New York Avenue": "orange", "Free Parking": "lightgray", "Kentucky Avenue": "red",
                "Indiana Avenue": "yellow", "Illinois Avenue": "yellow", "B. & O. Railroad": "black",
                "Atlantic Avenue": "green", "Ventnor Avenue": "green", "Water Works": "lightgray",
                "Marvin Gardens": "green", "Pacific Avenue": "blue", "North Carolina Avenue": "blue",
                "Short Line": "black", "Pennsylvania Avenue": "blue", "Park Place": "purple",
                "Luxury Tax": "lightgray", "Boardwalk": "purple", "Jail": "lightgray"}
    final = [0] * 40
    exp_num = int(exp_num)
    for i in range(exp_num):
        x = monopoly_simulation()
        for i in range(len(x)):
            final[i] += x[i]
    for i in range(len(final)):
        final[i] = final[i] / exp_num
        final[i] = final[i]
        print("{:<25}{:.3%}".format(property_map[i], final[i]))

    colors = [color_map[property_map[i]] for i in range(len(final))]
    plt.figure(figsize=(15, 8))
    plt.bar(np.arange(len(property_map)), final, align='center', alpha=0.5, color=colors)
    plt.xticks(np.arange(len(property_map)), property_map.values(), rotation='vertical')
    plt.ylabel('Probability')
    plt.title('Probability of Landing on Each Monopoly Square')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()