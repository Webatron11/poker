import re


def yninput(session, question, player):
    string = ""
    match question:
        case "players":
            string = "Is %s playing? (Y/N) "
        case "buyins":
            string = "Did %s buyin? (Y/N) "
        case "revbuyins":
            string = "Did %s reverse buyin? (Y/N) "

    x = True
    while x:
        yn = input(string % player.name).upper()
        match yn:
            case "Y":
                session.players.append(player.name)
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
        match = re.match(r"\d+\s*W\s*\d+\s*R\s*\d+\s*B\s*\d+\s*G", balancestring)
        if match is not None:
            vars(session)[playername] = balancestring
            x = False
        else:
            print("Invalid input.")
            x = True
