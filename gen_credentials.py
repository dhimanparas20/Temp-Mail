# code to accept and save user's API
from time import *
from os import system

# Defining colors
VIOLET = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
BROWN = '\033[93m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
HIGH = '\x1b[6;30;42m'
HIGHLIGHT = '\x1b[6;30;43m'

system("clear")
print(f"{VIOLET}=========================================================================================================")
# Taking the input
api = input(f"{CYAN}Enter your api {RED}(get one from {YELLOW}https://mailsac.com/api-keys) {GREEN}: ")
mail = input(f"{CYAN}Enter your mailsac temp mail id {RED}(this is mail you want to recieve emails to){GREEN}: ")
print(f"{VIOLET}========================================================================================================={END}")

# writing the inputs to another python file
x = open("credentials.py", "w")
x.write(f"#Your API is saved here\napi = '{api}' \nmail = '{mail}'")
x.close()
system("pip install geocoder")
print(f"{HIGHLIGHT}{RED}Data saved Sucessfully.{END}")
sleep(1)