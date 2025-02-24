from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    with open("/data/message.txt", "w") as f:
        f.write("Hello from Flask!")
    return "Data written to shared volume!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
