# Experiment 3 — Google App Engine Hello World — Windows

## Aim

To configure **Google App Engine (GAE)** and create a simple web application using **Python + Flask** on **Windows 10/11**.

### 1. Check Installation

Open **Command Prompt (CMD)** and run:

```bat
python --version
gcloud --version
```

If `python` does not work, try:

```bat
py --version
```

You need **Python** and **Google Cloud CLI** installed before proceeding.

### 2. Connect Google Account

```bat
gcloud auth login
gcloud init
```

A browser will open. Sign in with your Google account and select your Google Cloud project.

Verify the selected project:

```bat
gcloud config get-value project
```

### 3. Create Application Folder

For example, create it on the Desktop:

```bat
cd %USERPROFILE%\Desktop
mkdir gae-hello
cd gae-hello
```

Create the virtual environment:

```bat
python -m venv .venv
```

Activate it:

```bat
.venv\Scripts\activate
```

You should now see:

```text
(.venv) C:\Users\YourName\Desktop\gae-hello>
```

Install Flask and Gunicorn:

```bat
pip install flask gunicorn
```

> Note: Gunicorn is used by App Engine after deployment. On Windows, use Flask's development server for the local test.

### 4. Create `main.py`

Run:

```bat
notepad main.py
```

Click **Yes** if Notepad asks to create the file.

Paste:

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

Save and close Notepad.

### 5. Create `requirements.txt`

Run:

```bat
pip freeze > requirements.txt
```

Check:

```bat
type requirements.txt
```

### 6. Create `app.yaml`

Run:

```bat
notepad app.yaml
```

Paste:

```yaml
runtime: python314

entrypoint: gunicorn -b :$PORT main:app
```

Save and close.

Your folder should now contain:

```text
gae-hello\
│
├── main.py
├── app.yaml
├── requirements.txt
└── .venv\
```

Verify:

```bat
dir
```

### 7. Run the Application Locally

Run:

```bat
python main.py
```

You should see something similar to:

```text
Running on http://127.0.0.1:8080
```

Open your browser and enter:

```text
http://127.0.0.1:8080
```

You should see:

```text
Hello World!
Welcome to Google App Engine

Language: Python
Framework: Flask
Subject: Cloud Computing
Experiment: Google App Engine
```

Stop the server using:

```text
Ctrl + C
```

### 8. Deploy to Google App Engine

Make sure you are still inside:

```text
gae-hello
```

Then run:

```bat
gcloud app create
```

Select a region when asked.

Then:

```bat
gcloud app deploy
```

Confirm with:

```text
Y
```

If deployment succeeds:

```bat
gcloud app browse
```

The deployed application will open in your browser.

### If You Get the Billing Error

You may receive:

```text
The project must have a billing account attached.
```

This means your code is not necessarily the problem. App Engine initialization/deployment requires an appropriately configured Google Cloud project, including billing when required.

For your practical/viva:

> **The application was successfully developed and tested locally. Cloud deployment could not be completed because the Google Cloud project did not have the required billing configuration.**

### 9. Disconnect Your Google Account

After the practical:

```bat
gcloud auth revoke --all
```

Verify:

```bat
gcloud auth list
```

## Quick Windows Commands to Remember

```bat
mkdir gae-hello
cd gae-hello

python -m venv .venv
.venv\Scripts\activate

pip install flask gunicorn

notepad main.py
pip freeze > requirements.txt
notepad app.yaml

python main.py

gcloud auth login
gcloud init
gcloud app create
gcloud app deploy
gcloud app browse
```

The main difference from your Mac procedure is virtual-environment activation:

**Mac/Linux**

```bash
source .venv/bin/activate
```

**Windows CMD**

```bat
.venv\Scripts\activate
```

### Result

Successfully configured the Google Cloud environment on Windows and developed and locally tested a **Hello World Flask application** for Google App Engine. Cloud deployment can be performed using the Google Cloud CLI with a properly configured project.
