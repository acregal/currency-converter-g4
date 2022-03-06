"""Create webpage in python"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def webpage():
    "Creating a webpage"
    return render_template("currencyconverter.html")

if __name__ == '__main__':
    app.run(debug=True)
