import requests
from bs4 import BeautifulSoup




url = "http://www.nfl.com/scores/2017/REG2"
r = requests.get(url)
r_html = r.content
soup = BeautifulSoup(r_html, "html.parser")

scores = soup.find_all("p", {"class": "total-score"})
teams = soup.find_all("p", {"class": "team-name"})

teamlist = []
match = []
scorelist = []

for team, score in zip(teams, scores):
    match.append('{} {}'.format(team.text, score.text))
    teamlist.append(team.text)
    scorelist.append(score.text)

#scorelist = ("\n".join(scorelist))
dictScores = dict(zip(teamlist, scorelist))



# Spread Scrape:
url = "https://www.cbssports.com/nfl/features/writers/expert/picks"
r = requests.get(url)
r_html = r.content
soup = BeautifulSoup(r_html, "html.parser")


away_teams = soup.find_all("span", {"class": "teamAbbrPreview fright"})
home_teams = soup.find_all("span", {"class": "teamAbbrPreview fleft"})
spreads = soup.find_all("span", {"id": "lineNumber"})

#away_teams = ["Buccaneers" if x=="TB" else "Dolphins" if x=="MIA" else x for x in away_teams.text]


slist = []
hometeam = []
awayteam = []
spreadlist = []
dictSpreads = {}
match = {}
# zip items from the three lists together
for away, home, spread in zip(away_teams, home_teams,
                              spreads):
    aTeam = away.text
    hTeam = home.text
    if aTeam == "ARI":
        aTeam = "Cardinals"
    elif aTeam == "ATL":
        aTeam = "Falcons"
    elif aTeam == "BAL":
        aTeam = "Ravens"
    elif aTeam == "CAR":
        aTeam = "Panthers"
    elif aTeam == "BUF":
        aTeam = "Bills"
    elif aTeam == "BAL":
        aTeam = "Ravens"
    elif aTeam == "CHI":
        aTeam = "Bears"
    elif aTeam == "CIN":
        aTeam = "Bengals"
    elif aTeam == "CLE":
        aTeam = "Browns"
    elif aTeam == "DAL":
        aTeam = "Cowboys"
    elif aTeam == "DEN":
        aTeam = "Broncos"
    elif aTeam == "DET":
        aTeam = "Lions"
    elif aTeam == "GB":
        aTeam = "Packers"
    elif aTeam == "HOU":
        aTeam = "Texans"
    elif aTeam == "IND":
        aTeam = "Colts"
    elif aTeam == "JAC":
        aTeam = "Jaguars"
    elif aTeam == "KC":
        aTeam = "Chiefs"
    elif aTeam == "MIA":
        aTeam = "Dolphins"
    elif aTeam == "MIN":
        aTeam = "Vikings"
    elif aTeam == "NE":
        aTeam = "Patriots"
    elif aTeam == "NO":
        aTeam = "Saints"
    elif aTeam == "NYG":
        aTeam = "Giants"
    elif aTeam == "NYJ":
        aTeam = "Jets"
    elif aTeam == "OAK":
        aTeam = "Raiders"
    elif aTeam == "PHI":
        aTeam = "Eagles"
    elif aTeam == "PIT":
        aTeam = "Steelers"
    elif aTeam == "LAC":
        aTeam = "Chargers"
    elif aTeam == "LAR":
        aTeam = "Rams"
    elif aTeam == "SF":
        aTeam = "49ers"
    elif aTeam == "SEA":
        aTeam = "Seahawks"
    elif aTeam == "TB":
        aTeam = "Buccaneers"
    elif aTeam == "TEN":
        aTeam = "Titans"
    elif aTeam == "WAS":
        aTeam = "Redskins"


    if hTeam == "ARI":
        hTeam = "Cardinals"
    elif hTeam == "ATL":
        hTeam = "Falcons"
    elif hTeam == "BAL":
        hTeam = "Ravens"
    elif hTeam == "CAR":
        hTeam = "Panthers"
    elif hTeam == "BUF":
        hTeam = "Bills"
    elif hTeam == "CHI":
        hTeam = "Bears"
    elif hTeam == "CIN":
        hTeam = "Bengals"
    elif hTeam == "CLE":
        hTeam = "Browns"
    elif hTeam == "DAL":
        hTeam = "Cowboys"
    elif hTeam == "DEN":
        hTeam = "Broncos"
    elif hTeam == "DET":
        hTeam = "Lions"
    elif hTeam == "GB":
        hTeam = "Packers"
    elif hTeam == "HOU":
        hTeam = "Texans"
    elif hTeam == "IND":
        hTeam = "Colts"
    elif hTeam == "JAC":
        hTeam = "Jaguars"
    elif hTeam == "KC":
        hTeam = "Chiefs"
    elif hTeam == "MIA":
        hTeam = "Dolphins"
    elif hTeam == "MIN":
        hTeam = "Vikings"
    elif hTeam == "NE":
        hTeam = "Patriots"
    elif hTeam == "NO":
        hTeam = "Saints"
    elif hTeam == "NYG":
        hTeam = "Giants"
    elif hTeam == "NYJ":
        hTeam = "Jets"
    elif hTeam == "OAK":
        hTeam = "Raiders"
    elif hTeam == "PHI":
        hTeam = "Eagles"
    elif hTeam == "PIT":
        hTeam = "Steelers"
    elif hTeam == "LAC":
        hTeam = "Chargers"
    elif hTeam == "LAR":
        hTeam = "Rams"
    elif hTeam == "SF":
        hTeam = "49ers"
    elif hTeam == "SEA":
        hTeam = "Seahawks"
    elif hTeam == "TB":
        hTeam = "Buccaneers"
    elif hTeam == "TEN":
        hTeam = "Titans"
    elif hTeam == "WAS":
        hTeam = "Redskins"





    slist.append('{} {} {} {}'.format(aTeam, "@", hTeam, spread.text))
    hometeam.append(hTeam)
    awayteam.append(aTeam)
    spreadlist.append(spread.text)
    dictSpreads[aTeam] = spread.text
    match[aTeam] = hTeam

#slist = ("\n".join(slist))
#print(slist)
print(dictScores)
print(dictSpreads)
#print(match)

length = len(hometeam)

awaylist = []

#print(score_Chiefs)


# updates the spreads scores: The spread is added to the home team's score
for key in dictSpreads:
    for jey in dictScores:
        if key == jey:
            try:
                dictScores[key] = int(dictScores[key])
                dictSpreads[key] = int(dictSpreads[key])
                dictScores[key] += dictSpreads[key]
                print(dictScores)
            except:
                continue

listScores = list(dictScores.items())

print(listScores)
for key in range(len(listScores)):
    if key%2!= 0:
        continue
    else:
        try:
            aScore = int(listScores[key][1])
            hScore = int(listScores[key+1][1])

            if(aScore > hScore):
                print(listScores[key][0] + " are winning against the Spread")
            else:
                print(listScores[key+1][0] + " are winning against the Spread")
        except:
            continue







# COMPARE dictSpread and dictScores and add the dict entry if they match





