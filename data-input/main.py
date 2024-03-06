from datetime import datetime
import sqlite3
from data import *
from functions import *

# Ask user for players
#   Recurse through list and ask for yes/no answer
# Ask user for buyins
# Ask user for revbuyins
# Ask user for player balances
#   Error check for correct # W # R # B # G format (regex)
#   Recurse through the list of players inputted.

session = Session(0, [], [], [], [])

for i in players:
    if yninput(session, "players", i) == "Y":
        yninput(session, "buyins", i)
        yninput(session, "revbuyins", i)

for i in session.players:
    balanceinput(session, i)

print(vars(session))

conn = sqlite3.connect('database.db')
cur = conn.cursor()

lowerplayers = list()
for i in session.players:
    lowerplayers.append(i.lower())

fields = ', '.join(lowerplayers) + ", date, players, buyins, revbuyins"

playerbalances = "'"
for i in lowerplayers:
    if vars(session)[i] != '':
        playerbalances += vars(session)[i] + "', '"

today = datetime.now()

values = (playerbalances +
          today.strftime("%Y/%m/%d %H:%M:%S") +
          "', '" + ", ".join(session.players) +
          "', '" + ", ".join(session.buyins) +
          "', '" + ", ".join(session.revbuyins) +
          "'"
          )

print(values)
cur.execute(f"INSERT INTO poker({fields}) VALUES ({values})")
conn.commit()

cur.close()
conn.close()
