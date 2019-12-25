from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    name = input("Please input your name: ")
    return name + "Happy New Year!"

if __name__ == "__main__":
    application.run()
