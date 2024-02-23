from dateutil import *
import psycopg2 as psql
import json
from data import *
from functions import *

# with open('connection.json') as f:
#     connectioninfo = json.load(f)
#
# conn = psql.connect(database="poker", user=connectioninfo['user'], password=connectioninfo['password'], host=connectioninfo['host'], port=connectioninfo['port'])
# cur = conn.cursor()
#
# cur.execute('SELECT * FROM poker;')
#
# cur.close()
# conn.close()

# WHAT IF WE STORE THE SESSION VARIABLE IN THE DATABASE INSTEAD OF THE SEPERATE DATA - LESS REDUNDANT PROCESSES!!!!

# Ask user for players
#   Recurse through list and ask for yes/no answer
# Ask user for buyins
# Ask user for revbuyins
# Ask user for player balances
#   Error check for correct # W # R # B # G format (regex)
#   Recurse through the list of players inputted.

session = Session(0, [], [], [], "", "", "", "", "", "", "")

for i in players:
    if yninput(session, "players", i) == "Y":
        yninput(session, "buyins", i)
        yninput(session, "revbuyins", i)

for i in session.players:
    balanceinput(session, i)

print(vars(session))
