import requests
import random
import time
from colorama import Fore, Style, init
import pyfiglet
from datetime import datetime, timezone

init(autoreset=True)

DISCORD_API = "https://discord.com/api/v10/users/@me"

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
]

def generate_headers(token):
    """Generate realistic headers for each request."""
    return {
        "Authorization": token,
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
    }

def get_account_creation_time(user_id):
    """Calculate the account creation time from the user ID (Snowflake)."""
    snowflake_time = (int(user_id) >> 22) + 1420070400000  
    creation_time = datetime.fromtimestamp(snowflake_time / 1000, timezone.utc)
    return creation_time.strftime('%Y-%m-%d %H:%M:%S')

def print_token_info(token, response):
    """Prints detailed information about a valid token."""
    user_data = response.json()
    username = f'{user_data["username"]}#{user_data["discriminator"]}'
    email = user_data.get("email", "Not linked")
    phone = user_data.get("phone", None)
    verified_email = user_data.get("verified", False)
    nitro = "Yes" if user_data.get("premium_type", 0) > 0 else "No"
    user_id = user_data["id"]  
    phone_verified = phone is not None and phone.strip() != ""
    creation_time = get_account_creation_time(user_id)
    days_old = (datetime.now(timezone.utc) - datetime.strptime(creation_time, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)).days
    print(f"{creation_time} | Username: {Fore.MAGENTA}{username}{Style.RESET_ALL} | Email_verified: {Fore.GREEN}{verified_email}{Style.RESET_ALL} | Phone_verified: {Fore.GREEN if phone_verified else Fore.RED}{phone_verified}{Style.RESET_ALL} | Days_old: {Fore.CYAN}{days_old}{Style.RESET_ALL}")

def check_token(token):
    """Check if a Discord token is valid."""
    headers = generate_headers(token)
    try:
        response = requests.get(DISCORD_API, headers=headers, timeout=10)
        if response.status_code == 200:
            print_token_info(token, response)
            return True
        elif response.status_code == 401:
            print(f"{Fore.RED}[INVALID]{Style.RESET_ALL} Token: {token[:10]}...{token[-5:]}")
            return False
        else:
            print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} Unexpected status code {response.status_code} for token.")
            return False
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Request failed for token: {str(e)}")
        return False

def process_tokens(tokens, valid_file, invalid_file):
    """Process tokens and classify them as valid or invalid."""
    valid_tokens, invalid_tokens = [], []
    for i, token in enumerate(tokens, start=1):
        if check_token(token):
            valid_tokens.append(token)
        else:
            invalid_tokens.append(token)
        #print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} Processed {i}/{len(tokens)} tokens.")
        time.sleep(3)
        if i % 10 == 0:
            print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Sleeping for a random time (5-7 seconds)...")
            time.sleep(random.randint(5, 7))
    with open(valid_file, "w") as vf:
        vf.write("\n".join(valid_tokens))
    with open(invalid_file, "w") as inf:
        inf.write("\n".join(invalid_tokens))
    print(f"\n{Fore.GREEN}Validation complete.{Style.RESET_ALL}\nValid tokens: {len(valid_tokens)}\nInvalid tokens: {len(invalid_tokens)}")

if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("Discord Token Tool", font="small")
    print(Fore.MAGENTA + ascii_banner)
    print(Fore.GREEN + "Made by: https://github.com/MrTimonM" + Style.RESET_ALL)
    file_name = input(f"{Fore.CYAN}Enter the token file name (e.g., tokens.txt): {Style.RESET_ALL}")
    try:
        with open(file_name, "r") as file:
            tokens = [line.strip() for line in file if line.strip()]
        if not tokens:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} No tokens found in the file.")
        else:
            print(f"{Fore.YELLOW}Total tokens found: {len(tokens)}{Style.RESET_ALL}")
            start = input(f"{Fore.GREEN}Do you want to start processing? (yes/no): {Style.RESET_ALL}").strip().lower()
            if start == "yes":
                valid_file = "valid_tokens.txt"
                invalid_file = "invalid_tokens.txt"
                process_tokens(tokens, valid_file, invalid_file)
            else:
                print(f"{Fore.RED}Process aborted.{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} File '{file_name}' not found. Please check the file name and try again.")
    except Exception as e:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} An unexpected error occurred: {e}")
