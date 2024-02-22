from dateutil import *
import psycopg2 as psql
import json

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
#   Error check for correct # W # R # B # G format (regex??)
#   Check if all players have an updated balance (eg there isn't a player in the players section who doesn't have a balance inputted)
#   Could be easy to do if you just recurse through the list of players inputted.


