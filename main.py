import csv
from data import *

aidan = Player("Aidan", 0, 0, 0)
ben = Player("Ben", 0, 0, 0)
cooper = Player("Cooper", 0, 0, 0)
hunter = Player("Hunter", 0, 0, 0)
mitchell = Player("Mitchell", 0, 0, 0)
oscar = Player("Oscar", 0, 0, 0)
xavier = Player("Xavier", 0, 0, 0)

sessions = []

csv_read = ''
with open('Poker.csv') as f:
    csv_read = csv.reader(f, delimiter=',')

    next(csv_read)

    form_information = []
    i = 1
    for row in csv_read:
        session = Session(i, row[1].split(';'), row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[10], row[11])
        form_information.append(session)
        i += 1

print(form_information)

for session in form_information:
