from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")

def Books():

    return ("Hello user")

books = [
    {"name":"Harry Potter", "like-ness scale": 7}, 
    {"name":"Alex Rider", "like-ness scale": 9},
    {"name":"Diary of a Wimpy kid", "like-ness scale": 8}
]

@app.route("/Get", methods = ["GET"])

def Get ():
     return jsonify({"Data": books})


@app.route("/Post", methods = ["Post"])

def Post():

    b = {"name":"Life of Pi", "like-ness scale": 5}
    
    books.append(b)
    return jsonify ({"Data":books})

        


app.run()

