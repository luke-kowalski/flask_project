from unicodedata import name
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "elo mordo"

if __name__ == '__main__':
    app.run(debug=True)