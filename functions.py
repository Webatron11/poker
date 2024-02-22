import re
from data import *


def chipstobalance(chips: str):
    # Uses regex to seperate inputed string into W, R, B, G chip counts and then creating a total balance
    regex = r'\d+\s*'

    matches = re.findall(regex, chips)
    formated = []

    for i in matches:
        formated.append(int(i.strip()))

    # I can't actually rememeber why this is here.

    try:
        return (formated[0] * 10) + (formated[1] * 25) + (formated[2] * 100) + (formated[3] * 500)
    except IndexError:
        return 0


def balance(sessions, player: Player):
    # Appends session chip total for a player onto their balanceovertime, vars converts strings into a variable name, and we need it to all be lower case as the variable names are lower case
    name = player.name.lower()

    for i in sessions:
        if vars(i)[name] != '':
            player.balanceovertime.append(chipstobalance(vars(i)[name]))
        else:
            if len(player.balanceovertime) == 0:
                player.balanceovertime.append(0)
            else:
                player.balanceovertime.append(player.balanceovertime[-1])

    player.balance = player.balanceovertime[-1]


def buyin(sessions, player):
    # Goes through all the sessions and adds up a player's buyins by checking if their name appears in the buyin column of the session.
    for i in sessions:
        if player.name in i.buyins:
            player.buyins += 1


def revbuyin(sessions, player):
    # Goes through all the sessions and adds up a player's revbuyins by checking if their name appears in the revbuyin column of the session.
    for i in sessions:
        if player.name in i.revbuyins:
            player.revbuyins += 1


def profit(sessions, player):
    # It SHOULD take the player balance overtime, apply any buyins or revbuyins then append it to the profit list in order to create a profit over time
    # thing, but it doesn't work yet.

    # Profit = balance - buyins + revbuyins

    buyintotal = player.buyins
    revbuyintotal = player.revbuyins

    # Check for revbuyin/buyin
    # index revbuyin/buyin if present
    # make profitovertime = balanceovertime + (revbuyintotal * 2000) - (buyintotal * 2000)

    for i in range(len(player.balanceovertime)):

        if player.name in sessions[i].buyins:
            buyintotal += 1

        if player.name in sessions[i].revbuyins:
            revbuyintotal += 1

        player.profitovertime.append(player.balanceovertime[i] - (buyintotal * 2000) + (revbuyintotal * 2000))
