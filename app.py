from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    'The secret files are located here [REDACTED]'
    '[REDACTED],[REDACTED],[REDACTED],[REDACTED],TOM WAS INVOLVED WITH [REDACTED][REDACTED], BRENT WATCHED ANDY [REDACTED][REDACTED][REDACTED]'
    return 'Hello, World!'

