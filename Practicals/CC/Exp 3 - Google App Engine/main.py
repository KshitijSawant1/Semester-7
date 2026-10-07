from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <h1>Hello World!</h1>
    <h2>Practical Exam</h2>
    <p>This application is developed using Python.</p>
    <p>Name : Kshitij K Sawant ; AI & DS - B ; BT</p>
    <p>Subject: Cloud Computing</p>
    <p>Experiment: Google App Engine</p>
    """

if __name__ == "__main__":
    app.run(port=8080)