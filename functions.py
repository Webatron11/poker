import re
from sqlite3 import connect

def chipstobalance(chips: str):
    # Uses regex to separate inputted string into W, R, B, G, Bl, P chip counts and then creating a total balance
    regex = r'\d+\s*'

    matches = re.findall(regex, chips)
    formatted = []

    # Takes all matches from balance string and then strips them of whitespace

    for i in matches:
        formatted.append(int(i.strip()))

    # Takes the formatted matches and times them by their respective chip amounts for the end total

    try:
        balance = (formatted[0] * 1) + (formatted[1] * 5) + (formatted[2] * 10) + (formatted[3] * 25) + (formatted[4] * 100)
        return balance
    except IndexError:
        return 0

def parsebalance(sessions, player):
    # Appends session chip total for a player onto their balance overtime, vars converts strings into a variable name,
    # and we need it to all be lower case as the variable names are lower case
    for session in sessions:
        if session.balances[player.name] is not None:
            player.balanceovertime.append(chipstobalance(session.balances[player.name]))
        else:
            if len(player.balanceovertime) == 0:
                player.balanceovertime.append(0)
            else:
                player.balanceovertime.append(player.balanceovertime[-1])

        player.balance = player.balanceovertime[-1]

def buyin(sessions, player):
    # Goes through all the sessions and adds up a player's buyins by checking if their name appears in the buyin column
    # of the session.
    for i in sessions:
        for x in i.buyins:
            if player.name == x:
                player.buyins += 1

def revbuyin(sessions, player):
    # Goes through all the sessions and adds up a player's revbuyins by checking if their name appears in the revbuyin
    # column of the session.
    for i in sessions:
        for x in i.revbuyins:
            if player.name == x:
                player.revbuyins += 1

def profit(sessions, player):
    # It takes the player balance overtime, applies any buyins or revbuyins then appends it to the profit list in
    # order to create a profit over time thing

    # Profit = balance - buyins + revbuyins

    buyintotal = player.buyins
    revbuyintotal = player.revbuyins

    # Check for revbuyin/buyin
    # index revbuyin/buyin if present
    # make profitovertime = balanceovertime + (revbuyintotal * 2000) - (buyintotal * 2000)
    for i in range(len(sessions)):
        if player.name in sessions[i].buyins:
            buyintotal += sessions[i].buyins.count(player.name)
        if player.name in sessions[i].revbuyins:
            revbuyintotal += sessions[i].revbuyins.count(player.name)
        player.balanceovertime = player.balanceovertime[:len(sessions)]
    # remove all buyins up to this point
    # add all revbuyins up to this point
        
        player.profitovertime.append(player.balanceovertime[i] - (buyintotal * 200) + (revbuyintotal * 200))

def yninput(session, buyinyn, revbuyyn, buyins, revbuys, player):
    if buyinyn == 'Y':
        session.buyins.append(player.name)
    if revbuyyn == 'Y':
        session.revbuyins.append(player.name)

def checkrev(session, player):
    balance = chipstobalance(session.balances[player])
    if balance >= 500:
        cnt = 1
        while True:
            if (balance - (200*cnt)) < 500:
                break
            else:
                cnt += 1
        for i in range(cnt):
            session.revbuyins.append(player)
        return f'{player} has had {cnt} reverse buy ins. Please remove the correct number of chips'

def checkbuy(session, player):
    if chipstobalance(session.balances[player]) <= 100:
        session.buyins.append(player)
        return f'{player} has had 1 buy in. Please add the correct number of chips to their bag.'

def add_user(player):
    conn = connect('database.db')
    cur = conn.cursor()
    cur.execute(f"alter table poker add {player.lower()};")
    conn.commit()