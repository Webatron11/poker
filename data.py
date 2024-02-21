class Player:
    def __init__(self, name, balance, buyins, revbuyins):
        self.name = name
        self.balance = balance
        self.buyin = buyins
        self.revbuyings = revbuyins


class Session:
    def __init__(self, number, players, buyins, revbuyins, oscar, mitchell, xavier, ben, aidan, hunter, cooper):
        self.number = number
        self.players = players
        self.buyins = buyins
        self.revbuyings = revbuyins
        self.oscar = oscar
        self.mitchell = mitchell
        self.xavier = xavier
        self.ben = ben
        self.aidan = aidan
        self.hunter = hunter
        self.cooper = cooper
