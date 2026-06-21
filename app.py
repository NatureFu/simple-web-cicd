from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello CI/CD v1.0 - 姓名：付自然 学号：2440664307"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)

