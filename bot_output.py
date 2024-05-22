import matplotlib.pyplot as plt
from tabulate import tabulate

from data import players, balances, Session
from functions import *


def create_sessions():
    sessions = []
    conn = connect('database.db')
    cur = conn.cursor()

    # Reads db file and parses the information into an array of the Session type.

    data = cur.execute('SELECT * FROM poker ORDER BY date')
    data = data.fetchall()

    for row in data:
        for player in players:
            index = players.index(player) + 4
            if row[index] == "":
                balances[player.name] = None
            else:
                balances[player.name] = row[index]

        sessions.append(
            Session(len(sessions) + 1, row[1].split(', '), row[2].split(', '), row[3].split(', '), balances.copy()))

    cur.close()
    conn.close()

    for player in players:
        parsebalance(sessions, player)
        profit(sessions, player)
        buyin(sessions, player)
        revbuyin(sessions, player)

        if len(player.profitovertime) >= len(sessions):
            player.balanceovertime = player.balanceovertime[:len(sessions)]
            player.profitovertime = player.profitovertime[:len(sessions)]

        # Writes player balance for a session to that session
        for session in sessions:
            if session.balances[player.name] is not None:
                player.balance = session.balances[player.name]

    return sessions


def print_table():
    create_sessions()
    table = [[player.name, player.balance, player.profitovertime[-1], player.buyins, player.revbuyins] for player in
             players]
    return tabulate(table, headers=['Name', 'Chip Balance', 'Profit', 'Buyins', 'Revbuyins'], tablefmt='github')


def map_sessions():
    # fetch date column
    # print date with date index + 1

    conn = connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT date FROM poker ORDER BY date DESC")
    data = cur.fetchall()

    cur.close()
    conn.close()

    return tabulate([[i + 1, data[i][0].split(" ")[0]] for i in range(len(data))], tablefmt='github')


def create_graph():
    sessions = create_sessions()

    sessionnumbers = [i + 1 for i in range(len(sessions))]

    for player in players:
        plt.plot(sessionnumbers, player.profitovertime, marker='x', label=player.name)

    # Finds smallest profit and largest profit
    smallest = 0
    largest = 0
    for player in players:
        if player.profitovertime[-1] > largest:
            largest = player.profitovertime[-1]
        elif player.profitovertime[-1] < smallest:
            smallest = player.profitovertime[-1]

    plt.title("Profit Over Time")
    plt.ylim([smallest - 500, largest + 2000])
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left", borderaxespad=0)
    plt.xlabel("Session Number")
    plt.ylabel("Profit")
    plt.grid(True)
    plt.subplots_adjust(right=0.8)

    plt.savefig("graph.png")
    plt.close()
