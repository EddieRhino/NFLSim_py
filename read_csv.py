import csv
teams = ["MIN","DET","GNB","CHI","DAL","PHI","WAS","NYG","ATL","NOR","TAM","CAR","LAR","ARI","SFO","SEA",
"BAL","PIT","CIN","CLE","MIA","NWE","NYJ","BUF","IND","HOU","TEN","JAX","KAN","DEN","LVR","LAC"]
filenameQB = "QB.csv"
fieldsQB = []
rowsQB = []
with open(filenameQB, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fieldsQB = next(csvreader)
    for row in csvreader:
        rowsQB.append(row)


filenameRB = "RB.csv"
fieldsRB = []
rowsRB = []
with open(filenameRB, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fieldsRB = next(csvreader)
    for row in csvreader:
        rowsRB.append(row)

# filenameWRTE = "WRTE.csv"
# fieldsWRTE = []
# rowsWRTE = []
# with open(filenameWRTE, 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     fieldsWRTE = next(csvreader)
#     for row in csvreader:
#         rowsWRTE.append(row)

filenameOff = "offense.csv"
fieldsOff = []
rowsOff = []
with open(filenameOff, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fieldsOff = next(csvreader)
    for row in csvreader:
        rowsOff.append(row)

filenamePDef = "passdefense.csv"
fieldsPDef = []
rowsPDef = []
with open(filenamePDef, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fieldsPDef = next(csvreader)
    for row in csvreader:
        rowsPDef.append(row)

filenameRDef = "rushdefense.csv"
fieldsRDef = []
rowsRDef = []
with open(filenameRDef, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fieldsRDef = next(csvreader)
    for row in csvreader:
        rowsRDef.append(row)

filenameGames = "games.csv"
fieldsGames = []
rowsGames = []
with open(filenameGames, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fieldsGames = next(csvreader)
    for row in csvreader:
        rowsGames.append(row)
