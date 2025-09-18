from colorama import Fore, init
from socket import gethostbyname
import webbrowser
import os
import sys

# Initialize colorama for Windows compatibility
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def open_links():
    print(Fore.CYAN + "\n[+] Opening official links...")
    webbrowser.open_new_tab("https://serialkey.top/")
    webbrowser.open_new_tab("https://t.me/darkvaiadmin")

def Miscript():
    clear_screen()
    print(Fore.GREEN + "========================================")
    print(Fore.GREEN + "     Welcome to IP Scanner")
    print(Fore.GREEN + "         by: Darkboss1bd")
    print(Fore.GREEN + "========================================")
    print(Fore.YELLOW + "Official Website: https://serialkey.top/")
    print(Fore.YELLOW + "Telegram ID: https://t.me/darkvaiadmin")
    print(Fore.GREEN + "========================================\n")

    try:
        target = input(Fore.CYAN + "[*] Enter the Host (e.g., google.com): " + Fore.WHITE)
        if not target.strip():
            print(Fore.RED + "\n[!] Error: Host cannot be empty!")
            input(Fore.YELLOW + "\nPress Enter to retry...")
            Miscript()

        print(Fore.YELLOW + "\n[+] Resolving IP Address...")
        targetIP = gethostbyname(target)
        print(Fore.GREEN + "\n[✓] Target IP ===>", Fore.WHITE + targetIP)
        print(Fore.GREEN + "+------------------------------------+")

        input(Fore.CYAN + "\n[+] Press Enter to scan again or Ctrl+C to exit...")

    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[!] Exiting... Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"\n[!] Error: {e}")
        input(Fore.YELLOW + "\nPress Enter to retry...")
    
    Miscript()  # Recursive call for continuous use

# Auto-open links when script starts
open_links()

# Start the tool
if __name__ == "__main__":
    Miscript()
