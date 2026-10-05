from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello World!</h1><p>Running on Google App Engine.</p>"


@app.route("/student")
def student():
    return """
    <h1>Student Information</h1>
    <p>Name: Kshitij Sawant</p>
    <p>Course: B.Tech AI and Data Science</p>
    """


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)