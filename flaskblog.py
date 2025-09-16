from flask import Flask, render_template # importing the flask class
app = Flask(__name__) # setting to an instance of the flask class using app variable
# the double underscore name is a special variable in python; name of the module

posts = [
    {
        'author': 'Mikayla Solomon',
        'title': 'Blog Post 1', 
        'content': 'First post content',
        'date': 'June 10, 2008'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': "Second post content",
        'date': 'June 11, 2009'
    }
]

@app.route("/") # the route decorator
@app.route("/home") # now both routes go to same page
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__': # conditional is only true if running script directly
    app.run(debug=True)