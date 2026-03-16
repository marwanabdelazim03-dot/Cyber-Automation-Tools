import requests
from concurrent.futures import ThreadPoolExecutor
import os

# --- Configuration ---
TARGETS_FILE = "targets.txt"  
THREADS = 5  # Number of concurrent threads
OUTPUT_FILE = "sensitive_findings.txt"

# Common sensitive paths for Information Disclosure attacks
SENSITIVE_PATHS = [
    "/.env",
    "/.git/config",
    "/.htaccess",
    "/phpinfo.php",
    "/config.php.bak",
    "/composer.json",
    "/backup.sql",
    "/database.sqlite"
]

def check_path(url):
    url = url.strip()
    if not url:
        return
    if not url.startswith("http"):
        url = "http://" + url
    
    for path in SENSITIVE_PATHS:
        full_url = url.rstrip('/') + path
        try:
            # allow_redirects=False is used to prevent false positives from login page redirects
            response = requests.get(full_url, timeout=5, allow_redirects=False, verify=False)
            
            # Print progress for debugging and tracking
            print(f"[*] Testing: {full_url} -> Status: {response.status_code}")

            if response.status_code == 200:
                result = f"[+] ALERT: Sensitive file found at {full_url}"
                print(f"\n{result}\n")
                with open(OUTPUT_FILE, "a") as f:
                    f.write(result + "\n")
        except Exception:
            # Silently ignore connection errors to keep the output clean
            pass

def start_scanning():
    print("--- Information Disclosure Finder Started ---")
    
    if not os.path.exists(TARGETS_FILE):
        print(f"[!] {TARGETS_FILE} not found. Creating a sample file...")
        with open(TARGETS_FILE, "w") as f:
            f.write("example.com\n")
        print("[*] Please add your target URLs to targets.txt and restart the script.")
        return

    with open(TARGETS_FILE, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    if not urls:
        print("[!] targets.txt is empty. Please add target URLs.")
        return

    print(f"[*] Scanning {len(urls)} targets with {THREADS} threads...")
    print("-" * 50)

    # Using ThreadPoolExecutor for high-performance concurrent scanning
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(check_path, urls)

    print("-" * 50)
    if os.path.exists(OUTPUT_FILE):
        print(f"[*] Completed! Results saved in {OUTPUT_FILE}")
    else:
        print("[*] Scan complete. No sensitive files detected.")

if __name__ == "__main__":
    # Disable SSL warnings for testing against HTTPS sites with self-signed certificates
    requests.packages.urllib3.disable_warnings()
    start_scanning()
