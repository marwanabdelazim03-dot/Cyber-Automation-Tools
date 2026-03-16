# 🔍 Subdomain Monitor

An automated subdomain monitoring tool that scans a target domain for newly discovered subdomains and sends real-time Telegram notifications. Useful for bug bounty hunters and security researchers who want to be the first to spot new attack surfaces.

---

## ✨ Features

- 🔄 Continuously monitors a domain for new subdomains (every hour)
- 📩 Instant Telegram alerts when new subdomains are discovered
- 💾 Persists known subdomains to a local file to track changes over time
- ⚡ Uses [subfinder](https://github.com/projectdiscovery/subfinder) for fast, passive enumeration

---

## 📋 Requirements

- Python 3.x
- [subfinder](https://github.com/projectdiscovery/subfinder/releases) (must be in PATH)
- A Telegram Bot Token and Chat ID

### Install Python dependencies

```bash
pip install requests
```

### Install subfinder

Download the latest release for your OS from:
👉 https://github.com/projectdiscovery/subfinder/releases

Then add the binary to your system PATH.

---

## ⚙️ Configuration

Open `subdomain_monitor.py` and edit the following variables:

```python
DOMAIN = "example.com"           # Target domain to monitor
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"  # Your Telegram bot token
CHAT_ID = "YOUR_CHAT_ID"           # Your Telegram chat ID
```

### How to get your Telegram Bot Token

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` and follow the instructions
3. Copy the token provided

### How to get your Chat ID

1. Send any message to your bot
2. Open in your browser:
   ```
   https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
   ```
3. Find `"chat": {"id": XXXXXXXXX}` — that's your Chat ID

---

## 🚀 Usage

```bash
python subdomain_monitor.py
```

The script will:
1. Scan the target domain using `subfinder`
2. Compare results against previously known subdomains
3. Send a Telegram notification for any new findings
4. Sleep for 1 hour, then repeat

---

## 📁 Output

A file named `<domain>_subdomains.txt` will be created in the same directory, storing all discovered subdomains.

Example: `google.com_subdomains.txt`

---

## 📸 Example Notification

```
🔔 New subdomains found for google.com:
mail.google.com
vpn.google.com
staging.google.com
```

---

## ⚠️ Disclaimer

This tool is intended for **authorized security research and bug bounty programs only**.  
Always ensure you have permission before scanning any domain.  
The author is not responsible for any misuse.

---

## 🛠️ Built With

- [Python](https://www.python.org/)
- [subfinder](https://github.com/projectdiscovery/subfinder) by ProjectDiscovery
- [Telegram Bot API](https://core.telegram.org/bots/api)
