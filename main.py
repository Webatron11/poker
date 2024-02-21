import csv
from functions import *
import matplotlib.pyplot as plt

# Player initialisation. Adds a -600 profit from the get go because of the initial buyin. The 0.3 for buyins is for the initial 600 buyin before the number was changed

aidan = Player("Aidan", 0, 0.3, 0, [0], [-600])
ben = Player("Ben", 0, 0.3, 0, [0], [-600])
cooper = Player("Cooper", 0, 0.3, 0, [0], [-600])
hunter = Player("Hunter", 0, 0.3, 0, [0], [-600])
mitchell = Player("Mitchell", 0, 0.3, 0, [0], [-600])
oscar = Player("Oscar", 0, 0.3, 0, [0], [-600])
xavier = Player("Xavier", 0, 0.3, 0, [0], [-600])

# Array of players in order to index through all players.

players = [aidan, ben, cooper, hunter, mitchell, oscar, xavier]

sessions = []

# Reads csv file and parses the information into an array of the Session type.

csv_read = ''
with open('Poker1.csv') as f:
    csv_read = csv.reader(f, delimiter=',')

    next(csv_read)

    i = 1 # This is for the session number.
    for row in csv_read:
        session = Session(i, row[1].split(';'), row[2].split(';'), row[3].split(';'), row[4], row[5], row[6], row[7], row[8], row[10], row[11])
        sessions.append(session)
        i += 1

# Makes an array of integers so we can graph stuff based on session number.

sessionnumbers = [0]
for i in range(len(sessions)):
    sessionnumbers.append(i+1)

# Does all the math stuff.

for i in players:
    balance(sessions, i)
    buyin(sessions, i)
    revbuyin(sessions, i)
    # profit(sessions, i) # Non-functional function to be added later
    i.balance = i.balance - (i.buyins * 2000) + (i.revbuyins * 2000) # This just creates a final balance based off buyins and revbuyins
    # TODO make final balance correct......
    print(i.balance, i.balanceovertime, i.profit, i.buyins, i.revbuyins, i.name) # Bug checking for now, going to output data in a prettier manner later

    # Plotting balanceovertime against session number. Should be self-explanatory

    plt.plot(sessionnumbers, i.balanceovertime, marker='x')
    # TODO make it plot negative numbers, change scale of x, interactive????
    plt.ylim(min(i.balanceovertime), max(i.balanceovertime))

    plt.xlabel("Session Number")
    plt.ylabel("Balance")
    plt.title(i.name)
    plt.grid(True)

    plt.show()