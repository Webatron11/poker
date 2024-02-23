

class Player:
    def __init__(self, name: str, balance: int, buyins: float, revbuyins: int, balanceovertime: list, profitovertime: list):
        self.name = name
        self.balance = balance
        self.buyins = buyins
        self.revbuyins = revbuyins
        self.balanceovertime = balanceovertime
        self.profitovertime = profitovertime


class Session:
    def __init__(self, number, players, buyins, revbuyins, oscar, mitchell, xavier, ben, aidan, hunter, cooper):
        self.number = number
        self.players = players
        self.buyins = buyins
        self.revbuyins = revbuyins
        self.oscar = oscar
        self.mitchell = mitchell
        self.xavier = xavier
        self.ben = ben
        self.aidan = aidan
        self.hunter = hunter
        self.cooper = cooper


# Player initialisation.

aidan = Player("Aidan", 0, 0, 0, [], [])
ben = Player("Ben", 0, 0, 0, [], [])
cooper = Player("Cooper", 0, 0, 0, [], [])
hunter = Player("Hunter", 0, 0, 0, [], [])
mitchell = Player("Mitchell", 0, 0, 0, [], [])
oscar = Player("Oscar", 0, 0, 0, [], [])
xavier = Player("Xavier", 0, 0, 0, [], [])

# Array of players in order to index through all players.

players = [aidan, ben, cooper, hunter, mitchell, oscar, xavier]
