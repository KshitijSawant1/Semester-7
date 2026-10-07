## Experiment 2 — Complete Steps: Install Ubuntu Linux on VirtualBox

### Aim
To install **Oracle VirtualBox** and create a virtual machine with **Ubuntu Linux** as the guest operating system.

### Step 1 — Install VirtualBox
1. Download **Oracle VirtualBox**.
2. Run the installer.
3. Follow **Next → Install → Finish**.
4. Open VirtualBox.

### Step 2 — Download Ubuntu ISO File

1. Go to the official Ubuntu download page : https://ubuntu.com/download/desktop
2. Download **Ubuntu Desktop**.
3. Select the ISO according to your processor:
   - **Intel/AMD PC:** AMD64/x86-64 ISO
   - **Apple Silicon / ARM:** ARM64 ISO
4. Save the `.iso` file in an easily accessible folder.

In our practical, we used:

```text
ubuntu-26.04-desktop-arm64.iso
```

**ISO file:** A disk-image file containing the operating-system installation files.

### Step 3 — Create a New Virtual Machine

Open VirtualBox and click:

**New**

Enter:

```text
VM Name: Ubuntu01
Type: Linux
Distribution: Ubuntu
ISO Image: Select downloaded Ubuntu ISO
```

We unchecked **Proceed with Unattended Installation** so that Ubuntu could be installed manually.

### Step 4 — Configure Hardware

Under **Specify Virtual Hardware**, configure:

```text
RAM: 4096 MB (4 GB)
Processors: 2
```

### Step 5 — Configure Virtual Hard Disk

Create a virtual hard disk:

```text
Disk Size: 25 GB
Disk Type: VDI
Allocation: Dynamically Allocated
```

A **dynamically allocated disk** grows as data is stored instead of immediately occupying the entire 25 GB.

Click **Finish**.

### Step 6 — Start the VM

Select:

**Ubuntu01 → Start**

VirtualBox boots the VM using the attached Ubuntu ISO.

### Step 7 — Install Ubuntu

Follow the Ubuntu installer:

**Language → Keyboard → Install Ubuntu → Interactive Installation → Default Selection**

For disk configuration, select:

**Erase disk and install Ubuntu**

This erases only the **virtual disk**, not the physical computer's storage.

### Step 8 — Create Ubuntu Account

Enter:

```text
Name: KS
Computer Name: ubuntu01
Username: ks
Password: your chosen password
```

Complete the installation.

### Step 9 — Restart Ubuntu

After installation:

**Restart Now**

If prompted to remove the installation medium, press **Enter**.

If the ISO remains attached:

**VirtualBox → Devices → Optical Drives → Remove Disk from Virtual Drive**

Ubuntu should now boot from the virtual hard disk.

### Step 10 — Login and Open Terminal

Log in to Ubuntu.

Open Terminal:

```text
Ctrl + Alt + T
```

### Step 11 — Run Basic Linux Commands

Current directory:

```bash
pwd
```

List files:

```bash
ls
```

Current user:

```bash
whoami
```

System/kernel information:

```bash
uname -a
```

IP/network information:

```bash
ip addr
```

### Step 12 — Test Internet Connection

```bash
ping -c 4 google.com
```
