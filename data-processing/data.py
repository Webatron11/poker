

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
