from flask import Flask

app = Flask(__name__)


@app.route("/") # This is a decorator which will fire the below function when the url inside the parentheses in clicked
def index():
    return "Hello World from Flask"


@app.route("/about") # append /about in base url to get the below function
def about():
    return "<h1 style ='color: red'>About !!!!</h1>"


if __name__ == "__main__":
    app.run()

