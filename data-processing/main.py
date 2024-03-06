import matplotlib.pyplot as plt
from functions import *

sessions = []

conn = connect('database.db')
cur = conn.cursor()

# Reads db file and parses the information into an array of the Session type.

for row in cur.execute('SELECT * FROM poker ORDER BY date'):
    for balance in row[4:]:
        for player in players:
            balances[player] = balance

    i = 1

    session = Session(i, row[1].split(','), row[2].split(','), row[3].split(','), balances)
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
