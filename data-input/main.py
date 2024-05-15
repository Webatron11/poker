from datetime import datetime
import sqlite3
from data import Session, balances
from functions import *


# Ask user for players
#   Recurse through list and ask for yes/no answer
# Ask user for buyins
# Ask user for revbuyins
# Ask user for player balances
#   Error check for correct # W # R # B # G format (regex)
#   Recurse through the list of players inputted.

today = datetime.now()
conn = sqlite3.connect('database.db')
cur = conn.cursor()

session = Session(0, [], [], [], balances)

edit = input("Do you want to edit one player (Y/N)").upper()
if edit == "Y":
    one_player = one_player(session)
    yninput(session, "buyins", one_player)
    yninput(session, "revbuyins", one_player)
else:
    for player in players:
        if yninput(session, "players", player) == "Y":
            yninput(session, "buyins", player)
            yninput(session, "revbuyins", player)

for player in session.players:
    balanceinput(session, player)
checkbuy(session)
checkrev(session)

playerbalances = "'"
for player in players:
    if session.balances[player.name] is not None:
        playerbalances += session.balances[player.name] + "', '"
fields = ', '.join([player.lower() for player in session.players]) + ", date, players, buyins, revbuyins"

values = (playerbalances +
          today.strftime("%Y/%m/%d") +
          "', '" + ", ".join(session.players) +
          "', '" + ", ".join(session.buyins) +
          "', '" + ", ".join(session.revbuyins) +
          "'"
          )

cur.execute(f"INSERT INTO poker({fields}) VALUES ({values}) ON CONFLICT DO UPDATE SET {one_player}")
conn.commit()

cur.close()
conn.close()
