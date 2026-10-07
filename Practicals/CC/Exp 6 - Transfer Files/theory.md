# Experiment 6 — Transfer Files from One Virtual Machine to Another

### Aim

To establish communication between two Ubuntu virtual machines and securely transfer files using **SSH and SCP**.

### Requirements

- Oracle VirtualBox
- Ubuntu01
- Ubuntu02
- Both VMs connected to the same NAT Network
- OpenSSH Server

## Procedure

### Step 1 — Create/Start Two Virtual Machines

Start both VMs:

```text
Ubuntu01
Ubuntu02
```

Both machines should be running simultaneously.

### Step 2 — Configure the VirtualBox Network

Power off the VMs before changing network settings.

In VirtualBox, create a NAT Network:

**Tools → Network → NAT Networks → Create**

Configure:

```text
Name: NatNetwork1
IPv4 Prefix: 10.10.0.0/24
Enable DHCP: ✓
```

For **both Ubuntu01 and Ubuntu02**:

**Settings → Network → Adapter 1**

Set:

```text
Enable Network Adapter: ✓
Attached to: NAT Network
Name: NatNetwork1
Virtual Cable Connected: ✓
```

Start both VMs.

### Step 3 — Check IP Addresses

On **Ubuntu01**:

```bash
hostname -I
```

In our practical:

```text
Ubuntu01 → 10.10.0.5
```

On **Ubuntu02**:

```bash
hostname -I
```

We obtained:

```text
Ubuntu02 → 10.10.0.4
```

The exact addresses may be different because DHCP assigns them automatically.

### Step 4 — Test Communication

From **Ubuntu01**, ping Ubuntu02:

```bash
ping -c 4 10.10.0.4
```

From **Ubuntu02**, ping Ubuntu01:

```bash
ping -c 4 10.10.0.5
```

Receiving replies confirms that the VMs can communicate.

### Step 5 — Install SSH Server on Ubuntu02

On **Ubuntu02**:

```bash
sudo apt update
sudo apt install openssh-server -y
```

If Ubuntu reports that `dpkg` was interrupted, first run:

```bash
sudo dpkg --configure -a
sudo apt --fix-broken install -y
```

Then install OpenSSH again:

```bash
sudo apt install openssh-server -y
```

### Step 6 — Start SSH

On Ubuntu02:

```bash
sudo systemctl enable --now ssh
```

Check:

```bash
sudo systemctl status ssh
```

The expected status is:

```text
Active: active (running)
```

Press `q` to exit.

### Step 7 — Create a File on Ubuntu01

On **Ubuntu01**:

```bash
echo "Hello from Ubuntu01 - Experiment 6" > test.txt
```

Verify:

```bash
cat test.txt
```

Output:

```text
Hello from Ubuntu01 - Experiment 6
```

### Step 8 — Transfer the File Using SCP

On **Ubuntu01**:

```bash
scp test.txt ubuntu02@10.10.0.4:/home/ubuntu02/
```

For the first connection, SSH may ask:

```text
Are you sure you want to continue connecting?
```

Enter:

```text
yes
```

Then enter the **Ubuntu02 user password**.

A successful transfer shows approximately:

```text
test.txt                100%
```

### Step 9 — Verify the File on Ubuntu02

Go to **Ubuntu02** and run:

```bash
ls
```

You should find:

```text
test.txt
```

Display its contents:

```bash
cat test.txt
```

Output:

```text
Hello from Ubuntu01 - Experiment 6
```

## Important Commands to Remember

```bash
hostname -I
ping -c 4 <IP>
sudo apt install openssh-server -y
sudo systemctl enable --now ssh
scp file.txt username@IP:/destination/
ls
cat file.txt
```

### Viva Points

- **SSH:** Secure Shell; provides secure remote communication.
- **SCP:** Secure Copy Protocol; securely transfers files between systems using SSH.
- **SSH default port:** `22`.
- **`hostname -I`:** Displays the system's IP addresses.
- **NAT Network:** Allows multiple VMs on the same virtual NAT network to communicate while also providing network access.
- **DHCP:** Automatically assigns IP addresses to the VMs.

### Result

**Successfully established communication between Ubuntu01 and Ubuntu02 and securely transferred a file from one virtual machine to another using SCP over SSH.**
