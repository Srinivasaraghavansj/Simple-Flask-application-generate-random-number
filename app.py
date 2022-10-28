from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def display_random_number():
    return f"<h2>The random number is {random.randint(0,9999)}</h2>"


if __name__ == "__main__":
    app.run()
