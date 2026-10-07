For this practical, you **do not need to build a complete real IPTV service**. The easiest way to perform it is to create a small **local video-streaming setup with multiple servers + Nginx load balancing**, then explain where the CDN fits.

Since you already have Ubuntu, do this there.

## 1. Install Nginx

Open Ubuntu Terminal:

```bash
sudo apt update
sudo apt install nginx -y
```

Check:

```bash
nginx -v
```

---

## 2. Create Two Streaming Servers

We'll simulate two cloud streaming servers using Python.

Create Server 1:

```bash
mkdir -p ~/iptv/server1
cd ~/iptv/server1
echo "<h1>IPTV Streaming Server 1</h1>" > index.html
```

Start it:

```bash
python3 -m http.server 8001
```

Keep this terminal running.

---

## 3. Start Server 2

Open a **new terminal**:

```bash
mkdir -p ~/iptv/server2
cd ~/iptv/server2
echo "<h1>IPTV Streaming Server 2</h1>" > index.html
```

Start:

```bash
python3 -m http.server 8002
```

Now you have:

```text
Server 1 → localhost:8001
Server 2 → localhost:8002
```

Test in browser:

```text
http://localhost:8001
http://localhost:8002
```

You should see the two different server pages.

---

## 4. Configure Nginx as Load Balancer

Open another terminal:

```bash
sudo nano /etc/nginx/sites-available/iptv
```

Paste:

```nginx
upstream iptv_servers {
    server 127.0.0.1:8001;
    server 127.0.0.1:8002;
}

server {
    listen 8080;

    location / {
        proxy_pass http://iptv_servers;
    }
}
```

Save:

**Ctrl + O → Enter → Ctrl + X**

Enable it:

```bash
sudo ln -s /etc/nginx/sites-available/iptv /etc/nginx/sites-enabled/iptv
```

Test configuration:

```bash
sudo nginx -t
```

Then:

```bash
sudo systemctl restart nginx
```

---

## 5. Test Load Balancing

Open:

```text
http://localhost:8080
```

Refresh the page several times.

You should alternate between:

```text
IPTV Streaming Server 1
```

and

```text
IPTV Streaming Server 2
```

This demonstrates:

```text
             ┌── Server 1 : 8001
User → Nginx ┤
             └── Server 2 : 8002
```

So you've practically demonstrated the **load-balancing part**.

---

## 6. CDN Part

You don't need to configure a commercial CDN for this college study.

Explain that in a real deployment, a CDN such as CloudFront would sit closer to users:

```text
Video Source
     ↓
Encoder / Transcoder
     ↓
Cloud Storage / Origin
     ↓
Load Balancer
     ↓
Streaming Servers
     ↓
CDN Edge Servers
     ↓
Users
```

The CDN **caches video near users**, reducing latency, buffering, and load on the origin infrastructure.

## What to show the examiner

Show:

1. Server 1 running on port `8001`
2. Server 2 running on port `8002`
3. Nginx configuration
4. `sudo nginx -t`
5. Browser at `localhost:8080`
6. Refresh showing requests distributed between the two servers
7. Draw the CDN architecture above

That is enough to demonstrate the practical concept properly.
