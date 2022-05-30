from flask import Flask

app = Flask(__name__)

@app.route("/python/sample")
def sample_api():
    print("calling /python/sample")
    return {
        "username": "luis",
        "theme": "tema",
        "image": "/img.png",
    }

@app.route("/python/sample/health/liveness")
def liveness_api():
    print("calling /python/sample/health/liveness")
    return {
        "live": "yes!"
    }


# https://flask.palletsprojects.com/en/2.1.x/installation/
# https://flask.palletsprojects.com/en/2.1.x/quickstart/
# https://predictivehacks.com/how-to-use-docker-for-flask-api/