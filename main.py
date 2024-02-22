import csv

import matplotlib.pyplot as plt

from functions import *

# Player initialisation. Adds a -600 profit from the get go because of the initial buyin. The 0.3 for buyins is for the initial 600 buyin before the number was changed

aidan = Player("Aidan", 0, 0.3, 0, [], [])
ben = Player("Ben", 0, 0.3, 0, [], [])
cooper = Player("Cooper", 0, 0, 0, [], [])
hunter = Player("Hunter", 0, 0.3, 0, [], [])
mitchell = Player("Mitchell", 0, 0.3, 0, [], [])
oscar = Player("Oscar", 0, 0.3, 0, [], [])
xavier = Player("Xavier", 0, 0.3, 0, [], [])

# Array of players in order to index through all players.

players = [aidan, ben, cooper, hunter, mitchell, oscar, xavier]

sessions = []

# Reads csv file and parses the information into an array of the Session type.

csv_read = ''
with open('Poker1.csv') as f:
    csv_read = csv.reader(f, delimiter=',')

    next(csv_read)

    i = 1  # This is for the session number.
    for row in csv_read:
        session = Session(i, row[1].split(','), row[2].split(','), row[13].split(','), row[3], row[4], row[5], row[6], row[7], row[9], row[10])
        sessions.append(session)
        i += 1

# Makes an array of integers, so we can graph stuff based on session number.

sessionnumbers = []
for i in range(len(sessions)):
    sessionnumbers.append(i+1)

# Does all the math stuff.

for i in players:
    balance(sessions, i)
    profit(sessions, i)
    buyin(sessions, i)
    revbuyin(sessions, i)
    i.balance = i.balance - (i.buyins * 2000) + (i.revbuyins * 2000)  # This just creates a final balance based off buyins and revbuyins to check against profit()
    # Final balance is correct, it just doesn't match the spreadsheet - I'm 100% sure the spreadsheet is wrong.
    print(i.balanceovertime, '\n', i.profitovertime, '\n', i.buyins, i.balance, i.revbuyins, i.name, '\n')  # Bug checking for now, going to output data in a prettier manner later

    # Plotting balanceovertime against session number. Should be self-explanatory

    plt.plot(sessionnumbers, i.profitovertime, marker='x', label=i.name)
    # TODO make it plot negative numbers, change scale of x, interactive????

    plt.xlabel("Session Number")
    plt.ylabel("Profit")
    plt.grid(True)

# Finds smallest profit and largest profit
smallest = 0
largest = 0

for i in players:
    if i.profitovertime[-1] > largest:
        largest = i.profitovertime[-1]
    elif i.profitovertime[-1] < smallest:
        smallest = i.profitovertime[-1]

plt.title("Profit Over Time")
plt.ylim([smallest, largest])
plt.legend()

plt.show()
