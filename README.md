# 🔐 Cyber-Automation-Tools

> A collection of powerful, lightweight tools designed for cybersecurity professionals, penetration testers, and security enthusiasts. Automate reconnaissance, intelligence gathering, and vulnerability assessment with precision and speed.

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![GitHub Commits](https://img.shields.io/badge/commits-9-lightgrey.svg)]()

---

## 📋 Table of Contents

- [Overview](#overview)
- [Tools](#tools)
  - [Sensitive Finder](#sensitive-finder)
  - [Subdomain Monitor](#subdomain-monitor)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [Contact](#contact)

---

## 🎯 Overview

**Cyber-Automation-Tools** is a Python-powered automation toolkit built to streamline cybersecurity workflows. Whether you're conducting reconnaissance, monitoring infrastructure, or searching for exposed sensitive data, these tools are designed to save time and reduce manual effort.

Perfect for:
- 🔍 Security researchers
- 🎯 Penetration testers
- 🛡️ Bug bounty hunters
- 🔐 Security teams
- 📚 Students learning cybersecurity

---

## 🛠️ Tools

### Sensitive Finder

**Purpose**: Automatically detect and catalog sensitive files, credentials, API keys, and confidential information exposed in public repositories, databases, or filesystem locations.

**Key Features**:
- Pattern-based detection of common secret formats
- Multi-source scanning (GitHub, GitLab, public databases)
- Customizable regex patterns for sensitive data
- Organized output reporting
- False positive filtering

**Use Cases**:
- OSINT and reconnaissance
- Internal security audits
- GitHub secret scanning
- Compliance monitoring

**Status**: `In Development` 🚀

---

### Subdomain Monitor

**Purpose**: Continuously track and monitor subdomains of target domains, detecting new discoveries, deletions, and changes to help identify attack surface expansion.

**Key Features**:
- Automated subdomain enumeration
- Change detection & alerts
- Historical tracking
- Integration with popular enumeration tools
- Scheduled monitoring
- Clean reporting with delta analysis

**Use Cases**:
- Infrastructure monitoring
- Attack surface management
- New service detection
- Security team notifications

**Status**: `Active Development` 🔄

---

## ⚡ Features

- **Automation First**: Reduce manual security tasks with intelligent automation
- **Python-Powered**: Easy to extend, modify, and integrate with other tools
- **Lightweight**: Minimal dependencies, fast execution
- **Customizable**: Configure behavior to match your security needs
- **Easy Integration**: Works seamlessly with other security tools and workflows
- **Well-Documented**: Clear examples and usage patterns

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Clone the Repository

```bash
git clone https://github.com/marwanabdelazim03-dot/Cyber-Automation-Tools.git
cd Cyber-Automation-Tools
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

*Or install individual tool dependencies:*

```bash
# For Sensitive Finder
pip install requests beautifulsoup4 python-dotenv

# For Subdomain Monitor
pip install dnspython requests aiohttp
```

---

## 🚀 Usage

### Sensitive Finder

```bash
# Basic usage - scan with default patterns
python sensitive_finder/finder.py --target <domain_or_repo>

# Custom regex patterns
python sensitive_finder/finder.py --target <target> --patterns config.json

# Output to file
python sensitive_finder/finder.py --target <target> --output results.json
```

**Example**:
```bash
python sensitive_finder/finder.py --target github.com/example/repo --output findings.json
```

---

### Subdomain Monitor

```bash
# Enumerate subdomains
python subdomain_monitor/monitor.py --domain example.com

# Run scheduled monitoring (checks every 24h)
python subdomain_monitor/monitor.py --domain example.com --schedule daily

# Compare with previous scan
python subdomain_monitor/monitor.py --domain example.com --compare
```

**Example**:
```bash
python subdomain_monitor/monitor.py --domain example.com --output subdomains.json --schedule
```

---

## 📋 Requirements

### Core Dependencies
- `requests` - HTTP requests
- `python-dotenv` - Environment variable management
- `dnspython` - DNS operations
- `aiohttp` - Async HTTP requests

### Optional Dependencies
- `beautifulsoup4` - HTML parsing
- `selenium` - Browser automation
- `shodan` - Shodan API integration

---

## ⚖️ Disclaimer

**Important Legal Notice**:

These tools are provided **for educational and authorized security testing purposes only**. Users are solely responsible for complying with all applicable laws and regulations, including:

- 🔒 Only use these tools on systems you own or have explicit written permission to test
- 📜 Unauthorized access to computer systems is illegal in most jurisdictions
- 🛡️ Always obtain proper authorization before conducting security assessments
- 📋 Follow responsible disclosure practices

The authors of this project are **not responsible** for any misuse, damage, or legal consequences resulting from unauthorized use of these tools.

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Guidelines
- Follow PEP 8 style guide
- Add docstrings to functions
- Include examples in your PR description
- Update README if adding new features

---

## 📞 Contact & Support

- **GitHub**: [@marwanabdelazim03-dot](https://github.com/marwanabdelazim03-dot)
- **Email**: marwanabdelazim03@gmail.com
- **Issues**: [Report bugs here](https://github.com/marwanabdelazim03-dot/Cyber-Automation-Tools/issues)

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Thanks to the cybersecurity community for tools and methodologies that inspired this project
- Special thanks to all contributors and users who provide feedback

---

**Made with ❤️ by [Marwan Abdelazim](https://github.com/marwanabdelazim03-dot)**

*Last Updated: March 2026*
