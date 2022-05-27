from flask_app import Flask

app = Flask('pridebot_server')

@app.route("/slack/events")
def hello_world():
    return "<p>Hello, World!</p>"



