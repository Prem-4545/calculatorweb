from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Home Page
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operator = request.form["operator"]

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2 if num2 != 0 else "Error"

        # Save to database
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS history (num1 REAL, operator TEXT, num2 REAL, result TEXT)")
        c.execute("INSERT INTO history (num1, operator, num2, result) VALUES (?, ?, ?, ?)",
                  (num1, operator, num2, str(result)))
        conn.commit()
        conn.close()

    return render_template("index.html", result=result)

# View History
@app.route("/history")
def history():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM history ORDER BY ROWID DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    return render_template("history.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)
