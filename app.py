from flask import Flask, render_template

app= Flask(__name__)

responses = []

@app.route("/")
def root_page():
    return render_template("root_page.html")
