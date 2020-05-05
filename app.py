from flask import Flask, render_template
import sqlite3
import json
import time


class DB:
    db = None

    def __init__(self):
        self.db = sqlite3.connect(
            'db.sqlite3',
            check_same_thread=False)
        self.db.row_factory = sqlite3.Row

    def sql(self, query):
        cur = self.db.cursor()
        cur.execute(query)
        return cur.fetchall()

db = DB()

app = Flask('MyApp')

@app.route('/json')
def return_data():
    td = []
    rows = db.sql("Select Group_Number as col1 FROM Group_")
    for r in rows:
        td.append(dict(r))
    print(json.dumps(td))
    time.sleep(15)
    return json.dumps(td)


@app.route('/')
def index():
    return render_template('index.html')

app.run()