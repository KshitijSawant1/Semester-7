# Google App Engine — Proper Setup and Removal Steps (Windows)

Use this clean procedure for **Experiments 3 and 4 on Windows 10/11**.

## Part A — Set Up Google App Engine

### 1. Check Python

Open **Command Prompt (CMD)**:

```bat
python --version
```

If that doesn't work:

```bat
py --version
```

### 2. Check Google Cloud CLI

```bat
gcloud --version
```

If the command works, continue.

### 3. Login to Google Cloud

```bat
gcloud auth login
```

Your browser will open. Sign in using your Google account.

### 4. Initialize Google Cloud CLI

```bat
gcloud init
```

If asked:

```text
[1] Re-initialize this configuration
[2] Create a new configuration
```

Choose:

```text
1
```

Select your account and Google Cloud project.

Verify:

```bat
gcloud config get-value project
```

---

# Part B — Create the Web Application

### 5. Create Project Folder

For example, on Desktop:

```bat
cd %USERPROFILE%\Desktop
mkdir gae-hello
cd gae-hello
```

### 6. Create Python Virtual Environment

```bat
python -m venv .venv
```

Activate:

```bat
.venv\Scripts\activate
```

You should see:

```text
(.venv) C:\Users\YourName\Desktop\gae-hello>
```

### 7. Install Dependencies

```bat
pip install flask gunicorn
```

Create `requirements.txt`:

```bat
pip freeze > requirements.txt
```

### 8. Create `main.py`

```bat
notepad main.py
```

Paste:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello World!</h1>
    <h2>Google App Engine</h2>
    <p>Cloud Computing Practical</p>
    <p>Language: Python</p>
    <p>Framework: Flask</p>
    """

if __name__ == "__main__":
    app.run(port=8080)
```

Save and close Notepad.

### 9. Create `app.yaml`

```bat
notepad app.yaml
```

Paste:

```yaml
runtime: python314

entrypoint: gunicorn -b :$PORT main:app
```

Save and close.

Check the directory:

```bat
dir
```

It should contain:

```text
gae-hello\
│
├── main.py
├── app.yaml
├── requirements.txt
└── .venv\
```

---

# Part C — Test the Application

Run:

```bat
python main.py
```

You should see:

```text
Running on http://127.0.0.1:8080
```

Open the browser and enter:

```text
http://127.0.0.1:8080
```

You should see the **Hello World** application.

Stop the server:

```text
Ctrl + C
```

---

# Part D — Set Up App Engine and Deploy

Make sure you are in the correct folder:

```bat
cd %USERPROFILE%\Desktop\gae-hello
dir
```

You should see `main.py`, `app.yaml`, and `requirements.txt`.

Create App Engine:

```bat
gcloud app create
```

Choose the required region.

Deploy:

```bat
gcloud app deploy
```

If asked:

```text
Do you want to continue (Y/n)?
```

Enter:

```text
Y
```

After successful deployment:

```bat
gcloud app browse
```

### Sequence to Remember

```text
gcloud auth login
        ↓
gcloud init
        ↓
Select Project
        ↓
gcloud app create
        ↓
gcloud app deploy
        ↓
gcloud app browse
```

## Billing Issue

If you receive:

```text
The project must have a billing account attached.
```

you can stop there. For your practical, demonstrate the Flask application locally and explain:

> **The application was successfully developed and tested locally. Cloud deployment requires a Google Cloud project with the required billing configuration.**

---

# Part E — Remove / Disconnect Everything

### 1. Stop Flask

If Flask is running:

```text
Ctrl + C
```

### 2. Exit Virtual Environment

```bat
deactivate
```

### 3. Disconnect Your Google Account

Check the logged-in account:

```bat
gcloud auth list
```

Revoke all locally stored authentication:

```bat
gcloud auth revoke --all
```

Verify:

```bat
gcloud auth list
```

### 4. Delete Local Application — Optional

Go to Desktop:

```bat
cd %USERPROFILE%\Desktop
```

Delete the folder using:

```bat
rmdir /s /q gae-hello
```

**Be careful:** this permanently deletes the `gae-hello` folder.

### 5. Google Cloud CLI

You **do not need to uninstall Google Cloud CLI** after the practical.

On a shared/college computer, simply revoke your Google account:

```bat
gcloud auth revoke --all
```

---

# Commands to Memorize

### Setup

```bat
gcloud auth login
gcloud init
gcloud config get-value project
```

### Application

```bat
python -m venv .venv
.venv\Scripts\activate

pip install flask gunicorn
pip freeze > requirements.txt

python main.py
```

### App Engine

```bat
gcloud app create
gcloud app deploy
gcloud app browse
```

### Cleanup

```bat
deactivate
gcloud auth revoke --all
gcloud auth list
```

### Most Important Viva Sequence

**Login → Initialize → Select Project → Create App Engine → Deploy → Browse → Revoke account when finished.**

The main Windows-specific differences are `.venv\Scripts\activate` instead of `source .venv/bin/activate`, `dir` instead of `ls`, and `rmdir /s /q` instead of `rm -rf`.
