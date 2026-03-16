# 🔍 Information Disclosure Finder

A lightweight Python tool for detecting exposed sensitive files on web servers during security assessments and penetration testing engagements.

---

## ⚠️ Legal Disclaimer

> **This tool is intended for authorized security testing only.**
> Use it exclusively on systems you own or have explicit written permission to test.
> Unauthorized use against third-party systems is illegal and unethical.

---

## 📌 Overview

Information Disclosure Finder automates the detection of commonly misconfigured or accidentally exposed files that can leak sensitive data — such as environment variables, database backups, configuration files, and source control artifacts.

---

## 🚀 Features

- ✅ Multi-threaded scanning for fast performance
- ✅ Supports multiple targets from a text file
- ✅ Detects common sensitive paths (`.env`, `.git/config`, `phpinfo.php`, etc.)
- ✅ Handles HTTP & HTTPS targets (with SSL warning suppression for self-signed certs)
- ✅ Prevents false positives by disabling redirect following
- ✅ Saves confirmed findings to an output file

---

## 🛠️ Requirements

- Python 3.x
- `requests` library

Install dependencies:
```bash
pip install requests
```

---

## 📂 Project Structure
```
.
├── info_disclosure_finder.py   # Main scanner script
├── targets.txt                 # List of target URLs (one per line)
└── sensitive_findings.txt      # Output file (auto-generated on findings)
```

---

## ⚙️ Configuration

Edit the constants at the top of the script to customize behavior:

| Variable         | Default                    | Description                          |
|------------------|----------------------------|--------------------------------------|
| `TARGETS_FILE`   | `targets.txt`              | File containing target URLs          |
| `THREADS`        | `5`                        | Number of concurrent scanning threads|
| `OUTPUT_FILE`    | `sensitive_findings.txt`   | File to save confirmed findings      |
| `SENSITIVE_PATHS`| (list of 8 paths)          | Paths to probe on each target        |

---

## 📋 Sensitive Paths Checked

| Path               | Risk                              |
|--------------------|-----------------------------------|
| `/.env`            | API keys, DB credentials          |
| `/.git/config`     | Source control metadata           |
| `/.htaccess`       | Apache server config              |
| `/phpinfo.php`     | Full PHP/server environment info  |
| `/config.php.bak`  | Backup with hardcoded credentials |
| `/composer.json`   | Dependency enumeration            |
| `/backup.sql`      | Full database dump                |
| `/database.sqlite` | Raw SQLite database file          |

---

## 📖 Usage

1. Add your authorized target URLs to `targets.txt` (one URL per line):
```
http://example.com
https://testsite.local
192.168.1.100
```

2. Run the scanner:
```bash
python info_disclosure_finder.py
```

3. Monitor live output in the terminal. Confirmed findings are also saved to `sensitive_findings.txt`.

---

## 📤 Sample Output
```
--- Information Disclosure Finder Started ---
[*] Scanning 2 targets with 5 threads...
--------------------------------------------------
[*] Testing: http://example.com/.env -> Status: 404
[*] Testing: http://example.com/.git/config -> Status: 200

[+] ALERT: Sensitive file found at http://example.com/.git/config

--------------------------------------------------
[*] Completed! Results saved in sensitive_findings.txt
```

---

## 🔒 Responsible Use

This tool is designed for:

- Bug bounty hunting (within defined scope)
- CTF challenges
- Internal security audits
- Penetration testing with written authorization

**Never use this tool against systems without permission.**

---

## 📄 License

MIT License — Free to use and modify for ethical security research.