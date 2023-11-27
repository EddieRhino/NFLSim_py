from sim import *
import math

def calc_full_bet(a_ml,h_ml,overs,h_covers,a_covers,num_sims,h_wins,a_wins):
    aml_money = 0
    if(a_ml < 0):
        aml_money = ((((100/abs(a_ml))+1)*a_wins)-num_sims)/num_sims
    else:
        aml_money = ((((abs(a_ml)/100)+1)*a_wins)-num_sims)/num_sims

    hml_money = 0
    if(h_ml < 0):
        hml_money = ((((100/abs(h_ml))+1)*h_wins)-num_sims)/num_sims
    else:
        hml_money = ((((abs(h_ml)/100)+1)*h_wins)-num_sims)/num_sims

    overs_money = ((overs-(num_sims-overs))/num_sims)
    unders_money = ((num_sims-overs)-overs)/num_sims
    h_covers_money = (h_covers-a_covers)/num_sims
    a_covers_money = (a_covers-h_covers)/num_sims

    return [aml_money, hml_money, overs_money, unders_money, h_covers_money, a_covers_money]


def calc_full_bet_adv(a_ml,h_ml,overs,h_covers,a_covers,num_sims,h_wins,a_wins,hsml,asml,oml,uml):
    aml_money = 0
    if(a_ml < 0):
        aml_money = ((((100/abs(a_ml))+1)*a_wins)-num_sims)/num_sims
    else:
        aml_money = ((((abs(a_ml)/100)+1)*a_wins)-num_sims)/num_sims

    hml_money = 0
    if(h_ml < 0):
        hml_money = ((((100/abs(h_ml))+1)*h_wins)-num_sims)/num_sims
    else:
        hml_money = ((((abs(h_ml)/100)+1)*h_wins)-num_sims)/num_sims

    overs_money = ((((100/abs(oml))+1)*overs)-num_sims)/num_sims
    unders_money = ((((100/abs(uml))+1)*(1-overs))-num_sims)/num_sims
    h_covers_money = ((((100/abs(hsml))+1)*h_covers)-num_sims)/num_sims
    a_covers_money = ((((100/abs(asml))+1)*a_covers)-num_sims)/num_sims

    return [aml_money, hml_money, overs_money, unders_money, h_covers_money, a_covers_money]


def play_many_games_b(num,home,away):
    num_wins_home = 0
    num_wins_away = 0
    hpy = 0
    hry = 0
    apy = 0
    ary = 0
    scores = []
    yards_gained = []
    for x in range(num):
        h_score, a_score, hpy, hry, apy, ary = play_game(home,away)
        if(h_score > a_score):
            num_wins_home += 1
        else:
            num_wins_away += 1
        scores.append([h_score,a_score])
        yards_gained.append([hpy,hry,apy,ary])
    print("\nRESULTS:")
    print("Home team wins:", num_wins_home)
    print("Away team wins:", num_wins_away)
    print()

def play_many_games_bb(num,spread,home,away,ou):
    num_wins_home = 0
    num_wins_away = 0
    home_covers = 0
    pushes = 0
    overs = 0
    hpy = 0
    hry = 0
    apy = 0
    ary = 0
    scores = []
    yards_gained = []
    for x in range(num):
        h_score, a_score, hpy, hry, apy, ary = play_game(home,away)
        if(h_score > a_score):
            num_wins_home += 1
        else:
            num_wins_away += 1
        if(h_score + spread > a_score):
            home_covers += 1
        elif(h_score + spread == a_score):
            pushes += 1
        if(h_score + a_score > ou):
            overs += 1
        scores.append([h_score,a_score])
        yards_gained.append([hpy,hry,apy,ary])
    print("\nRESULTS:")
    print("Home team wins:", num_wins_home)
    print("Away team wins:", num_wins_away)
    print("Home team covers:", home_covers)
    if(pushes != 0):
        print("With",pushes,"pushes")
    print("Overs hit:",overs)
    count = False
    print("\nOPINION OF THIS SIM:")
    if(home_covers >= num*0.65):
        print("Bet Home Team Covering")
    elif(home_covers <= num*0.35):
        print("Bet Away Team Covering")
    else:
        count = True
    if(overs >= num*0.65):
        print("Bet Over")
    elif(overs <= num*0.35):
        print("Bet Under")
    elif(count):
        print("\nStay away from this game")
    print()








def play_many_games_bbm(num,spread,home,away,ou,risk):
    num_wins_home = 0
    num_wins_away = 0
    home_covers = 0
    pushes = 0
    overs = 0
    hpy = 0
    hry = 0
    apy = 0
    ary = 0
    scores = []
    yards_gained = []
    for x in range(num):
        h_score, a_score, hpy, hry, apy, ary = play_game(home,away)
        if(h_score > a_score):
            num_wins_home += 1
        else:
            num_wins_away += 1
        if(h_score + spread > a_score):
            home_covers += 1
        elif(h_score + spread == a_score):
            pushes += 1
        if(h_score + a_score > ou):
            overs += 1
        scores.append([h_score,a_score])
        yards_gained.append([hpy,hry,apy,ary])
    print("\nRESULTS:")
    print("Home team wins:", num_wins_home)
    print("Away team wins:", num_wins_away)
    print("Home team covers:", home_covers)
    if(pushes != 0):
        print("With",pushes,"pushes")
    print("Overs hit:",overs)
    count = False
    print("\nOPINION OF THIS SIM:")
    if(home_covers >= num*0.65):
        if(overs >= num*0.65):
            print("\nBet {money:.2f} on Home Team Covering".format(money=(risk*(home_covers/(home_covers+overs)))))
            print("\nBet {money:.2f} on Over".format(money=(risk*(overs/(home_covers+overs)))))
        elif(overs <= num*0.35):
            print("\nBet {money:.2f} on Home Team Covering".format(money=(risk*(home_covers/(home_covers+(1-overs))))))
            print("\nBet {money:.2f} on Over".format(money=(risk*((1-overs)/(home_covers+(1-overs))))))
        else:
            print("\nBet {money:.2f} on Home Team Covering".format(money=risk))
    elif(home_covers <= num*0.35):
        if(overs >= num*0.65):
            print("\nBet {money:.2f} on Away Team Covering".format(money=(risk*((1-home_covers)/((1-home_covers)+overs)))))
            print("\nBet {money:.2f} on Over".format(money=(risk*(overs/(home_covers+overs)))))
        elif(overs <= num*0.35):
            print("\nBet {money:.2f} on Away Team Covering".format(money=(risk*((1-home_covers)/((1-home_covers)+(1-overs))))))
            print("\nBet {money:.2f} on Over".format(money=(risk*((1-overs)/((1-home_covers)+(1-overs))))))
        else:
            print("\nBet {money:.2f} on Away Team Covering".format(money=risk))
    else:
        count = True
    if(overs >= num*0.65):
        print("\nBet {money:.2f} on Over".format(money=risk))
    elif(overs <= num*0.35):
        print("\nBet {money:.2f} on Under".format(money=risk))
    elif(count):
        print("\nStay away from this game")
        print("But if you want to bet no matter what, here is my choice:")
        if(home_covers > num-home_covers-pushes):
            if(overs > num-overs):
                print("\nBet {money:.2f} on Home Team Covering".format(money=(risk*(home_covers/(home_covers+overs)))))
                print("\nBet {money:.2f} on Over".format(money=(risk*(overs/(home_covers+overs)))))
            elif(overs == num-overs):
                print("Don't bet Over/Under")
                print("\nBet {money:.2f} on Home Team Covering".format(money=risk))
            else:
                print("\nBet {money:.2f} on Home Team Covering".format(money=(risk*(home_covers/(home_covers+(1-overs))))))
                print("\nBet {money:.2f} on Over".format(money=(risk*((1-overs)/(home_covers+(1-overs))))))
        elif(home_covers == num-home_covers-pushes):
            if(overs == num-overs):
                print("Run again, or just don't bet on this game :)")
            elif(overs > num-overs):
                print("Don't bet on the spread")
                print("Bet {money:.2f} on Over".format(money=risk))
            else:
                print("Don't bet on the spread")
                print("Bet {money:.2f} on Under".format(money=risk))
        else:
            if(overs > num-overs):
                print("\nBet {money:.2f} on Away Team Covering".format(money=(risk*((1-home_covers)/((1-home_covers)+overs)))))
                print("\nBet {money:.2f} on Over".format(money=(risk*(overs/((1-home_covers)+overs)))))
            elif(overs == num-overs):
                print("Don't bet Over/Under")
                print("\nBet {money:.2f} on Away Team Covering".format(money=risk))
            else:
                print("\nBet {money:.2f} on Away Team Covering".format(money=(risk*((1-home_covers)/((1-home_covers)+(1-overs))))))
                print("\nBet {money:.2f} on Under".format(money=(risk*((1-overs)/((1-home_covers)+(1-overs))))))

    print()



def play_many_games_ab(num,spread,home,away,ou,aml,hml):
    num_wins_home = 0
    num_wins_away = 0
    home_covers = 0
    pushes = 0
    overs = 0
    hpy = 0
    hry = 0
    apy = 0
    ary = 0
    scores = []
    yards_gained = []
    for x in range(num):
        h_score, a_score, hpy, hry, apy, ary = play_game(home,away)
        if(h_score > a_score):
            num_wins_home += 1
        else:
            num_wins_away += 1
        if(h_score + spread > a_score):
            home_covers += 1
        elif(h_score + spread == a_score):
            pushes += 1
        if(h_score + a_score > ou):
            overs += 1
        scores.append([h_score,a_score])
        yards_gained.append([hpy,hry,apy,ary])
    print("\nRESULTS:")
    print("Home team wins:", num_wins_home)
    print("Away team wins:", num_wins_away)
    print("Home team covers:", home_covers)
    if(pushes != 0):
        print("With",pushes,"pushes")
    print("Overs hit:",overs)
    count = 0
    print("\nOPINION OF THIS SIM:")
    if(home_covers >= num*0.65):
        print("\nBet Home Team Covering")
    elif(home_covers <= num*0.35):
        print("\nBet Away Team Covering")
    else:
        count += 1
    if(overs >= num*0.65):
        print("\nBet Over")
    elif(overs <= num*0.35):
        print("\nBet Under")
    a_ml_money = ((((100/abs(aml))+1)*num_wins_away)-num)
    h_ml_money = ((((100/abs(hml))+1)*num_wins_home)-num)
    if(a_ml_money >= num*0.1):
        print("Bet Away Moneyline")
    elif(h_ml_money >= num*0.1):
        print("Bet Home Moneyline")
    else:
        count += 1
    if(count == 2):
        print("\nStay away from this game")
    print()






def play_many_games_abm(num,spread,home,away,ou,risk,aml,hml):
    num_wins_home = 0
    num_wins_away = 0
    home_covers = 0
    pushes = 0
    overs = 0
    hpy = 0
    hry = 0
    apy = 0
    ary = 0
    scores = []
    yards_gained = []
    for x in range(num):
        h_score, a_score, hpy, hry, apy, ary = play_game(home,away)
        if(h_score > a_score):
            num_wins_home += 1
        else:
            num_wins_away += 1
        if(h_score + spread > a_score):
            home_covers += 1
        elif(h_score + spread == a_score):
            pushes += 1
        if(h_score + a_score > ou):
            overs += 1
        scores.append([h_score,a_score])
        yards_gained.append([hpy,hry,apy,ary])
    print("\nRESULTS:")
    print("Home team wins:", num_wins_home)
    print("Away team wins:", num_wins_away)
    print("Home team covers:", home_covers)
    if(pushes != 0):
        print("With",pushes,"pushes")
    print("Overs hit:",overs)
    count = 0
    money_vals = calc_full_bet(aml,hml,overs,home_covers,num-home_covers-pushes,num,num_wins_home,num_wins_away)
    print("\nAway Money Line earnings per game ($1 bet):",money_vals[0])
    print("Home Money Line earnings per game ($1 bet):",money_vals[1])
    print("Over earnings per game ($1 bet):",money_vals[2])
    print("Under earnings per game ($1 bet):",money_vals[3])
    print("Home Covering earnings per game ($1 bet):",money_vals[4])
    print("Away Covering earnings per game ($1 bet):",money_vals[5])
    print("\nOPINION OF THIS SIM:")
#[aml_money, hml_money, overs_money, unders_money, h_covers_money, a_covers_money]
    sum = 0
    for x in range(len(money_vals)):
        if(money_vals[x] >= 0.25):
            sum += money_vals[x]
    if(sum != 0):
        if(money_vals[0] >= 0.25):
                print("\nBet {money:.2f} on away money line".format(money = (risk*(money_vals[0]/sum))))
        if(money_vals[1] >= 0.25):
                print("\nBet {money:.2f} on home money line".format(money = (risk*(money_vals[1]/sum))))
        if(money_vals[2] >= 0.25):
                print("\nBet {money:.2f} on over".format(money = (risk*(money_vals[2]/sum))))
        if(money_vals[3] >= 0.25):
                print("\nBet {money:.2f} on under".format(money = (risk*(money_vals[3]/sum))))
        if(money_vals[4] >= 0.25):
                print("\nBet {money:.2f} on home team covering".format(money = (risk*(money_vals[4]/sum))))
        if(money_vals[5] >= 0.25):
                print("\nBet {money:.2f} on away team covering".format(money = (risk*(money_vals[5]/sum))))
    else:
        print("\nReally, you shouldn't bet on this game")


    print()















def play_many_games_fg(num,games):
    num_wins_home = 0
    num_wins_away = 0
    home_covers = 0
    pushes = 0
    overs = 0
    hpy = 0
    hry = 0
    apy = 0
    ary = 0
    scores = []
    yards_gained = []
    for x in range(num):
        h_score, a_score, hpy, hry, apy, ary = play_game(home,away)
        if(h_score > a_score):
            num_wins_home += 1
        else:
            num_wins_away += 1
        if(h_score + spread > a_score):
            home_covers += 1
        elif(h_score + spread == a_score):
            pushes += 1
        if(h_score + a_score > ou):
            overs += 1
        scores.append([h_score,a_score])
        yards_gained.append([hpy,hry,apy,ary])
    print("\nRESULTS:")
    print("Home team wins:", num_wins_home)
    print("Away team wins:", num_wins_away)
    print("Home team covers:", home_covers)
    if(pushes != 0):
        print("With",pushes,"pushes")
    print("Overs hit:",overs)
    count = 0
    print("\nOPINION OF THIS SIM:")
    if(home_covers >= num*0.65):
        print("\nBet Home Team Covering")
    elif(home_covers <= num*0.35):
        print("\nBet Away Team Covering")
    else:
        count += 1
    if(overs >= num*0.65):
        print("\nBet Over")
    elif(overs <= num*0.35):
        print("\nBet Under")
    a_ml_money = ((((100/abs(aml))+1)*num_wins_away)-num)
    h_ml_money = ((((100/abs(hml))+1)*num_wins_home)-num)
    if(a_ml_money >= num*0.1):
        print("Bet Away Moneyline")
    elif(h_ml_money >= num*0.1):
        print("Bet Home Moneyline")
    else:
        count += 1
    if(count == 2):
        print("\nStay away from this game")
    print()





#awayteam,hometeam,spread,home_spread_ml,away_spread_ml,ou,over_ml,under_ml,away_ml,home_ml
def play_many_games_fgm(num,games,risk):
    for y in range(len(games)):
        print("\n{awayteam}({a_ml}) AT {hometeam}({h_ml})({spread}) {ou}".format(
        awayteam = games[y][0],a_ml = games[y][8],hometeam = games[y][1],h_ml = games[y][9],
        spread = games[y][2],ou = games[y][5]))
        num_wins_home = 0
        num_wins_away = 0
        home_covers = 0
        pushes = 0
        overs = 0
        hpy = 0
        hry = 0
        apy = 0
        ary = 0
        spread = float(games[y][2])
        ou = float(games[y][5])
        aml = float(games[y][8])
        hml = float(games[y][9])
        money_vals = []
        for x in range(num):
            h_score, a_score, hpy, hry, apy, ary = play_game(games[y][1],games[y][0])
            if(h_score > a_score):
                num_wins_home += 1
            else:
                num_wins_away += 1
            if(h_score + spread > a_score):
                home_covers += 1
            elif(h_score + spread == a_score):
                pushes += 1
            if(h_score + a_score > ou):
                overs += 1
                #a_ml,h_ml,overs,h_covers,a_covers,num_sims,h_wins,a_wins,hsml,asml,oml,uml
        money_vals = (calc_full_bet_adv(aml,hml,overs,home_covers,num-home_covers-pushes,num,
        num_wins_home,num_wins_away,float(games[y][3]),float(games[y][4]),float(games[y][6]),float(games[y][7])))
    #[aml_money, hml_money, overs_money, unders_money, h_covers_money, a_covers_money]
        print("Overs hit:",overs)
        sum = 0
        for x in range(len(money_vals)):
            if(money_vals[x] >= 0.24):
                sum += money_vals[x]
        if(sum != 0):
            if(money_vals[0] >= 0.24):
                    print("Bet {money:.2f} on away money line".format(money = (risk*(money_vals[0]/sum))))
            if(money_vals[1] >= 0.24):
                    print("Bet {money:.2f} on home money line".format(money = (risk*(money_vals[1]/sum))))
            if(money_vals[2] >= 0.24):
                    print("Bet {money:.2f} on over".format(money = (risk*(money_vals[2]/sum))))
            if(money_vals[3] >= 0.24):
                    print("Bet {money:.2f} on under".format(money = (risk*(money_vals[3]/sum))))
            if(money_vals[4] >= 0.24):
                    print("Bet {money:.2f} on home team covering".format(money = (risk*(money_vals[4]/sum))))
            if(money_vals[5] >= 0.24):
                    print("Bet {money:.2f} on away team covering".format(money = (risk*(money_vals[5]/sum))))
        else:
            print("Ehh I'd stay away from this one")
