from flask import Flask 

# __name__ = "__main__"
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/about")
def about():
    return "Testing"

if __name__ == "__main__":
    app.run(debug=True)