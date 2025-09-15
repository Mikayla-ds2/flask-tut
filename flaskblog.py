from flask import Flask # importing the flask class
app = Flask(__name__) # setting to an instance of the flask class using app variable
# the double underscore name is a special variable in python; name of the module

@app.route("/") # the route decorator
@app.route("/home") # now both routes go to same page
def home():
    return '<h1>Home Page</h1>'

@app.route("/about")
def about():
    return '<h1>About Page</h1>'

if __name__ == '__main__': # conditional is only true if running script directly
    app.run(debug=True)