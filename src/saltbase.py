import os
import sys
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


#--- Dashboard ---#
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/<database>")
def database(database: str):
    return render_template("database.html")


@app.route("/<database>/<table>")
def table(database: str, table: str):
    return render_template("table.html")


#--- API ---#
@app.route("/api/databases", methods=["GET", "POST", "PATCH", "DELETE"])
def api_databases():
    pass


@app.route("/api/databases/<database>", methods=["GET", "POST", "PATCH", "DELETE"])
def api_database(database: str):
    pass


@app.route("/api/databases/<database>/<table>", methods=["GET", "POST", "PATCH", "DELETE"])
def api_table(database: str, table: str):
    pass


if __name__ == "__main__":
    app.run("0.0.0.0", port=42069)