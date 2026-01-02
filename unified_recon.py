#!/usr/bin/env python3

"""
Unified OSINT Reconnaissance Tool
Combines MSFTRecon, Blackbird (username OSINT), and Cr3dOv3r (credential reuse)
"""

import argparse
import sys
import os
import subprocess
import asyncio

# Add paths for submodules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'blackbird'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'cr3dov3r'))

from colorama import init, Fore

init()

def print_banner():
    print(Fore.CYAN + """
╔═══════════════════════════════════════════════════════════════╗
║           Unified OSINT Reconnaissance Tool                    ║
║  MSFTRecon + Blackbird + Cr3dOv3r                             ║
╚═══════════════════════════════════════════════════════════════╝
    """ + Fore.RESET)

def run_msftrecon(args):
    """Run MSFTRecon tool"""
    print(Fore.GREEN + "\n[+] Running MSFTRecon...\n" + Fore.RESET)
    # Run msftrecon as subprocess to avoid import conflicts
    cmd = [sys.executable, os.path.join(os.path.dirname(__file__), 'msftrecon.py'), '-d', args.domain]
    if args.json:
        cmd.append('-j')
    if hasattr(args, 'gov') and args.gov:
        cmd.append('--gov')
    if hasattr(args, 'cn') and args.cn:
        cmd.append('--cn')
    subprocess.run(cmd)

def run_blackbird(args):
    """Run Blackbird username search"""
    print(Fore.GREEN + "\n[+] Running Blackbird username search...\n" + Fore.RESET)
    # Change to blackbird directory
    original_dir = os.getcwd()
    blackbird_dir = os.path.join(os.path.dirname(__file__), 'blackbird')
    os.chdir(blackbird_dir)
    
    try:
        from blackbird import findUsername
        asyncio.run(findUsername(args.username))
    finally:
        os.chdir(original_dir)

def run_cr3dov3r(args):
    """Run Cr3dOv3r credential checker"""
    print(Fore.GREEN + "\n[+] Running Cr3dOv3r credential checker...\n" + Fore.RESET)
    # Change to cr3dov3r directory
    original_dir = os.getcwd()
    cr3dov3r_dir = os.path.join(os.path.dirname(__file__), 'cr3dov3r')
    os.chdir(cr3dov3r_dir)
    
    try:
        # Import cr3dov3r modules
        import Cr3d0v3r as cr3d
        
        # Create args for cr3dov3r
        cr3d_args = argparse.Namespace()
        cr3d_args.email = args.email
        cr3d_args.p = args.p if hasattr(args, 'p') else False
        cr3d_args.np = args.np if hasattr(args, 'np') else False
        cr3d_args.q = True  # Quiet mode to avoid duplicate banner
        
        # Run cr3dov3r
        cr3d.args = cr3d_args
        cr3d.email = args.email
        cr3d.main()
    finally:
        os.chdir(original_dir)

def main():
    parser = argparse.ArgumentParser(
        description='Unified OSINT Reconnaissance Tool - MSFTRecon + Blackbird + Cr3dOv3r',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run MSFTRecon on a domain
  ./unified_recon.py --msftrecon -d example.com
  
  # Search for username across social networks
  ./unified_recon.py --blackbird -u john_doe
  
  # Check email for credential leaks
  ./unified_recon.py --cr3dov3r -e user@example.com
  
  # Run all tools (requires domain, username, and email)
  ./unified_recon.py --all -d example.com -u john_doe -e user@example.com
        """)
    
    # Tool selection
    parser.add_argument('--msftrecon', action='store_true', help='Run MSFTRecon (Microsoft 365/Azure recon)')
    parser.add_argument('--blackbird', action='store_true', help='Run Blackbird (username OSINT)')
    parser.add_argument('--cr3dov3r', action='store_true', help='Run Cr3dOv3r (credential reuse checker)')
    parser.add_argument('--all', action='store_true', help='Run all tools')
    
    # MSFTRecon arguments
    parser.add_argument('-d', '--domain', help='Domain for MSFTRecon (e.g., example.com)')
    parser.add_argument('-j', '--json', action='store_true', help='Output in JSON format (MSFTRecon)')
    parser.add_argument('--gov', action='store_true', help='Query government tenancy (MSFTRecon)')
    parser.add_argument('--cn', action='store_true', help='Query Chinese tenancy (MSFTRecon)')
    
    # Blackbird arguments
    parser.add_argument('-u', '--username', help='Username to search (Blackbird)')
    parser.add_argument('--list-sites', action='store_true', help='List supported sites (Blackbird)')
    parser.add_argument('--web', action='store_true', help='Run Blackbird web server')
    
    # Cr3dOv3r arguments
    parser.add_argument('-e', '--email', help='Email to check for leaks (Cr3dOv3r)')
    parser.add_argument('-p', action='store_true', help='Don\'t check for leaks or passwords (Cr3dOv3r)')
    parser.add_argument('-np', action='store_true', help='Don\'t check for plain text passwords (Cr3dOv3r)')
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    # Handle special cases
    if args.list_sites:
        import json
        blackbird_data = os.path.join(os.path.dirname(__file__), 'blackbird', 'data.json')
        with open(blackbird_data) as f:
            data = json.load(f)
            print(Fore.YELLOW + f"\n[!] Blackbird supports {len(data['sites'])} sites:\n" + Fore.RESET)
            for i, site in enumerate(data['sites'], 1):
                print(f"{i}. {site['app']}")
        return
    
    if args.web:
        print(Fore.YELLOW + "[!] Starting Blackbird web server..." + Fore.RESET)
        original_dir = os.getcwd()
        os.chdir(os.path.join(os.path.dirname(__file__), 'blackbird'))
        try:
            import webserver
        finally:
            os.chdir(original_dir)
        return
    
    # Determine which tools to run
    run_all = args.all
    run_msft = args.msftrecon or run_all
    run_bb = args.blackbird or run_all
    run_cr3d = args.cr3dov3r or run_all
    
    # If no tool specified, show help
    if not (run_msft or run_bb or run_cr3d):
        parser.print_help()
        return
    
    # Validate required arguments
    if run_msft and not args.domain:
        print(Fore.RED + "[-] Error: --domain is required for MSFTRecon" + Fore.RESET)
        return
    
    if run_bb and not args.username:
        print(Fore.RED + "[-] Error: --username is required for Blackbird" + Fore.RESET)
        return
    
    if run_cr3d and not args.email:
        print(Fore.RED + "[-] Error: --email is required for Cr3dOv3r" + Fore.RESET)
        return
    
    # Run selected tools
    if run_msft:
        try:
            run_msftrecon(args)
        except Exception as e:
            print(Fore.RED + f"[-] Error running MSFTRecon: {e}" + Fore.RESET)
    
    if run_bb:
        try:
            run_blackbird(args)
        except Exception as e:
            print(Fore.RED + f"[-] Error running Blackbird: {e}" + Fore.RESET)
    
    if run_cr3d:
        try:
            run_cr3dov3r(args)
        except Exception as e:
            print(Fore.RED + f"[-] Error running Cr3dOv3r: {e}" + Fore.RESET)
    
    print(Fore.GREEN + "\n[+] All selected reconnaissance tasks completed!" + Fore.RESET)

if __name__ == "__main__":
    main()
