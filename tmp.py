import json
# import cPickle as pickle


# twitter = {
#     "user" : [{
#         "username": "John",
#         "email": "john@haha.com",
#         "password": "Hahaha123",
#         "fullname": "John rukmana"
#     },{
#         "username": "jeff",
#         "email": "jeff@haha.com",
#         "password": "Hahaha123",
#         "fullname": "John rukmana"
#     }],
#     "tweet" : [{
#         "email": "john@haha.com",
#         "tweet": "Ini ceritanya tweet Twitter yah",
#     },{
#         "email": "jeff@haha.com",
#         "tweet": "Ini ceritanya tweet Twitter yah"
#     }]
# }

# with open('oka.json','w') as file:
#     file.write(json.dumps(twitter))
#     file.close()
# twitter = {}
# twitter = open("oka.txt","r")
# twitter = twitter.read()
# print(twitter)
# print(twitter.read())

# with open('C:\Users\navcore\Desktop\Nitip\clientServer\Tugas twitter\oka.txt','w') as file:
#     file.write(pickle.dumps(twitter))


# class postTweet(Resource):
#     def __init__(self):
#         self.reqparse = reqparse.RequestParser()
#         self.reqparse.add_argument(
#             "tweet",
#             help = "please input your tweet",
#             required = True,
#             location = ["json"]
#         )
#         super().__init__()
#     def post(self):
#         data = request.json
#         cekEmailPostTweet(data["email"])
#         twitter["tweet"].append(data)
#         return "Success", 201

# class deleteTweet(Resource):
#     def delete(self):
#         data = request.json
#         for x in twitter["tweet"]:
#             if x["tweet"] == data["tweet"] and x["email"] == data["email"]:
#                 twitter["tweet"].remove(data)
#                 return "Success", 201
#         return "Failed, tweet not found", 404

# class readTweetUser(Resource):
#     def get(self):
#         data = request.json
#         arrTweet = []
#         for tweet in twitter["tweet"]:
#             if tweet["email"] == data["email"]:
#                 arrTweet.append(tweet["tweet"])
#         return arrTweet, 201
yuyu = {"asdaa" : "asdadsa"}
yiyi = {"oka" : "okasjdi"}

z = yuyu.copy()
z.update(yiyi)
print(z)

# yuyu = yuyu.update(yiyi)
# # print(yuyu["oka"])

# a= {"asdaa" : "asdadsa"}.update({"oka" : "okasjdi"})
# print(a)

# tmp = {}
# tmp["asda"] = "asdpaok"
# print(tmp)

# i = yuyu.update(tmp)
# print(i)