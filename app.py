from flask import Flask, render_template, jsonify, flash, get_flashed_messages

import secrets

app = Flask(__name__)

count = 0
click_value = 1
# Upgradeするために必要な変数

app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def index():
    global count, click_value
    return render_template("index.html", count=count, click_value=click_value)


@app.route("/increment", methods=["POST"])
def increment():
    global count, click_value
    count += click_value
    return jsonify({"counter": count})


@app.route("/upgrade", methods=["POST"])
def upgrade():
    global count, click_value
    if count >= 10:
        count -= 10
        click_value += 1
    else:
        flash("Not enough your point.")
        message = get_flashed_messages()
    return jsonify({"counter": count, "click_value": click_value, "message": message})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)

# url_for これを使えばrouteのurlを変えても関数で紐づいているため問題なく動く。
