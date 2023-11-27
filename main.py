from output import *
import csv


filenameGames = "games.csv"
fieldsGames = []
rowsGames = []
with open(filenameGames, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fieldsGames = next(csvreader)
    for row in csvreader:
        rowsGames.append(row)





def main():
    print("\nWELCOME TO EDDIE'S NFL SIMULATOR!\n")
    while(True):
        responses = ["Basic","Basic Betting","Advanced Betting","Full Games"]
        print("Basic is just sim with no betting")
        print("Basic Betting is the sim with the spread and over/under")
        print("Advanced Betting is basic betting with moneyline included")
        print("Full Games gives you advanced betting but simulates all games")
        response = input("What mode do you want to use? (Basic, Basic Betting, Advanced Betting, Full Games) ")
        if(response in responses):
            break
        print("Invalid response, try again")
    if(response == "Full Games"):
        money = float(input("How much money do you want to risk? (Enter 0 if you don't want to use this feature): "))
        num_times = int(input("How many times do you want the teams to play? "))
        if(money == 0):
            play_many_games_fg(num_times,rowsGames)
        else:
            play_many_games_fgm(num_times,rowsGames,money)
    else:
        while(True):
            print(teams)
            team1 = input("Who should be the home team? (3 letter abbreviation): ")
            if(team1 in teams):
                break
            print("Incorrect abbreviation, try again")
        while(True):
            team2 = input("Who should be the away team? (3 letter abbreviation): ")
            if(team2 in teams):
                break
            print("Incorrect abbreviation, try again")
        num_times = int(input("How many times do you want the teams to play? "))
        if(response == "Basic Betting"):
            money = float(input("How much money do you want to risk? (Enter 0 if you don't want to use this feature): "))
            spread = float(input("What is the spread relative to the home team? "))
            points = float(input("What is the over/under of the game? "))
            if(money == 0):
                play_many_games_bb(num_times,spread,team1,team2,points)
            else:
                play_many_games_bbm(num_times,spread,team1,team2,points,money)
        elif(response == "Advanced Betting"):
            money = float(input("How much money do you want to risk? (Enter 0 if you don't want to use this feature): "))
            spread = float(input("What is the spread relative to the home team? "))
            points = float(input("What is the over/under of the game? "))
            a_ml = int(input("What is the moneyline of the away team? "))
            h_ml = int(input("What is the moneyline of the home team? "))
            if(money == 0):
                play_many_games_ab(num_times,spread,team1,team2,points,a_ml,h_ml)
            else:
                play_many_games_abm(num_times,spread,team1,team2,points,money,a_ml,h_ml)
        else:
            play_many_games_b(num_times,team1,team2)




if __name__ == '__main__':
    main()
