from flask import Flask, request, render_template



app = Flask(__name__) # determine the route path

# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route("/") # Homepage of the website
def index():
    return "Spread Bets"


@app.route("/profile/<username>") # variables are in '< >'
def profile(username):
    return render_template("profile.html", username=username)

@app.route("/week/<int:week>") # ints have to be announced like this
def week(week):
    return "This is week {}".format(week)










if __name__ == "__main__":
    app.run(debug=True) # start the server






