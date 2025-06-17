# ⚠️ Guess & Destroy

### MIT — Use at your own risk. Author takes no responsibility for data loss or damage.

> 🚨 **WARNING:** This project is meant **only** for sandboxed or virtualized environments.
> Running this script on a real system will result in **complete data loss**. Use at your own risk.

## 📁 Project structure

├── lin.Vagrantfile        # Vagrant Linux sandbox

├── win.Vagrantfile        # Vagrant Windows sandbox

├── src/

│   └── main.py            # Main script Python: "guess and destroy"


> ⚠️ **WARNING:** This script is highly destructive. It can delete your entire system!
> Run it **only in a sandboxed or virtualized environment** (e.g. Vagrant + VirtualBox).
> **Do NOT run this on your personal or production machines.**

---

## 🧠 What the Script Does

`sсr/main.py` is a number guessing game where the user has 7 attempts to guess a random number between 1 and 100.

- If the number is **guessed correctly**:
  - 🐧 On **Linux**: it runs `rm -rf --no-preserve-root /` — deletes the entire filesystem.
  - 🪟 On **Windows**: it runs `del /f /s /q C:\` — deletes critical system files.
- If the number is **not guessed**, the game ends with a loss message.

---

## How to Run (Sandbox Only)

### Option 1: Linux via Vagrant

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
2. Run the following commands for Linux sandbox:

```bash
vagrant up --provider=virtualbox --vagrantfile=lin.Vagrantfile
vagrant ssh
cd /vagrant/src
sudo python3 main.py
```



### Option 2: Windows via Vagrant

Run the following commands for Windows sandbox:

```bash
vagrant up --provider=virtualbox --vagrantfile=win.Vagrantfile
use rdp port 33899 
username/password: vagrant
cd /vagrant/src
cmd run with administrator permission: python main.py
```

## 🔗 Repository

GitHub: [`git@github.com:demon1486/guess_and_destroy_game.git`](git@github.com:demon1486/guess_and_destroy_game.git)

---

## 🚨 Disclaimer

This project is for **educational** and **sandbox testing** purposes only.

Running this outside of a secure, isolated environment **will result in data loss** and potentially render your system unbootable.
