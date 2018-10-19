import os
import env
from flask import Flask
from resources.Twitter import twitter_api

app = Flask(__name__)
app.register_blueprint(twitter_api, url_prefix = '/api/v1/')

@app.route("/")
def hello():
    return "TWITTER"


if __name__ == '__main__':
    app.run(debug=True, host=env.HOST, port=env.PORT)
    # app.run(debug=True, host=os.getenv("HOST"), port=os.getenv("PORT"))