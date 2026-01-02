#!/usr/bin/env python3

"""
Example usage of the Unified OSINT Reconnaissance Tool
This script demonstrates how to use the three integrated tools
"""

import subprocess
import sys

def print_section(title):
    """Print a formatted section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")

def run_command(cmd, description):
    """Run a command and display it"""
    print(f"Command: {' '.join(cmd)}")
    print(f"Description: {description}\n")
    print("Note: This is a demonstration of the command structure.")
    print("For actual use, replace example values with real targets.\n")

def main():
    print("""
╔═══════════════════════════════════════════════════════════════╗
║     Unified OSINT Reconnaissance Tool - Usage Examples        ║
║                MSFTRecon + Blackbird + Cr3dOv3r               ║
╚═══════════════════════════════════════════════════════════════╝
    """)

    print_section("1. MSFTRecon - Microsoft 365/Azure Reconnaissance")
    print("MSFTRecon maps Microsoft 365 and Azure tenant infrastructure.")
    print("It performs comprehensive enumeration without authentication.\n")
    
    run_command(
        ["python3", "unified_recon.py", "--msftrecon", "-d", "contoso.onmicrosoft.com"],
        "Scan a Microsoft 365 domain for tenant information, services, and configuration"
    )
    
    run_command(
        ["python3", "unified_recon.py", "--msftrecon", "-d", "example.com", "-j"],
        "Output results in JSON format for automation/integration"
    )

    print_section("2. Blackbird - Username OSINT across 131+ Social Networks")
    print("Blackbird searches for a username across social media platforms,")
    print("extracting metadata like profile pictures, bios, and locations.\n")
    
    run_command(
        ["python3", "unified_recon.py", "--blackbird", "-u", "johndoe"],
        "Search for username 'johndoe' across 131+ social networks"
    )
    
    run_command(
        ["python3", "unified_recon.py", "--list-sites"],
        "List all 131+ sites that Blackbird searches"
    )
    
    print("You can also start a web interface:")
    run_command(
        ["python3", "unified_recon.py", "--web"],
        "Start Blackbird web server at http://127.0.0.1:5000"
    )

    print_section("3. Cr3dOv3r - Credential Reuse and Breach Checking")
    print("Cr3dOv3r checks if an email appears in data breaches and tests")
    print("for credential reuse across multiple platforms.\n")
    
    run_command(
        ["python3", "unified_recon.py", "--cr3dov3r", "-e", "user@example.com"],
        "Check if email appears in breaches and test credential reuse"
    )
    
    run_command(
        ["python3", "unified_recon.py", "--cr3dov3r", "-e", "user@example.com", "-np"],
        "Check breaches only, don't test for plain text passwords"
    )

    print_section("4. Combined Reconnaissance - Run All Tools")
    print("You can run all three tools in sequence for comprehensive OSINT.\n")
    
    run_command(
        ["python3", "unified_recon.py", "--all", 
         "-d", "contoso.com", 
         "-u", "johndoe", 
         "-e", "john@contoso.com"],
        "Run complete reconnaissance: tenant info + username search + credential check"
    )

    print_section("Individual Tool Usage")
    print("You can also run each tool separately:\n")
    
    print("MSFTRecon only:")
    print("  cd /path/to/msftrecon")
    print("  python3 msftrecon.py -d example.com\n")
    
    print("Blackbird only:")
    print("  cd /path/to/msftrecon/blackbird")
    print("  python3 blackbird.py -u username\n")
    
    print("Cr3dOv3r only:")
    print("  cd /path/to/msftrecon/cr3dov3r")
    print("  python3 Cr3d0v3r.py user@example.com\n")

    print_section("Important Notes")
    print("""
⚠️  LEGAL DISCLAIMER ⚠️

This tool is for AUTHORIZED security testing and educational purposes only.

- Always obtain proper authorization before testing
- Respect privacy and data protection laws
- Follow responsible disclosure practices
- Do not use for illegal activities

The authors are not responsible for misuse or damage caused by this tool.
    """)

    print_section("Installation Reminder")
    print("""
Make sure all dependencies are installed:

  pip install -r requirements.txt

If you encounter issues, try:

  python3 -m pip install --upgrade -r requirements.txt
    """)

if __name__ == "__main__":
    main()
