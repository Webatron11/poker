import re


def yninput(session, question, player):
    string = ""
    match question:
        case "players":
            string = "Is %s playing? (Y/N) "
            buyin = None
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
            r"(\d+\s+?W)+?\s+?(\d+\s+?R)+?\s+?(\d+\s+?B)+?\s+?(\d+\s+?G)+?\s+?(\d+\s+?B)+?\s+?(\d+\s+?P)",
            balancestring)

        if match is not None:
            session.balances[playername] = balancestring
            x = False
        else:
            print("Invalid input.")
            x = True
