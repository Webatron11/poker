import re


def chipstobalance(chips: str):
    # Uses regex to separate inputted string into W, R, B, G, Bl, P chip counts and then creating a total balance
    regex = r'\d+\s*'

    matches = re.findall(regex, chips)
    formatted = []

    # Takes all matches from balance string and then strips them of whitespace

    for i in matches:
        formatted.append(int(i.strip()))

    # Takes the formatted matches and times them by their respective chip amounts for the end total

    try:
        balance = (formatted[0] * 1) + (formatted[1] * 5) + (formatted[2] * 10) + (formatted[3] * 25) + (formatted[4] * 100)
        return balance
    except IndexError:
        return 0


def yninput(session, question, player):
    string = ""
    buyin = None
    match question:
        case "buyins":
            string = "Did %s buyin? (Y/N) "
            buyin = True
        case "revbuyins":
            string = "Did %s reverse buyin? (Y/N) "
            buyin = False

    x = True
    while x:
        yn = input(string % player.name).upper()
        match yn:
            case "Y":
                match buyin:
                    # Takes buyin bool and takes number of buyins or reverse buyins. If neither, it just does normal
                    # stuff.
                    case None:
                        session.players.append(player.name)
                    case True:
                        num = int(input(f'How many times did {player.name} buyin? '))
                        for i in range(num):
                            session.buyins.append(player.name)
                    case False:
                        num = int(input(f'How many times did {player.name} reverse buyin? '))
                        for i in range(num):
                            session.revbuyins.append(player.name)
                
                x = False
            case "N":
                x = False
                continue
            case _:
                print("Invalid input")

    return yn


def balanceinput(session, playername):
    x = True
    while x:

        balancestring = input("What is %s's balance? " % playername).upper()

        match = re.match(
            r"(\d+\s+?W)+?\s+?(\d+\s+?R)+?\s+?(\d+\s+?B)+?\s+?(\d+\s+?G)+?\s+?(\d+\s+?B)",
            balancestring)

        if match is not None:
            session.balances[playername] = balancestring
            x = False
        else:
            print("Invalid input.")
            x = True


def checkrev(session):
    for player in session.players:
        balance = chipstobalance(session.balances[player])
        if balance >= 500:
            cnt = 1
            while True:
                if (balance - (200*cnt)) < 500:
                    print(f'{player} has had {cnt} reverse buy ins. Please remove the correct number of chips from their bag.')
                    break
                else:
                    cnt += 1
            for i in range(cnt):
                session.revbuyins.append(player)


def checkbuy(session):
    for player in session.players:
        if chipstobalance(session.balances[player]) <= 100:
            session.buyins.append(player)
            print(f'{player} has had 1 buy in. Please add the correct number of chips to their bag.')
