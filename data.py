from sqlite3 import connect


class Player:
    def __init__(self, name, balance, buyins, revbuyins, balanceovertime, profitovertime):
        self.name = name
        self.balance = balance
        self.buyins = buyins
        self.revbuyins = revbuyins
        self.balanceovertime = balanceovertime
        self.profitovertime = profitovertime


class Session:
    def __init__(self, number, players, buyins, revbuyins, balances):
        self.number = number
        self.players = players
        self.buyins = buyins
        self.revbuyins = revbuyins
        self.balances = balances


conn = connect('poker.db')
cur = conn.cursor()

columns = cur.execute("SELECT name FROM PRAGMA_TABLE_INFO('poker')")

print(columns)

players = []
for i in columns:
    players.append(Player(i, 0, 0, 0, [], []))

print(players)

# Player initialisation.

# aidan = Player("Aidan", 0, 0, 0, [], [])
# ben = Player("Ben", 0, 0, 0, [], [])
# cooper = Player("Cooper", 0, 0, 0, [], [])
# hunter = Player("Hunter", 0, 0, 0, [], [])
# mitchell = Player("Mitchell", 0, 0, 0, [], [])
# oscar = Player("Oscar", 0, 0, 0, [], [])
# xavier = Player("Xavier", 0, 0, 0, [], [])
#
# # Array of players in order to index through all players.
#
# players = [aidan, ben, cooper, hunter, mitchell, oscar, xavier]
