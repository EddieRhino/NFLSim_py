from read_csv import *
import random
#Player,Tm,Cmp,Att,CmpPct,Yds,TD,TDPct,Inter,InterPct,SuccPct,YPA,AYPA,YPC,YPG,Rate,QBR,Sk,SkYds,SkPct,NYPA,ANYPA
#  0     1  2   3    4     5  6    7     8     9        10     11  12   13  14  15  16  17  18     19    20  21
def play_game(home,away):
    home_team = []
    away_team = []
    home_pass_yards = 0
    away_pass_yards = 0
    home_run_yards = 0
    away_run_yards = 0
    for x in range(len(rowsQB)):
        if(rowsQB[x][1] == home):
            home_team.append(rowsQB[x])
            break
    for x in range(len(rowsRB)):
        if(rowsRB[x][1] == home):
            home_team.append(rowsRB[x])
            break

    # for x in range(len(rowsWRTE)):
    #     if(rowsWRTE[x][1] == home):
    #         home_team.append(rowsWRTE[x])

    for x in range(len(rowsQB)):
        if(rowsQB[x][1] == away):
            away_team.append(rowsQB[x])
            break
    for x in range(len(rowsRB)):
        if(rowsRB[x][1] == away):
            away_team.append(rowsRB[x])
            break

    # for x in range(len(rowsWRTE)):
    #     if(rowsWRTE[x][1] == away):
    #         away_team.append(rowsWRTE[x])

    for x in range(len(rowsOff)):
        if(rowsOff[x][0] == home):
            home_team.append(rowsOff[x])
            break

    for x in range(len(rowsOff)):
        if(rowsOff[x][0] == away):
            away_team.append(rowsOff[x])
            break

    for x in range(len(rowsPDef)):
        if(rowsPDef[x][0] == home):
            home_team.append(rowsPDef[x])
            break

    for x in range(len(rowsPDef)):
        if(rowsPDef[x][0] == away):
            away_team.append(rowsPDef[x])
            break

    for x in range(len(rowsRDef)):
        if(rowsRDef[x][0] == home):
            home_team.append(rowsRDef[x])
            break

    for x in range(len(rowsRDef)):
        if(rowsRDef[x][0] == away):
            away_team.append(rowsRDef[x])
            break
    if(len(home_team) != 5):
        print("Problem with home team adding")
    if(len(away_team) != 5):
        print("Problem with home team adding")
    home_cpct = (float(home_team[0][4]) + float(away_team[3][1]))/2
    away_cpct = (float(away_team[0][4]) + float(home_team[3][1]))/2
    home_ypp = (float(home_team[0][13]) + float(away_team[3][4]))/2
    away_ypp = (float(away_team[0][13]) + float(home_team[3][4]))/2
    home_ypr = (float(home_team[1][6]) + float(away_team[4][1]))/2
    away_ypr = (float(away_team[1][6]) + float(home_team[4][1]))/2
    home_sack = (float(home_team[0][19]) + float(away_team[3][6]))/2
    away_sack = (float(away_team[0][19]) + float(home_team[3][6]))/2
    home_int = (float(home_team[0][9]) + float(away_team[3][3]))/2
    away_int = (float(away_team[0][9]) + float(home_team[3][3]))/2

    def pass_play(team,yard,down,togo,time,pct,ypp,inter,sack):
        #Pass play called
        num1 = random.random()
        num2 = random.random()
        hasball = True
        if(num1*100 <= pct):
            # print("Pass complete\n")
            yards = 0
            time -= 40
            if(num2 <= 0.5):
                yards = random.randint(0,int(ypp))
            elif(num2 < (1-(float(home_team[0][7])/100))):
                yards = random.randint(int(ypp),30)
            else:
                yards = random.randint(30,100)
            # print("Gain of", yards, "yards\n")
            yard += yards
            togo -= yards
            if(togo <= 0):
                down = 1
                togo = 10
            else:
                down += 1
        else:
            if(num1 > 1-(inter/100)):
                # print("Pass intercepted\n")
                hasball = False
                time -= 10
                yard = 100-yard
            elif(num1 > 1-(inter/100)-(sack/100)):
                # print("Sacked")
                yard -= 5
                down += 1
                togo += 5
                time -= 40
            else:
                # print("Pass incomplete\n")
                time -= 10
                down += 1
        return hasball, yard, down, togo, time

    def run_play(team,yard,down,togo,time,ypr):
        # print("Run Play")
        num1 = random.random()
        num2 = random.random()
        hasball = True
        yards = 0
        if(num1 <= 0.7):
            yards = random.randint(-1,int(ypr))
            time -= 50
            yard += yards
            togo -= yards
            if(togo <= 0):
                down = 1
                togo = 10
            else:
                down += 1
        else:
            if((int(team[1][8]) < 2) and (num1 >= 0.98)):
                # print("Fumble")
                hasball = False
                time -= 10
                yard = 100-yard
            elif((int(team[1][8]) < 4) and (num1 >= 0.96)):
                # print("Fumble")
                hasball = False
                time -= 10
                yard = 100-yard
            elif((int(team[1][8]) < 6) and (num1 >= 0.94)):
                # print("Fumble")
                hasball = False
                time -= 10
                yard = 100-yard
            elif((int(team[1][8]) >= 6) and (num1 >= 0.92)):
                # print("Fumble")
                hasball = False
                time -= 10
                yard = 100-yard
            else:
                yards = random.randint(int(float(team[1][6])),40)
                time -= 50
                yard += yards
                togo -= yards
                if(togo <= 0):
                    down = 1
                    togo = 10
                else:
                    down += 1
        return hasball, yard, down, togo, time

    def field_goal_attempt(yard):
        if(yardline >= 90):
            if(random.random() <= 0.98):
                return True
            else:
                return False
        elif(yardline >= 80):
            if(random.random() <= 0.95):
                return True
            else:
                return False
        elif(yardline >= 70):
            if(random.random() <= 0.85):
                return True
            else:
                return False
        elif(yardline >= 60):
            if(random.random() <= 0.67):
                return True
            else:
                return False



    home_score = 0
    away_score = 0
    time_left = 1800
    down = 1
    yardline = 25
    yardsleft = 10
    yardline2 = 25
    secondHalf = False
    # print("\n")
    while(True):
        if(time_left <= 0 and secondHalf == True):
            break
        down = 1
        yardsleft = 10
        # print(home, "has the ball\n")
        #print("{minutes}:{seconds} left in the half\n".format(minutes = time_left//60,seconds = time_left%60))


        #HOME TEAM OFFENSE


        while(True):
            if(time_left == 1800 and secondHalf == True):
                break
            if(time_left <= 0):
                secondHalf = True
                time_left = 1800
                break
            if(down == 1 and (100-yardline < yardsleft)):
                yardsleft = 100-yardline
            # print("Down:", down, "and", yardsleft,"to go.\n")
            # if(yardline > 50):
            #     yardline2 = 50-(yardline-50)
            #     print("On the opposing", yardline2, "yard line\n")
            # else:
            #     print("On own", yardline, "yard line\n")
            num2 = random.random()
            if(time_left <= 10 and yardline >= 60):
                if(field_goal_attempt(yardline)):
                    home_score += 3
                    yardline = 25
                time_left = 1800
                secondHalf = True
                break
            elif(down == 4 and yardline >= 60):
                # print("Field Goal attempt\n")
                if(field_goal_attempt(yardline)):
                    home_score += 3
                    yardline = 25
                    time_left -= 5
                    # print("Field Goal made\n")
                    break
                else:
                    yardline = 100-yardline
                    time_left -= 5
                    break

                # print("SCORE\n",home," ",home_score,"\n",away," ",away_score)
            elif(down == 4):
                # print("Punted\n")
                time_left -= 10
                # print("SCORE\n",home," ",home_score,"\n",away," ",away_score,"\n")
                yardline = yardline + 50
                if(yardline >= 100):
                    yardline = 20
                else:
                    yardline = 100-yardline
                break

            elif(down == 1 and random.random() < (float(home_team[2][1])-20)/100):
                temp = yardline
                a,yardline,down,yardsleft,time_left = pass_play(home_team,yardline,down,yardsleft,time_left,
                home_cpct,home_ypp,home_int,home_sack)
                if(a):
                    home_pass_yards += (yardline - temp)
            elif(down == 1):
                temp = yardline
                a,yardline,down,yardsleft,time_left = run_play(home_team,yardline,down,yardsleft,time_left,home_ypr)
                if(a):
                    home_run_yards += (yardline - temp)
            elif(yardsleft <= 1 and home == "PHI"): #Gotta account for the Eagles QB sneak
                yardline += 2
                down = 1
                yardsleft = 10
                time_left -= 40
                home_run_yards += 2
            elif(down == 2 and yardsleft > 7 and random.random() < ((float(home_team[2][1])+15)/100)):
                temp = yardline
                a,yardline,down,yardsleft,time_left = pass_play(home_team,yardline,down,yardsleft,time_left,
                home_cpct,home_ypp,home_int,home_sack)
                if(a):
                    home_pass_yards += (yardline - temp)
            elif(down == 2 and yardsleft > 7):
                temp = yardline
                a,yardline,down,yardsleft,time_left = run_play(home_team,yardline,down,yardsleft,time_left,home_ypr)
                if(a):
                    home_run_yards += (yardline - temp)
            elif(down == 2 and yardsleft > 3 and random.random() < ((float(home_team[2][1])-10)/100)):
                temp = yardline
                a,yardline,down,yardsleft,time_left = pass_play(home_team,yardline,down,yardsleft,time_left,
                home_cpct,home_ypp,home_int,home_sack)
                if(a):
                    home_pass_yards += (yardline - temp)
            elif(down == 2 and yardsleft > 3):
                temp = yardline
                a,yardline,down,yardsleft,time_left = run_play(home_team,yardline,down,yardsleft,time_left,home_ypr)
                if(a):
                    home_run_yards += (yardline - temp)
            elif(down == 2 and random.random() < ((float(home_team[2][1])-15)/100)):
                temp = yardline
                a,yardline,down,yardsleft,time_left = pass_play(home_team,yardline,down,yardsleft,time_left,
                home_cpct,home_ypp,home_int,home_sack)
                if(a):
                    home_pass_yards += (yardline - temp)
            elif(down == 2):
                temp = yardline
                a,yardline,down,yardsleft,time_left = run_play(home_team,yardline,down,yardsleft,time_left,home_ypr)
                if(a):
                    home_run_yards += (yardline - temp)
            elif(down == 3 and yardsleft > 7 and random.random() < ((float(home_team[2][1])+35)/100)):
                temp = yardline
                a,yardline,down,yardsleft,time_left = pass_play(home_team,yardline,down,yardsleft,time_left,
                home_cpct,home_ypp,home_int,home_sack)
                if(a):
                    home_pass_yards += (yardline - temp)
            elif(down == 3 and yardsleft > 7):
                temp = yardline
                a,yardline,down,yardsleft,time_left = run_play(home_team,yardline,down,yardsleft,time_left,home_ypr)
                if(a):
                    home_run_yards += (yardline - temp)
            elif(down == 3 and yardsleft > 3 and random.random() < ((float(home_team[2][1])+15)/100)):
                temp = yardline
                a,yardline,down,yardsleft,time_left = pass_play(home_team,yardline,down,yardsleft,time_left,
                home_cpct,home_ypp,home_int,home_sack)
                if(a):
                    home_pass_yards += (yardline - temp)
            elif(down == 3 and yardsleft > 3):
                temp = yardline
                a,yardline,down,yardsleft,time_left = run_play(home_team,yardline,down,yardsleft,time_left,home_ypr)
                if(a):
                    home_run_yards += (yardline - temp)
            elif(down == 3 and random.random() < ((float(home_team[2][1])-7)/100)):
                temp = yardline
                a,yardline,down,yardsleft,time_left = pass_play(home_team,yardline,down,yardsleft,time_left,
                home_cpct,home_ypp,home_int,home_sack)
                if(a):
                    home_pass_yards += (yardline - temp)
            elif(down == 3):
                temp = yardline
                a,yardline,down,yardsleft,time_left = run_play(home_team,yardline,down,yardsleft,time_left,home_ypr)
                if(a):
                    home_run_yards += (yardline - temp)






            if(yardline <= 0):
                # print("Safety")
                away_score += 2
                break
            if(a == False):
                # print("SCORE\n",home," ",home_score,"\n",away," ",away_score,"\n")
                break
            if(yardline >= 100):
                # print("TOUCHDOWN!\n")
                home_score += 6
                if(random.random() <= 0.95):
                    home_score += 1
                # print("SCORE\n",home," ",home_score,"\n",away," ",away_score,"\n")
                yardline = 25
                break



#AWAY TEAM OFFENSE


        down = 1
        yardsleft = 10
        if(time_left <= 0 and secondHalf == True):
            break
        elif(time_left <= 0):
            secondHalf = True
            time_left = 1800
        # print(away, "has the ball\n")
        #print("{minutes}:{seconds} left in the half\n".format(minutes = time_left//60,seconds = time_left%60))
        while(True):
            if(down == 1 and (100-yardline < yardsleft)):
                yardsleft = 100-yardline
            # print("Down:", down, "and", yardsleft,"to go.\n")
            # if(yardline > 50):
            #     yardline2 = 50-(yardline-50)
            #     print("On the opposing", yardline2, "yard line\n")
            # else:
            #     print("On own", yardline, "yard line\n")
            num1 = random.random()
            num2 = random.random()
            if(time_left <= 10 and yardline >= 60):
                if(field_goal_attempt(yardline)):
                    away_score += 3
                    yardline = 25
                time_left -= 10
                secondHalf = True
                break
            elif(down == 4 and yardline >= 65):
                # print("Field Goal attempt\n")
                if(field_goal_attempt(yardline)):
                    away_score += 3
                    yardline = 25
                    time_left -= 10
                    # print("Field Goal made\n")
                    break
                else:
                    yardline = 100-yardline
                    time_left -= 10
                    break
                # print("SCORE\n",home," ",home_score,"\n",away," ",away_score,"\n")
            elif(down == 4):
                # print("Punted\n")
                # print("SCORE\n",home," ",home_score,"\n",away," ",away_score,"\n")
                yardline = yardline + 50
                time_left -= 10
                if(yardline >= 100):
                    yardline = 20
                else:
                    yardline = 100-yardline
                break
            elif(down == 1 and random.random() < (float(away_team[2][1])-20)/100):
                temp = yardline
                a,yardline,down,yardsleft,time_left = pass_play(away_team,yardline,down,yardsleft,time_left,
                away_cpct,away_ypp,away_int,away_sack)
                if(a):
                    away_pass_yards += (yardline - temp)
            elif(down == 1):
                temp = yardline
                a,yardline,down,yardsleft,time_left = run_play(away_team,yardline,down,yardsleft,time_left,away_ypr)
                if(a):
                    away_run_yards += (yardline - temp)
            elif(yardsleft <= 1 and away == "PHI"): #Gotta account for the Eagles QB sneak
                yardline += 2
                down = 1
                yardsleft = 10
                time_left -= 40
                away_run_yards += 2
            elif(down == 2 and yardsleft > 7 and random.random() < ((float(away_team[2][1])+15)/100)):
                temp = yardline
                a,yardline,down,yardsleft,time_left = pass_play(away_team,yardline,down,yardsleft,time_left,
                away_cpct,away_ypp,away_int,away_sack)
                if(a):
                    away_pass_yards += (yardline - temp)
            elif(down == 2 and yardsleft > 7):
                temp = yardline
                a,yardline,down,yardsleft,time_left = run_play(away_team,yardline,down,yardsleft,time_left,away_ypr)
                if(a):
                    away_run_yards += (yardline - temp)
            elif(down == 2 and yardsleft > 3 and random.random() < ((float(away_team[2][1])-10)/100)):
                temp = yardline
                a,yardline,down,yardsleft,time_left = pass_play(away_team,yardline,down,yardsleft,time_left,
                away_cpct,away_ypp,away_int,away_sack)
                if(a):
                    away_pass_yards += (yardline - temp)
            elif(down == 2 and yardsleft > 3):
                temp = yardline
                a,yardline,down,yardsleft,time_left = run_play(away_team,yardline,down,yardsleft,time_left,away_ypr)
                if(a):
                    away_run_yards += (yardline - temp)
            elif(down == 2 and random.random() < ((float(away_team[2][1])-15)/100)):
                temp = yardline
                a,yardline,down,yardsleft,time_left = pass_play(away_team,yardline,down,yardsleft,time_left,
                away_cpct,away_ypp,away_int,away_sack)
                if(a):
                    away_pass_yards += (yardline - temp)
            elif(down == 2):
                temp = yardline
                a,yardline,down,yardsleft,time_left = run_play(away_team,yardline,down,yardsleft,time_left,away_ypr)
                if(a):
                    away_run_yards += (yardline - temp)
            elif(down == 3 and yardsleft > 7 and random.random() < ((float(away_team[2][1])+35)/100)):
                temp = yardline
                a,yardline,down,yardsleft,time_left = pass_play(away_team,yardline,down,yardsleft,time_left,
                away_cpct,away_ypp,away_int,away_sack)
                if(a):
                    away_pass_yards += (yardline - temp)
            elif(down == 3 and yardsleft > 7):
                temp = yardline
                a,yardline,down,yardsleft,time_left = run_play(away_team,yardline,down,yardsleft,time_left,away_ypr)
                if(a):
                    away_run_yards += (yardline - temp)
            elif(down == 3 and yardsleft > 3 and random.random() < ((float(away_team[2][1])+15)/100)):
                temp = yardline
                a,yardline,down,yardsleft,time_left = pass_play(away_team,yardline,down,yardsleft,time_left,
                away_cpct,away_ypp,away_int,away_sack)
                if(a):
                    away_pass_yards += (yardline - temp)
            elif(down == 3 and yardsleft > 3):
                temp = yardline
                a,yardline,down,yardsleft,time_left = run_play(away_team,yardline,down,yardsleft,time_left,away_ypr)
                if(a):
                    away_run_yards += (yardline - temp)
            elif(down == 3 and random.random() < ((float(away_team[2][1])-7)/100)):
                temp = yardline
                a,yardline,down,yardsleft,time_left = pass_play(away_team,yardline,down,yardsleft,time_left,
                away_cpct,away_ypp,away_int,away_sack)
                if(a):
                    away_pass_yards += (yardline - temp)
            elif(down == 3):
                temp = yardline
                a,yardline,down,yardsleft,time_left = run_play(away_team,yardline,down,yardsleft,time_left,away_ypr)
                if(a):
                    away_run_yards += (yardline - temp)

            if(a == False):
                # print("SCORE\n",home," ",home_score,"\n",away," ",away_score,"\n")
                break
            if(yardline <= 0):
                # print("Safety")
                home_score += 2
                break
            if(yardline >= 100):
                # print("TOUCHDOWN!\n")
                away_score += 6
                if(random.random() <= 0.95):
                    away_score += 1
                # print("SCORE\n",home," ",home_score,"\n",away," ",away_score,"\n")
                yardline = 25
                break
    # print("FINAL SCORE\n",home," ",home_score,"\n",away," ",away_score,"\n")
    if(home_score == away_score):
        if(random.random() >= 0.5):
            home_score += 3
        else:
            away_score += 3
    return home_score,away_score,home_pass_yards,home_run_yards,away_pass_yards,away_run_yards
