import sqlite3
from random import randint
from time import time

# path = "/home/pi/Downloads/"
database = "computer_cards.db"
cards = []

# Connect to database
conn = sqlite3.connect(database)

# retrieve computer table
def read_all_cards():
    result = conn.execute("SELECT * FROM computer")
    return result.fetchall()

# pick a random card
def pick_card():
    cards = read_all_cards()
    random_card = cards[randint(0, len(cards) - 1)]
    insert_picked(random_card[0])
    return random_card

# record picked card
def insert_picked(name):
    insert_sql = "INSERT INTO picked(name, time) VALUES ('{}', {})".format(name, time())
    conn.execute(insert_sql)
    conn.commit()
    return

# get last card picked
def read_last_picked():
    result = conn.execute("SELECT * FROM picked ORDER BY time DESC")
    return result.fetchone()

# get last two cards picked
def get_last_2_cards_picked():
    result = conn.execute("SELECT * FROM picked ORDER BY time DESC LIMIT 2")
    records = result.fetchall()
    print(records)
    for record in records:
        cards.append(record[0])
    return cards

def add_result(card1, card2, winner):
    result_sql = "INSERT INTO result(card1, card2, winner) VALUES ('{}', '{}', '{}')".format(card1, card2, winner)
    conn.execute(result_sql)
    conn.commit()
    return

# game setup
player = input("Are you player (1) or (2) >")
choosing_player = "1"

# game loop
for round in range(3):
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
    # get winning card and save result
    cards_played = get_last_2_cards_picked()
    card1 = cards_played[1]
    card2 = cards_played[0]
    if choosing_player == "1":
        add_result(card1, card2, card1)
    elif choosing_player == "2":
        add_result(card1, card2, card2)

conn.close()