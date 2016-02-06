import re
from random import choice

from flask import Flask, render_template, g, redirect, url_for, session
from flask_openid import OpenID

from models import Member

app = Flask(__name__)
oid = OpenID(app, 'store')

app.secret_key = "a bad secret key"
_steam_id_re = re.compile('steamcommunity.com/openid/id/(.*?)$')

backgrounds = [
    "ark.jpg",
    "rl.jpg",
    "csgo.jpg",
    "dota2.jpg"
]


@app.route("/")
def index():
    streaming = 3
    return render_template("index.html", bg=choice(backgrounds), streamers=streaming)

@app.route("/login")
def login():
    if g.user is not None:
        return redirect(oid.get_next_url())
    return oid.try_login("http://steamcommunity.com/openid")

@oid.after_login
def create_or_login(response):
    match = _steam_id_re.search(response.identity_url)
    g.user, created = Member.get_or_create(steam_id=match.group(1))
    session['user_id'] = g.user.id
    return redirect(oid.get_next_url())

@app.before_request
def lookup_current_user():
    g.user = None
    if 'user_id' in session:
        g.user = Member.get(Member.id == session['user_id'])


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(oid.get_next_url())

@app.route("/merch")
def merch():
    return render_template("merch.html", bg=choice(backgrounds))


@app.route("/join")
def join():
    return render_template("join.html", bg=choice(backgrounds))


@app.route("/chat")
def chat():
    return render_template("chat.html", bg=choice(backgrounds))


if __name__ == "__main__":
    app.run(debug=True)
