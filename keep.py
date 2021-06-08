from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)