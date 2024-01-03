from flask import Flask

app = Flask(__name__)

# Main page
@app.route("/")
def index():
    return "Hello, Flask!"

# Some pages with common functional
@app.route("/company")
@app.route("/about")
def about():
    return "<h1 style=\"color: aqua\">About our company</h1>"

if __name__ == "__main__":
    app.run(debug=True)
