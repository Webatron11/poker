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

with open('temp.json', 'r') as f:
    data = json.load(f)
    s = data['session']
    session = Session(s[0]['number'], s[1]['players'], s[2]['buyins'], s[3]['revbuyins'], s[4]['balances'])
while True:
    player_temp = input("Who is playing: ").lower()
    if player_temp in [i.name.lower() for i in players] or player_temp.lower() == "merge" or player_temp.lower() == "plzfix":
        break

if player_temp.lower() == "merge":
    playerbalances = "'"
    for i in players:
        if session.balances[i.name] is not None:
            playerbalances += session.balances[i.name] + "', '"
    today = datetime.now()
    fields = ', '.join([i.lower() for i in session.players]) + ", date, players, buyins, revbuyins"

    values = (playerbalances +
        today.strftime("%Y/%m/%d %H:%M:%S") +
        "', '" + ", ".join(session.players) +
        "', '" + ", ".join(session.buyins) +
        "', '" + ", ".join(session.revbuyins) +
        "'"
        )

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute(f"INSERT INTO poker({fields}) VALUES ({values})")
    conn.commit()

    cur.close()
    conn.close()
    with open('temp.json', 'w') as file:
        file.write(json.dumps({"session": [{"number": 0}, {"players": []}, {"buyins": []}, {"revbuyins": []}, {"balances": balances}]}, indent=2))
        exit()
