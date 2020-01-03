""" Added logging function of who wins, into the 'results' table.
    The way it works is that assumes choosing_player (goes first)
    presses "ready" first.

    Rusmat Ahmed, Future Learn, Programming 103.
    29 November 2019

"""
import sqlite3
from random import randint
from time import time

conn = sqlite3.connect("computer_cards.db")

def create(name, cores, cpu_speed, ram, cost):
    insert_sql = "INSERT INTO computer(name, cores, cpu_speed, ram, cost) VALUES ('{}', {}, {}, {}, {})".format(name, cores, cpu_speed, ram, cost)
    conn.execute(insert_sql)
    conn.commit()

def delete(Name):
    delete_sql = "DELETE FROM computer WHERE name = '{}'".format(Name)
    conn.execute(delete_sql)
    conn.commit()

def read(name):
    select_sql = "SELECT * FROM computer WHERE name = '{}'".format(name)
    result = conn.execute(select_sql)
    return result.fetchone()

def update(name, cores, cpu_speed, ram, cost):
    update_sql = "UPDATE computer SET cores = {}, cpu_speed = {}, ram = {}, cost = {} WHERE name = '{}'".format(cores, cpu_speed, ram, cost, name)
    conn.execute(update_sql)
    conn.commit()

def read_all_cards():
    result = conn.execute("SELECT * FROM computer")
    return result.fetchall()

# inserts card and timestamp into 'picked' table
def insert_picked(name):
    insert_sql = "INSERT INTO picked(name, time) VALUES ('{}', {})".format(name, time())
    conn.execute(insert_sql)
    conn.commit()

# read last picked card
def read_last_picked():
    result = conn.execute("SELECT * FROM picked ORDER BY time DESC")
    return result.fetchone()

# updated pick_card function, that checks for duplicates
def pick_card():
    cards = read_all_cards()
    last_picked_card = read_last_picked()
    random_card = cards[randint(0, len(cards) - 1)]
    while random_card[0] == last_picked_card[0]:
        random_card = cards[randint(0, len(cards) - 1)]
    insert_picked(random_card[0])
    return random_card

# below is used to get players's cards in right field of 'results' table. Assumes lower timestamp in 'picked' table
# is the one who won previous round
def return_last_but_two():
    remove_str = "[(')]"
    temp = ''
    result = conn.execute("SELECT * FROM 'picked' ORDER BY time DESC LIMIT 2")
    a_string =  str(result.fetchall())
    for char in a_string:
        if char not in remove_str:
            temp += char
    output = [list(temp.split(","))[0], list(temp.split(","))[2]]
    return output

# function to insert correctly into 'result' table
def add_to_result(choosing_player, output, win):
    # card1 = None
    # card2 = None
    # winner = None
    if choosing_player == "1":
        card1 = output[1]
        card2 = output[0]
    elif choosing_player == "2":
        card1 = output[0]
        card2 = output[1]
    if win == "y" and choosing_player == "1":
        winner = card1
        insert_sql = "INSERT INTO result(card1, card2, winner) VALUES ('{}', '{}', '{}')".format(card1, card2,
                                                                                                 winner)
        conn.execute(insert_sql)
        conn.commit()
    if win == "y" and choosing_player == "2":
        winner = card2
        insert_sql = "INSERT INTO result(card1, card2, winner) VALUES ('{}', '{}', '{}')".format(card1, card2,
                                                                                                 winner)
        conn.execute(insert_sql)
        conn.commit()
    else:
        pass

# = = = game itself below this line = = =
player = input("Are you player (1) or (2) > ")
choosing_player = "1"

for round in range(2):
    input("Press enter to pick a card when both players are ready > ")
    card = pick_card()
    card_text = "{}, cores={}, speed={}GHz, RAM={}MB, cost={}$".format(card[0], card[1], card[2], card[3], card[4])
    print(card_text)
    print("Player " + choosing_player + " picks.")
    win = input("Did you win? (Y)es, (N)o, (D)raw > ").lower()

    # read last 2 cards put into 'picked' table
    output = return_last_but_two()
    print(output)

    # insert_into_result(output, player, choosing_player, win)
    add_to_result(choosing_player, output, win)

    # adjust choosing_player if needed
    if win == "y":
        choosing_player = player
    elif win == "n":
        choosing_player = "2" if player == "1" else "1"

conn.close()




