from flask import Flask,render_template,request
import sqlite3
con=sqlite3.connect("dbs.db")
try:
    con.execute("create table msg(name text,age int,email email)")
except:
    pass

app=Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')
    # return 'Hello World'

app.run()