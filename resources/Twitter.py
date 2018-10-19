from flask import Flask, jsonify, Blueprint, request
from flask_restful import Resource, Api, reqparse, inputs, abort
import json
import datetime


twitter = {}
with open('oka.json') as file:
    twitter = json.load(file)

    
class ReadAll(Resource):
    def get(self):
        return twitter

class Login(Resource):
    def post(self):
        data = request.json
        for user in twitter["user"]:
            if user["email"] == data["email"]:
                if user["password"] == data["password"]:
                    # cookies["email"] = data["email"]
                    return "Login success", 200
        return "Username or Password incorrect", 401

def cekUsername(username):
    for user in twitter["user"]:
        if user["username"] == username:
            abort(400, message = "Username already exist")
    return username

def cekEmail(email):
    for user in twitter["user"]:
        if user["email"] == email:
            abort(400,message = "Email already exist")
    return email

def cekEmailPostTweet(email):
    for user in twitter["user"]:
        if user["email"] == email:
            return email
    return "Email not exist"

def saveData(twitter):
    with open('oka.json','w') as file:
            file.write(json.dumps(twitter))
            file.close()
    # with open('oka.json', 'w') as outfile:  
    #     json.dump(twitter, outfile)

class Signup(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "username",
            help = "please input username",
            required = True,
            location = ["json"]
        )
        self.reqparse.add_argument(
            "email",
            help = "Please input email",
            required = True,
            location = ["json"]
        )
        self.reqparse.add_argument(
            "password",
            help = "Please input password",
            required = True,
            location = ["json"]
        )
        self.reqparse.add_argument(
            "fullname",
            help = "please input fullname",
            required = True,
            location = ["json"]
        )
        super().__init__()

    def post(self):
        args = self.reqparse.parse_args() #buat apa ??
        data = request.json
        cekUsername(data["username"])
        cekEmail(data["email"])
        twitter["user"].append(data)
        saveData(twitter)
        return "Signup Successfully", 201

class Tweet(Resource):
    # status = cekCookies(cookies)
    # if status == True:

    # else:
    #     return "Not Login"

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "tweet",
            help = "please input your tweet",
            required = True,
            location = ["json"]
        )
        super().__init__()
    
    def get(self):
        data = request.json
        arrTweet = []
        for tweet in twitter["tweet"]:
            if tweet["email"] == data["email"]:
                arrTweet.append(tweet["tweet"])
        return arrTweet, 201

    def post(self):
        data = request.json
        time = str(datetime.datetime.now())
        tmp = {}
        tmp["time"] = time
        req = data.copy()
        req.update(tmp)
        cekEmailPostTweet(data["email"])
        twitter["tweet"].append(req)
        saveData(twitter)
        return "Success", 201

    def delete(self):
        data = request.json
        for x in twitter["tweet"]:
            if x["tweet"] == data["tweet"] and x["email"] == data["email"]:
                twitter["tweet"].remove(data)
                saveData(twitter)
                return "Success", 201
        return "Failed, tweet not found", 404
    
    def put(self):
        data = request.json
        for x in twitter["tweet"]:
            if x["tweet"] == data["tweet"] and x["email"] == data["email"]:
                x["tweet"] = data["newtweet"]
                x["time"] = str(datetime.datetime.now())
                saveData(twitter)
                return "Success", 200

twitter_api = Blueprint("resources/twitter",__name__) #kalo error cek disini
api = Api(twitter_api)
api.add_resource(Login,'login')
api.add_resource(Signup, 'signup')
api.add_resource(Tweet,'tweet')
api.add_resource(ReadAll,'readAll')

# api.add_resource(postTweet,'postTweet')
# api.add_resource(deleteTweet,'deleteTweet')
# api.add_resource(readTweetUser, 'readTweetUser')


