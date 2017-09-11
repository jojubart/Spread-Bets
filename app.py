from flask import Flask, request, render_template
import smtplib # for mail
import requests
import itertools # for zip iteration
import datetime # to run on pythonanywhere.com only on Thursdays
from bs4 import BeautifulSoup



app = Flask(__name__) # determine the route path

# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route("/") # Homepage of the website
@app.route("/<user>") # If user is logged in, he is directed to his account, otherwise to regular homepage
def index(user=None):
    return render_template("user.html", user=user)


@app.route("/profile/<username>") # variables are in '< >'
def profile(username):
    return render_template("profile.html", username=username)

@app.route("/week/<int:week>") # ints have to be announced like this
def week(week):
    return "This is week {}".format(week)

@app.route("/spreads")
def spread():
    return render_template("spreads.html", hometeam = hometeam, awayteam = awayteam, spreadlist = spreadlist, length = length)




# Spread Scrape:
url = "https://www.cbssports.com/nfl/features/writers/expert/picks"
r = requests.get(url)
r_html = r.content
soup = BeautifulSoup(r_html, "html.parser")

td = soup.find_all("td")

away_teams = soup.find_all("span", {"class": "teamAbbrPreview fright"})
home_teams = soup.find_all("span", {"class": "teamAbbrPreview fleft"})
spreads = soup.find_all("span", {"id": "lineNumber"})

slist = []
hometeam = []
awayteam = []
spreadlist = []
# zip items from the three lists together
for away, home, spread in zip(away_teams, home_teams,
                              spreads):
    slist.append('{} {} {} {}'.format(away.text, "@", home.text, spread.text))
    hometeam.append(home.text)
    awayteam.append(away.text)
    spreadlist.append(spread.text)

#slist = ("\n".join(slist))
print(slist)
print(spreadlist)
length = len(hometeam)









if __name__ == "__main__":
    app.run(debug=True) # start the server






