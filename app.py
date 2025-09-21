from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_user", methods=["POST"])
def add_user():
    nombre = request.form["nombre"]
    email = request.form["email"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
    conn.commit()
    conn.close()

    return "Usuario agregado!"

@app.route("/get_users", methods=["GET"])
def get_users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)