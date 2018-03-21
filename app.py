from flask import Flask, render_template
import sqlite3
import json

db = sqlite3.connect('db.sqlite3')
db.row_factory = sqlite3.Row

app = Flask('MyApp')

@app.route('/json')
def return_data():
    td = []
    cur = db.cursor()
    cur.execute("Select Group_Number as col1 FROM Group_")
    rows = cur.fetchall()
    for r in rows:
        td.append(dict(r))
    return json.dumps(td)


@app.route('/')
def index():
    return render_template('index.html')

app.run()