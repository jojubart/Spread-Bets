from flask import Flask



app = Flask(__name__) # determine the route path

# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route('/') # Homepage of the website
def index():
    return '<h2>This is the homepage</h2>'

if __name__ == "__main__":
    app.run(debug=True) # start the server






