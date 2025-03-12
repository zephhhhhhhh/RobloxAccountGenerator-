import requests
import time
import random
import string
from colorama import Fore, Style, init

init()

def ge():
    characters = string.ascii_letters + string.digits
    if random.choice([True, False]):   
        pos = random.randint(1, 2)   
        base_chars = random.choices(string.ascii_letters + string.digits, k=3)
        base_chars.insert(pos, '_')
        return ''.join(base_chars)
    else:
        return ''.join(random.choices(characters, k=4))

def webhook(username):
    webhook_url = "ENTER YOUR DISCORD WEBHOOK" # DISCORD WEBHOOK
    message = f"```diff\n+ @everyone, account found: {username}\n```" 
    data = {"content": message}
    try:
        requests.post(webhook_url, json=data)
    except requests.exceptions.RequestException as e:
        print(Fore.YELLOW + f"error: {e}" + Style.RESET_ALL)

def usernamecheck(username):
    url = f"https://auth.roblox.com/v1/usernames/validate?Username={username}&Birthday=2000-01-01"
    try:
        response = requests.get(url)
        response_data = response.json()

        code = response_data.get("code")
        if code == 0:
            print(Fore.GREEN + f"VALID: {username}" + Style.RESET_ALL)
            webhook(username)
        elif code == 1:
            print(Fore.LIGHTBLACK_EX + f"TAKEN: {username}" + Style.RESET_ALL)
        elif code == 2:
            print(Fore.RED + f"CENSORED: {username}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"bruh ({code}): {username}" + Style.RESET_ALL)

    except requests.exceptions.RequestException as e:
        print(Fore.YELLOW + f"glitch {username}: {e}" + Style.RESET_ALL)

def main():
    for _ in range(1):  # CHANGE THE NUMBER TO WHAT YOU WANT 
        username = ge()
        usernamecheck(username)
        time.sleep(0.05)

if __name__ == "__main__":
    main()
