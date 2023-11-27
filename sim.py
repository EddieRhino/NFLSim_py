from read_csv import *
import random
#Player,Tm,Cmp,Att,CmpPct,Yds,TD,TDPct,Inter,InterPct,SuccPct,YPA,AYPA,YPC,YPG,Rate,QBR,Sk,SkYds,SkPct,NYPA,ANYPA
#  0     1  2   3    4     5  6    7     8     9        10     11  12   13  14  15  16  17  18     19    20  21
def play_game(home,away):
    #Initializing variables for stats and team array
    home_team = []
    away_team = []
    home_pass_yards = 0
    away_pass_yards = 0
    home_run_yards = 0
    away_run_yards = 0

    #Append onto the teams arrays the necessary players and stats
    
    for x in range(len(rowsQB)):
        if(rowsQB[x][1] == home):
            home_team.append(rowsQB[x])
            break
    for x in range(len(rowsRB)):
        if(rowsRB[x][1] == home):
            home_team.append(rowsRB[x])
            break

    for x in range(len(rowsQB)):
        if(rowsQB[x][1] == away):
            away_team.append(rowsQB[x])
            break
    for x in range(len(rowsRB)):
        if(rowsRB[x][1] == away):
            away_team.append(rowsRB[x])
            break

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

    #Error checking for adding
    if(len(home_team) != 5):
        print("Problem with home team adding")
    if(len(away_team) != 5):
        print("Problem with home team adding")


    #Creating values for simulation that takes into account defense and offense
    home_cpct = (float(home_team[0][4]) + float(away_team[3][1]))/2 #home adjusted comp percent
    away_cpct = (float(away_team[0][4]) + float(home_team[3][1]))/2 #away adjusted comp percent
    home_ypp = (float(home_team[0][13]) + float(away_team[3][4]))/2 #home adjusted yards per pass
    away_ypp = (float(away_team[0][13]) + float(home_team[3][4]))/2 #away adjusted yards per pass
    home_ypr = (float(home_team[1][6]) + float(away_team[4][1]))/2 #home adjusted yards per rush
    away_ypr = (float(away_team[1][6]) + float(home_team[4][1]))/2 #away adjusted yards per rush
    home_sack = (float(home_team[0][19]) + float(away_team[3][6]))/2 #home adjusted sack percentage
    away_sack = (float(away_team[0][19]) + float(home_team[3][6]))/2 #away adjusted sack percentage
    home_int = (float(home_team[0][9]) + float(away_team[3][3]))/2 #home adjusted interception percentage
    away_int = (float(away_team[0][9]) + float(home_team[3][3]))/2 #away adjusted interception percentage

    def pass_play(team,yard,down,togo,time,pct,ypp,inter,sack):
        #Pass play called
        num1 = random.random()
        num2 = random.random()
        hasball = True
        if(num1*100 <= pct):
            #Pass completed
            yards = 0
            time -= 40
            if(num2 <= 0.5):
                #Short pass
                yards = random.randint(0,int(ypp))
            elif(num2 < (1-(float(home_team[0][7])/100))):
                #Medium pass
                yards = random.randint(int(ypp),30)
            else:
                #Long pass
                yards = random.randint(30,100)
                
            yard += yards
            togo -= yards
            if(togo <= 0): #Check if first down
                down = 1
                togo = 10
            else: 
                down += 1
        else:
            if(num1 > 1-(inter/100)):
                #Pass intercepted
                hasball = False
                time -= 10
                yard = 100-yard
            elif(num1 > 1-(inter/100)-(sack/100)):
                # QB sacked
                yard -= 5
                down += 1
                togo += 5
                time -= 40
            else:
                #Pass incomplete
                time -= 10
                down += 1
                
        return hasball, yard, down, togo, time

    def run_play(team,yard,down,togo,time,ypr):
        #Run play
        num1 = random.random()
        num2 = random.random()
        hasball = True
        yards = 0
        if(num1 <= 0.7):
            #Short/average run
            yards = random.randint(-1,int(ypr))
            time -= 50
            yard += yards
            togo -= yards
            if(togo <= 0): #Check if first down
                down = 1
                togo = 10
            else:
                down += 1
        else:
            if((int(team[1][8]) < 2) and (num1 >= 0.98)):
                #Fumble for non fumble prone RB
                hasball = False
                time -= 10
                yard = 100-yard
            elif((int(team[1][8]) < 4) and (num1 >= 0.96)):
                #Fumble for not very fumble prone RB
                hasball = False
                time -= 10
                yard = 100-yard
            elif((int(team[1][8]) < 6) and (num1 >= 0.94)):
                #Fumble for somewhat fumble prone RB
                hasball = False
                time -= 10
                yard = 100-yard
            elif((int(team[1][8]) >= 6) and (num1 >= 0.92)):
                #Fumble for sorta fumble prone RB
                hasball = False
                time -= 10
                yard = 100-yard
            else:
                #Long run
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
            #0-27 Yard FG
            if(random.random() <= 0.98):
                return True
            else:
                return False
        elif(yardline >= 80):
            #28-37 Yard FG
            if(random.random() <= 0.95):
                return True
            else:
                return False
        elif(yardline >= 70):
            #38-47 Yard FG
            if(random.random() <= 0.85):
                return True
            else:
                return False
        elif(yardline >= 60):
            #48-57 Yard FG
            if(random.random() <= 0.67):
                return True
            else:
                return False


    #Initializing variables necessary for the sim
    home_score = 0
    away_score = 0
    time_left = 1800
    down = 1
    yardline = 25
    yardsleft = 10
    yardline2 = 25
    secondHalf = False

    while(True):
        if(time_left <= 0 and secondHalf == True):
            #Check if game is over
            break
        #initialize the down and distance
        down = 1
        yardsleft = 10


        #HOME TEAM OFFENSE


        while(True):
            if(time_left == 1800 and secondHalf == True):
                #Check if it is after half and away team should have ball
                break
            if(time_left <= 0):
                #Check if it is halftime
                secondHalf = True
                time_left = 1800
                break
            if(down == 1 and (100-yardline < yardsleft)):
                #Check if it's a goal to go situation
                yardsleft = 100-yardline

            if(time_left <= 10 and yardline >= 60):
                #Buzzer beater field goal
                if(field_goal_attempt(yardline)):
                    home_score += 3
                    yardline = 25
                time_left = 1800
                secondHalf = True
                break
            elif(down == 4 and yardline >= 60):
                #4th down field goal attempt
                if(field_goal_attempt(yardline)):
                    home_score += 3
                    yardline = 25
                    time_left -= 5
                    #Made field goal
                    break
                else:
                    #Switch possession
                    yardline = 100-yardline
                    time_left -= 5
                    break

            elif(down == 4):
                #Punt
                time_left -= 10
                yardline = yardline + 50
                if(yardline >= 100):
                    #Touchback
                    yardline = 20
                else:
                    yardline = 100-yardline
                break

            #First down pass/run selection 
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
            elif(yardsleft <= 1 and home == "PHI"): #Gotta account for the Eagles Tush Push
                yardline += 2
                down = 1
                yardsleft = 10
                time_left -= 40
                home_run_yards += 2

            #Second down pass/run selection based on yards left and offense tendencies
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

            #3rd down pass/run selection based on yards left and offense tendencies
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
                #Safety
                away_score += 2
                break
            if(a == False):
                #Turnover
                break
            if(yardline >= 100):
                #Touchdown
                home_score += 6
                if(random.random() <= 0.95):
                    #Extra point
                    home_score += 1
                yardline = 25
                break



#AWAY TEAM OFFENSE
#Same procedure as above just with the away team


        down = 1
        yardsleft = 10
        if(time_left <= 0 and secondHalf == True):
            break
        elif(time_left <= 0):
            secondHalf = True
            time_left = 1800
        while(True):
            if(down == 1 and (100-yardline < yardsleft)):
                yardsleft = 100-yardline
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
                if(field_goal_attempt(yardline)):
                    away_score += 3
                    yardline = 25
                    time_left -= 10
                    break
                else:
                    yardline = 100-yardline
                    time_left -= 10
                    break
            elif(down == 4):
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
                break
            if(yardline <= 0):
                home_score += 2
                break
            if(yardline >= 100):
                away_score += 6
                if(random.random() <= 0.95):
                    away_score += 1
                yardline = 25
                break

    if(home_score == away_score):
        #Overtime, random for now
        #TODO: Implement overtime
        if(random.random() >= 0.5):
            home_score += 3
        else:
            away_score += 3
    return home_score,away_score,home_pass_yards,home_run_yards,away_pass_yards,away_run_yards
