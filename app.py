from flask import Flask, request, render_template
import smtplib # for mail
import requests
import itertools # for zip iteration
import datetime # to run on pythonanywhere.com only on Thursdays
from bs4 import BeautifulSoup
from scrape import dictScores, length, hometeam, awayteam, spreadlist, listScores



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

@app.route("/spreads", methods = ["GET", "POST"])
def spread():
    for item in request.form.values():
        print(item)
    #ateam = request.form["ateams"]
    return render_template("spreads.html", hometeam = hometeam, awayteam = awayteam, spreadlist = spreadlist, length = length)


@app.route("/result", methods = ['POST', 'GET'])
def result():
    if request.method =='POST':
        result = request.form
        return render_template("result.html", result = result)

userBets = []


if __name__ == "__main__":
    app.run(debug=True) # start the server






