import requests
import os
from time import sleep
import sys
import threading

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PINK = '\033[95m'

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_tor_service():
    try:
        print(colors.OKBLUE + "\nChecking Tor Service." + colors.ENDC)
        response = os.system("service tor status > /dev/null 2>&1")
        if response != 0:
            print(colors.FAIL + "Tor Service Running X" + colors.ENDC)
            start_tor_service()
        else:
            print(colors.OKGREEN + "Tor Service Running ✔" + colors.ENDC)
    except Exception as e:
        print(colors.FAIL + "\nFailed to check Tor service status:", e + colors.ENDC)
        sys.exit(1)


def start_tor_service():
    print(colors.OKBLUE + "\nStarting Tor Service" + colors.ENDC)
    try:
        os.system("sudo service tor start > /dev/null 2>&1")
        print(colors.OKGREEN + "\nTor service started successfully." + colors.ENDC)
        clear_terminal()
        Main()
    except Exception as e:
        print(colors.FAIL + "\nFailed to start Tor service:", e + colors.ENDC)
        sys.exit(1)

def spinner_effect():
    spinner = ['|', '/', '-', '\\']
    i = 0
    while True:
        sys.stdout.write("\r" + colors.BOLD + "Fetching IP... " + colors.OKCYAN + spinner[i] + colors.ENDC)
        sys.stdout.flush()
        sleep(0.1)
        i = (i + 1) % 4

def Main():
    clear_terminal()
    print(colors.PINK + """░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░    ░▒▓██████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     
░▒▓█▓▒░       ░▒▓█████████████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     
                                                                                                          
                                                                                                          
Follow on instagram: @pwnkitty""" + colors.ENDC)

    change = int(input(colors.WARNING + "\nEnter the interval (in seconds) for changing your IP: " + colors.ENDC))
    check_tor_service()
    url = "https://httpbin.org/ip"
    proxy = {'http':'socks5://127.0.0.1:9050', 'https':'socks5://127.0.0.1:9050'}

    spinner_thread = threading.Thread(target=spinner_effect)
    spinner_thread.start()

    while True:
        try:
            response = requests.get(url, proxies=proxy)
            if response.status_code == 200:
                sys.stdout.write("\r\033[K")
                print(colors.OKGREEN + "Your Current IP :: {}".format(response.json().get("origin")) + colors.ENDC)
            else:
                sys.stdout.write("\r\033[K")
                print(colors.FAIL + "Failed To Fetch Current IP" + colors.ENDC)
        except Exception as e:
            sys.stdout.write("\r\033[K")
            print(colors.FAIL + "An error occurred:", e + colors.ENDC)
        sleep(change)

if __name__ == "__main__":
    Main()
