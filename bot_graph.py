import matplotlib.pyplot as plt
from functions import *
from data import players, balances, Session
from tabulate import tabulate


def create_graph():
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

    # Makes an array of integers, so we can graph stuff based on session number.

    sessionnumbers = []
    for i in range(len(sessions)):
        sessionnumbers.append(i + 1)

    # Does all the math stuff.

    for player in players:
        parsebalance(sessions, player)
        profit(sessions, player)
        buyin(sessions, player)
        revbuyin(sessions, player)
        # This just creates a final balance based off buyins and revbuyins to check against profit()
        # if player.balance

        # Plotting balanceovertime against session number. Should be self-explanatory
        if len(player.profitovertime) >= len(sessions):
            player.balanceovertime = player.balanceovertime[:len(sessions)]
            player.profitovertime = player.profitovertime[:len(sessions)]

        plt.plot(sessionnumbers, player.profitovertime, marker='x', label=player.name)

    table = []
    for player in players:
        for session in sessions:
            if session.balances[player.name] is not None:
                player.balance = session.balances[player.name]
        table.append([player.name, player.balance, player.profitovertime[-1], player.buyins, player.revbuyins])

    print(tabulate(table, headers=['Name', 'Chip Balance', 'Profit', 'Buyins', 'Revbuyins'], tablefmt='github'))

    # Finds smallest profit and largest profit
    smallest = 0
    largest = 0
    for player in players:
        if player.profitovertime[-1] > largest:
            largest = player.profitovertime[-1]
        elif player.profitovertime[-1] < smallest:
            smallest = player.profitovertime[-1]

    plt.title("Profit Over Time")
    plt.ylim([smallest-500, largest+2000])
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left", borderaxespad=0)
    plt.xlabel("Session Number")
    plt.ylabel("Profit")
    plt.grid(True)
    plt.subplots_adjust(right=0.8)

    plt.savefig("graph.png")
    plt.close()
