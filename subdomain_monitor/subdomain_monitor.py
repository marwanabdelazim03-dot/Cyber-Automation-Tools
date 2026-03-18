import requests
import time
import subprocess
import os

# --- Configuration ---
DOMAIN = "google.com"  # The domain you want to monitor
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"  # Your Telegram bot token
CHAT_ID = "YOUR_CHAT_ID"  # Your Telegram chat ID
FILE_NAME = f"{DOMAIN}_subdomains.txt"

def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Error sending telegram message: {e}")

def get_subdomains(domain):
    print(f"[*] Scanning {domain} for subdomains...")
    # We'll use a tool like subfinder if available, or fall back to an external API
    # Here we assume we're trying something simple as a starting point
    try:
        # This simulates the discovery process; in practice we use tools like subfinder or amass
        result = subprocess.check_output(f"subfinder -d {domain} -silent", shell=True)
        return set(result.decode().splitlines())
    except:
        print("[!] Subfinder not found, using a fallback method or empty list.")
        return set()

def monitor():
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()

    known_subs = set(line.strip() for line in open(FILE_NAME))
    
    while True:
        current_subs = get_subdomains(DOMAIN)
        new_subs = current_subs - known_subs
        
        if new_subs:
            msg = f"🔔 New subdomains found for {DOMAIN}:\n" + "\n".join(new_subs)
            print(msg)
            send_telegram_msg(msg)
            
            # Update the file with newly discovered subdomains
            with open(FILE_NAME, "a") as f:
                for sub in new_subs:
                    f.write(sub + "\n")
            known_subs.update(new_subs)
        else:
            print("[*] No new subdomains found. Sleeping...")
            
        time.sleep(3600)  # Re-scan every hour

if __name__ == "__main__":
    monitor()
