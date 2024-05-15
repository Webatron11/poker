from datetime import datetime
import sqlite3
from data import Session, balances, players
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


def all_players(date, dbconn, dbcur):
    session = Session(0, [], [], [], balances)

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
              date.strftime("%Y/%m/%d") +
              "', '" + ", ".join(session.players) +
              "', '" + ", ".join(session.buyins) +
              "', '" + ", ".join(session.revbuyins) +
              "'"
              )

    dbcur.execute(f"INSERT INTO poker({fields}) VALUES ({values})")
    dbconn.commit()


def one_player(date, dbconn, dbcur):
    for player in players:
        print(f"{players.index(player)}. {player.name}")
    player = input("Which player would you like to edit session data for? ")
    if player is int:
        player = players[player]
    if player.lower() in players:
        player = player.lower()


one_player(today, conn, cur)

cur.close()
conn.close()
