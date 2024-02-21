import csv
from functions import *
import matplotlib.pyplot as plt

aidan = Player("Aidan", 0, 0.3, 0, [0], [-600])
ben = Player("Ben", 0, 0.3, 0, [0], [-600])
cooper = Player("Cooper", 0, 0.3, 0, [0], [-600])
hunter = Player("Hunter", 0, 0.3, 0, [0], [-600])
mitchell = Player("Mitchell", 0, 0.3, 0, [0], [-600])
oscar = Player("Oscar", 0, 0.3, 0, [0], [-600])
xavier = Player("Xavier", 0, 0.3, 0, [0], [-600])

players = [aidan, ben, cooper, hunter, mitchell, oscar, xavier]

sessions = []

csv_read = ''
with open('Poker.csv') as f:
    csv_read = csv.reader(f, delimiter=',')

    next(csv_read)

    i = 1
    for row in csv_read:
        session = Session(i, row[1].split(';'), row[2].split(';'), row[3].split(';'), row[4], row[5], row[6], row[7], row[8], row[10], row[11])
        sessions.append(session)
        i += 1

sessionnumbers = [0]
for i in range(len(sessions)):
    sessionnumbers.append(i+1)

for i in players:
    balance(sessions, i)
    buyin(sessions, i)
    revbuyin(sessions, i)
    profit(sessions, i)
    # i.balance = i.balance - (i.buyins * 2000) + (i.revbuyins * 2000)
    # TODO make final balance correct......
    print(i.balance, i.balanceovertime, i.profit, i.buyins, i.revbuyins, i.name)
    #
    # plt.plot(sessionnumbers, i.balanceovertime, marker='x')
    # TODO make it plot negative numbers, change scale of x, interactive????
    # plt.ylim(min(i.balanceovertime), max(i.balanceovertime))
    #
    # plt.xlabel("Session Number")
    # plt.ylabel("Balance")
    # plt.title(i.name)
    # plt.grid(True)
    #
    # plt.show()
