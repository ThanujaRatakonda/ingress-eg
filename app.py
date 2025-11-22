from flask import Flask, render_template, request, redirect
import json
import os
app = Flask(__name__)
users = []
DATA_FILE = "/app/data/users.json"
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        users = json.load(f)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form.get("name")
    email = request.form.get("email")
    if name and email:
        users.append({"name": name, "email": email})
        with open(DATA_FILE, "w") as f:
            json.dump(users, f)
    return redirect("/users")
@app.route("/users")
def display_users():
    return render_template("users.html", users=users)
@app.route("/error")
def trigger_error():
    import os
    os._exit(1)
    return "Container crashed"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
