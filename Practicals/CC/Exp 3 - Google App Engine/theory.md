## Experiment 3 — Google App Engine Hello World

### Aim

To configure **Google App Engine** and create a simple web application using **Python + Flask**.

### 1. Check installation

```bash
python3 --version
gcloud --version
```

### 2. Connect Google account

```bash
gcloud auth login
gcloud init
```

During `gcloud init`, select the Google account and your Cloud project.

Verify:

```bash
gcloud config get-value project
```

### 3. Create application folder

```bash
mkdir gae-hello
cd gae-hello
```

Create virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install packages:

```bash
pip install flask gunicorn
```

### 4. Create `main.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <h1>Hello World!</h1>
    <h2>Welcome to Google App Engine</h2>
    <p>Language: Python</p>
    <p>Framework: Flask</p>
    <p>Subject: Cloud Computing</p>
    <p>Experiment: Google App Engine</p>
    """

if __name__ == "__main__":
    app.run(port=8080)
```

### 5. Create `requirements.txt`

```bash
pip freeze > requirements.txt
```

### 6. Create `app.yaml`

```yaml
runtime: python314

entrypoint: gunicorn -b :$PORT main:app
```

Your folder should contain:

```text
gae-hello/
├── main.py
├── app.yaml
├── requirements.txt
└── .venv/
```

Check with:

```bash
ls
```

### 7. Run locally

```bash
python main.py
```

Open:

`http://127.0.0.1:8080`

You should see the **Hello World** page.

Stop the server with:

```text
Ctrl + C
```

### 8. App Engine deployment commands

```bash
gcloud app create
gcloud app deploy
gcloud app browse
```

In our practice, `gcloud app create` stopped with:

```text
The project must have a billing account attached.
```

So for the viva you can explain:

> **The application was successfully developed and tested locally. Cloud deployment could not be completed because Google App Engine requires a billing-enabled Google Cloud project.**

### 9. Disconnect account after practical

```bash
gcloud auth revoke --all
```

Verify:

```bash
gcloud auth list
```

### Important Viva

- **GAE:** Google App Engine.
- **Service model:** PaaS.
- **Flask:** Python web framework.
- **`main.py`:** Contains application code.
- **`app.yaml`:** App Engine configuration.
- **`requirements.txt`:** Lists Python dependencies.
- **`gcloud app create`:** Initializes App Engine.
- **`gcloud app deploy`:** Deploys the application.
- **Port used locally:** `8080`.
- **Why deployment failed in our case?** Billing account was not attached.

### Result

Successfully configured the Google Cloud environment and developed and tested a **Hello World Flask application** for Google App Engine. Cloud deployment requires a billing-enabled project.
