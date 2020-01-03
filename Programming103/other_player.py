"""" Next part is the Making the Game 2 players assignments

"""
import sqlite3
from random import randint
from time import time

conn = sqlite3.connect("computer_cards.db")

def create(name, cores, cpu_speed, ram, cost):
    insert_sql = "INSERT INTO computer(name, cores, cpu_speed, ram, cost) VALUES ('{}', '{}', '{}', '{}', '{}')".format(name, cores, cpu_speed, ram, cost)
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

# function to put player 1 & 2 cards into db's 'result' table, and let know which card won
def input(card, winner):
    if player == "1":
        insert_sql = "INSERT INTO result(card1) VALUES ('{}')".format(card[0])
        conn.execute(insert_sql)
        conn.commit()
    else:
        insert_sql = "INSERT INTO result(card2) VALUES ('{}')".format(card[0])
        conn.execute(insert_sql)
        conn.commit()
    if winner == "y":
        insert_sql = "INSERT INTO result(winner) VALUES ('{}')".format(card[0])
        conn.execute(insert_sql)
        conn.commit()


# = = = game itself below this line = = =
player = input("Are you player (1) or (2) >")
choosing_player = "1"
for round in range(5):
    input("Press enter to pick a card when both players are ready >")
    card = pick_card()
    card_text = "{}, cores={}, speed={}GHz, RAM={}MB, cost={}$".format(card[0], card[1], card[2], card[3], card[4])
    print(card_text)
    print("Player " + choosing_player + " picks.")
    winner = input("Did you win? (Y)es, (N)o, (D)raw >").lower()
    if winner == "y":
        choosing_player = player
    elif winner == "n":
        choosing_player = "2" if player == "1" else "1"
    #input(card, winner)
conn.close()








