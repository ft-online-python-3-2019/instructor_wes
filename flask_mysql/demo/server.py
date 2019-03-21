from flask import Flask, render_template
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    db = connectToMySQL('sept_py1_twitter')
    users_list = db.query_db('SELECT * FROM users;')
    return render_template("index.html", users=users_list)

if __name__ == "__main__":
    app.run(debug=True)