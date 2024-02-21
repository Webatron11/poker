import re
from data import *


def chipstobalance(chips: str):
    ### Uses regex to seperate inputed string into W, R, B, G chip counts and then creating a total balance
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
    # Appends session chip total for a player onto their balanceovertime, vars converts strings into a variable name and we need it to all be lower case as the variable names are lower case
    name = player.name.lower()


    # TODO UNBREAK THIS IDK WHY IT DOESN'T WORK
    for i in sessions:
        if vars(i)[name] != '':
            player.balanceovertime.append(chipstobalance(vars(i)[name]))
        else:
            player.balanceovertime.append(player.balanceovertime[-1])

    player.balance = player.balanceovertime[-1]


def buyin(sessions, player):
    ### Goes through all the sessions and adds up a player's buyins by checking if their name appears in the buyin column of the session.
    for i in sessions:
        if player.name in i.buyins:
            player.buyins += 1


def revbuyin(sessions, player):
    ### Goes through all the sessions and adds up a player's revbuyins by checking if their name appears in the revbuyin column of the session.
    for i in sessions:
        if player.name in i.revbuyins:
            player.revbuyins += 1


def profit(sessions, player):
    ### It SHOULD take the player balance overtime, apply any buyins or revbuyins then append it to the profit list in order to create a profit over time
    ### thing, but it doesn't work yet.

    for i in range(len(player.balanceovertime)):
        i -= 1
        if player.name in sessions[i].revbuyins:
            player.profit.append(player.balanceovertime[i] + (1 * 2000))
        elif player.name in sessions[i].buyins:
            player.profit.append(player.balanceovertime[i] - (1 * 2000))
        else:
            player.profit.append(player.balanceovertime[i])

        # TODO need to make it not just copy last one, but also include the last shit. i have no idea what that means, look at the stuff to make sense of it
