## Google App Engine — Proper Setup and Removal Steps

For Experiments **3 and 4**, this is the clean procedure you can follow tomorrow.

### Part A — Set Up Google App Engine

**1. Check Python**

```bash
python3 --version
```

**2. Check Google Cloud CLI**

```bash
gcloud --version
```

If `gcloud` is already installed, continue.

**3. Login to Google Cloud**

```bash
gcloud auth login
```

A browser opens. Sign in with your Google account.

**4. Initialize Google Cloud CLI**

```bash
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

Then select your account and Google Cloud project.

Verify:

```bash
gcloud config get-value project
```

---

### Part B — Create the Web Application

**5. Create project folder**

```bash
mkdir gae-hello
cd gae-hello
```

**6. Create and activate Python environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

**7. Install dependencies**

```bash
pip install flask gunicorn
```

Create `requirements.txt`:

```bash
pip freeze > requirements.txt
```

**8. Create `main.py`**

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

**9. Create `app.yaml`**

```yaml
runtime: python314

entrypoint: gunicorn -b :$PORT main:app
```

Your directory should be:

```text
gae-hello/
├── main.py
├── app.yaml
├── requirements.txt
└── .venv/
```

---

### Part C — Test the Application

Run:

```bash
python main.py
```

Open:

`http://127.0.0.1:8080`

If **Hello World** appears, your application is working.

Stop it:

```text
Ctrl + C
```

---

### Part D — Set Up App Engine and Deploy

Make sure you're inside `gae-hello`:

```bash
pwd
ls
```

Then:

```bash
gcloud app create
```

Choose your region.

Then deploy:

```bash
gcloud app deploy
```

After successful deployment:

```bash
gcloud app browse
```

The sequence is:

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

### Billing Issue

In your practice account, `gcloud app create` gave:

```text
The project must have a billing account attached.
```

So **don't attach billing just for practice**. You can demonstrate the Flask application locally and explain that cloud deployment requires a billing-enabled project.

---

# Part E — Remove/Disconnect Everything After Practical

There are several different things you may want to remove.

### 1. Stop the Flask Application

If it's running:

```text
Ctrl + C
```

### 2. Exit Python Virtual Environment

```bash
deactivate
```

### 3. Disconnect Google Account from `gcloud`

First check authenticated accounts:

```bash
gcloud auth list
```

Then remove all locally stored gcloud authentication:

```bash
gcloud auth revoke --all
```

Verify:

```bash
gcloud auth list
```

### 4. Remove the Local Application

If you no longer need the practice application:

```bash
cd ..
rm -rf gae-hello
```

Be careful with `rm -rf`; make sure you're deleting the correct folder.

### 5. Remove Google Cloud CLI — Optional

You **do not need to uninstall `gcloud` after every practical**. Logging out with `gcloud auth revoke --all` is normally enough.

If this is a college/shared computer, revoke your authentication when you're finished.

---

## Commands to Memorize

### Setup

```bash
gcloud auth login
gcloud init
gcloud config get-value project
```

### Application

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install flask gunicorn
pip freeze > requirements.txt

python main.py
```

### App Engine

```bash
gcloud app create
gcloud app deploy
gcloud app browse
```

### Cleanup

```bash
deactivate
gcloud auth revoke --all
gcloud auth list
```

For the viva, remember the core sequence as:

**Login → Initialize → Select Project → Create App Engine → Deploy → Browse → Revoke account when finished.**
