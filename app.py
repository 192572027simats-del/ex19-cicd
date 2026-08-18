from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "LAB EX19 - Continuous Deployment using GitHub Actions!"

@app.route("/version")
def version():
    return "Version 1.0"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)