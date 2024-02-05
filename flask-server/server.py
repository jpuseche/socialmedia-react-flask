from flask import Flask

app = Flask(__name__)

@app.route("/posts")
def members():
    return {"posts": ["Juan"]}