from flask import Flask

PORT = 8000
f = open('HelloMessage.txt','r')
MESSAGE = f.read()

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
