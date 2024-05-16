from datetime import datetime
import sqlite3
from data import *
from functions import *
import json

def open_session():
    with open('temp.json', 'r') as f:
        data = json.load(f)
        s = data['session']
        session = Session(s[0]['number'], s[1]['players'], s[2]['buyins'], s[3]['revbuyins'], s[4]['balances'])
    return session

def process_results(results: dict):
    session = open_session()   

    player = [p for p in players if p.name == results['name'][0]]
    player = player[0]
    if player.name not in session.players:
        session.players.append(player.name)
    #print(player.name)
    yninput(session, results['buyinyn'], results['revbuyyn'], results['buyins'], results['revbuys'], player)

    session.balances[player.name] = results['balance']

    return_buyins = checkbuy(session, player.name)
    return_revbuys = checkrev(session, player.name)

    with open('temp.json', "r") as f:
        data = json.load(f)
        s = data['session']
        s[0]['number'] = session.number
        s[1]['players'] = session.players
        s[2]['buyins'] = session.buyins
        s[3]['revbuyins'] = session.revbuyins
        s[4]['balances'] = session.balances
    with open('temp.json', 'w') as f:
        f.write(json.dumps(data, indent=2))
    
    return (return_buyins, return_revbuys)

def merge_results():
    session = open_session()
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

def plz_fix():
    with open('temp.json','w') as file:
        file.write(json.dumps({"session": [{"number": 0}, {"players": []}, {"buyins": []}, {"revbuyins": []}, {"balances": balances}]}, indent=2))