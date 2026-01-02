# MSFTRecon - Unified OSINT Reconnaissance Tool

MSFTRecon is now a comprehensive reconnaissance suite that combines three powerful OSINT tools:

1. **MSFTRecon** - Microsoft 365 and Azure tenant infrastructure mapping
2. **Blackbird** - Username OSINT across 131+ social networks
3. **Cr3dOv3r** - Credential reuse and breach checking

This unified tool is designed for red teamers and security professionals to perform comprehensive reconnaissance without requiring authentication.

## Features

### 🎯 MSFTRecon
- Enumerate Microsoft 365/Azure tenant information
- Discover exposed applications and services
- Identify authentication methods and federation configuration
- Check for Azure AD Connect status
- Detect Microsoft Defender for Identity (MDI) instances
- Map Azure services (App Services, Storage, CDN, B2C, etc.)

### 🔍 Blackbird  
- Search across 131+ social networks and platforms
- Async HTTP requests for supersonic speed
- Metadata extraction (name, bio, location, profile pictures)
- Export results as JSON or PDF reports
- Web interface for easy usage
- Random UserAgent rotation to avoid blocking

### 🔐 Cr3dOv3r
- Check emails against public breach databases (haveibeenpwned API)
- Retrieve plain text passwords from known leaks
- Test credential reuse across multiple platforms
- Detect captcha protection mechanisms
- Support for various login methods (forms, POST requests)


## Installation

```bash
# Clone the repository
git clone https://github.com/FacundoZS/msftrecon.git
cd msftrecon

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

## Quick Start

```bash
# See all available options
python3 unified_recon.py --help

# Run examples and usage guide
python3 examples.py

# Quick test - list all supported social networks
python3 unified_recon.py --list-sites
```

## Usage

### Unified Tool (All-in-One)

The unified_recon.py script combines all three tools:

```bash
# Run MSFTRecon only
./unified_recon.py --msftrecon -d example.com

# Search for username across social networks (Blackbird)
./unified_recon.py --blackbird -u john_doe

# Check email for credential leaks (Cr3dOv3r)
./unified_recon.py --cr3dov3r -e user@example.com

# Run all tools together
./unified_recon.py --all -d example.com -u john_doe -e user@example.com

# List all supported sites for username search
./unified_recon.py --list-sites

# Start Blackbird web interface
./unified_recon.py --web
```

### Individual Tool Usage

#### MSFTRecon (Microsoft 365/Azure Reconnaissance)
```bash
./msftrecon.py -d example.com
```

JSON output:
```bash
./msftrecon.py -d example.com -j
```

Government cloud:
```bash
./msftrecon.py -d example.gov --gov
```

China cloud:
```bash
./msftrecon.py -d example.cn --cn
```

#### Blackbird (Username OSINT)

Search for a username across 131+ social networks:
```bash
cd blackbird
python3 blackbird.py -u username
```

Run web interface:
```bash
cd blackbird
python3 blackbird.py --web
# Access http://127.0.0.1:5000 in browser
```

#### Cr3dOv3r (Credential Reuse Checker)

Check if an email appears in data breaches and test credential reuse:
```bash
cd cr3dov3r
python3 Cr3d0v3r.py user@example.com
```

Skip password checking:
```bash
cd cr3dov3r
python3 Cr3d0v3r.py -p user@example.com
```

## Sample Output

```
[+] Target Organization:
Tenant Name: Contoso
Tenant ID: 1234abcd-1234-abcd-1234-1234abcd1234

[+] Federation Information:
Namespace Type: Managed
Brand Name: Contoso
Cloud Instance: microsoftonline.com

[+] Azure AD Configuration:
Tenant Region: NA

[+] Azure AD Connect Status:
  Identity Configuration: Managed (Cloud Only)
  Authentication Type: Managed

  [!] Identity Insights:
  * Cloud-only authentication detected
  * All authentication handled in Azure AD
  * Focus on cloud-based attack vectors
```

## Red Team Usage

This unified reconnaissance suite provides comprehensive insights for red teamers:

### MSFTRecon - Identity & Infrastructure Attack Vectors

1. **Identity Attack Vectors**
   - Identifies authentication methods for targeted attacks
   - Reveals potential password spray opportunities
   - Highlights federation configurations for SAML attacks

2. **Application Attack Surface**
   - Discovers exposed enterprise applications
   - Identifies OAuth abuse opportunities
   - Reveals admin consent endpoints for phishing

3. **Infrastructure Insights**
   - Maps Azure services for lateral movement
   - Identifies B2C configurations
   - Discovers potential storage misconfigurations

4. **Security Control Awareness**
   - Detects MDI presence for evasion planning
   - Identifies conditional access configurations
   - Reveals authentication requirements

### Blackbird - Username Intelligence

- Map target's digital footprint across 131+ platforms
- Discover social media profiles for social engineering
- Find additional email addresses and contact information
- Identify metadata like location, bio, and profile pictures

### Cr3dOv3r - Credential Intelligence

- Check if target emails appear in data breaches
- Retrieve plain text passwords from known leaks
- Test credential reuse across multiple platforms
- Identify which services use the same credentials

## Disclaimer

This tool is intended for legal security assessments and penetration testing only. Users must obtain proper authorization before conducting security assessments. The authors are not responsible for any misuse or damage caused by this tool.

**Important:** 
- Blackbird and Cr3dOv3r are for educational purposes only
- Always get permission before testing credentials
- Respect privacy and data protection laws
- Follow responsible disclosure practices

## License

This project is licensed under the MIT License 

## Acknowledgments

- MSFTRecon: Based on research and techniques from various Microsoft 365 and Azure security resources, plus check_mdi.py
- Blackbird: Originally created by p1ngul1n0 - OSINT username search tool
- Cr3dOv3r: Originally created by D4Vinci - Credential reuse attack tool

## Tools Included

### Blackbird
- **Description:** OSINT tool to search for accounts by username across 131+ sites
- **Original Repository:** https://github.com/p1ngul1n0/blackbird
- **Features:** Async HTTP requests, metadata extraction, PDF export, web interface

### Cr3dOv3r  
- **Description:** Credential reuse attack tool for security testing
- **Original Repository:** https://github.com/D4Vinci/Cr3dOv3r
- **Features:** Breach data lookup via haveibeenpwned, plain text password retrieval, credential testing

## Author

FacundoZS (original MSFTRecon by jhaddix)
