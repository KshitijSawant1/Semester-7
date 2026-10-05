from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Google App Engine Application</h1>
    <p>Experiment 4 application deployed using Render.</p>
    """

@app.route("/student")
def student():
    return """
    <h2>Student Details</h2>
    <p>Name: Kshitij Sawant</p>
    <p>Course: B.Tech AI & DS</p>
    """

@app.route("/about")
def about():
    return """
    <h2>Cloud Computing Laboratory</h2>
    <p>Application launching and management experiment.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)