from sqlite3 import connect


class Player:
    def __init__(self, name, balance, buyins, revbuyins, balanceovertime, profitovertime):
        self.name = name  # Name of player
        self.balance = balance  # Balance of player
        self.buyins = buyins  # Contains a int which is the total number of buyins for the player
        self.revbuyins = revbuyins  # Contains an int which is the total number of revbuyins for the player
        self.balanceovertime = balanceovertime  # Contains an array which contains the player's balance overtime
        self.profitovertime = profitovertime  # Contains an array which contains the player's profit over time. This is calculated from their rev/buyins for the session


class Session:
    def __init__(self, number, players, buyins, revbuyins, balances):
        self.number = number  # Contains an int which is used for the chart later (In the database this is a date)
        self.players = players  # Contains a string of players who participated in that session
        self.buyins = buyins  # Contains a string which has one name per buyin in that session
        self.revbuyins = revbuyins  # Contains a string which has one name per revbuyin in that session
        self.balances = balances  # Contains the player's balances.


# Fetches column names from the database and then creates X number of players based off the number of player columns
# in the database

# Connects to the poker db file
conn = connect('database.db')
cur = conn.cursor()

columns = cur.execute("PRAGMA table_info(poker)")  # Fetches the column names from the table 'poker'
columns = columns.fetchall()  # Takes the request to the db and converts the response into an array of tuples
columns = columns[4:]  # Trims list to the player names. 0:4 is date, players, buyins, revbuyins

conn.close()  # Closes the database connection

# Initialises the players array from the array of column names gathered earlier.
players = []
for i in columns:
    players.append(Player(i[1].title(), 0, 0, 0, [], []))

balances = dict.fromkeys([i.name for i in players])  # Creates a dictionary with the names of all players in the array
