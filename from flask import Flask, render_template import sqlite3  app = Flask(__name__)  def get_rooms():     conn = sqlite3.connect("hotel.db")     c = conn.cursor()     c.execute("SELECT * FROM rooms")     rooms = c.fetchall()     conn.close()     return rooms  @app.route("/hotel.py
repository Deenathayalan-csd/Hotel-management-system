from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_rooms():
    conn = sqlite3.connect("hotel.db")
    c = conn.cursor()
    c.execute("SELECT * FROM rooms")
    rooms = c.fetchall()
    conn.close()
    return rooms

@app.route("/")
def index():
    rooms = get_rooms()
    return render_template("index.html", rooms=rooms)

if __name__ == "__main__":
    app.run(debug=True)
