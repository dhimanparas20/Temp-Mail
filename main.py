#Import Libraries
import requests, json 
import os.path
from os import path
from os import system
from time import *
from credentials import api,mail
import geocoder

# Colors
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

# Adding API headers
headers = {'Mailsac-Key': api}

# Fetching DATA Using the API
req = requests.get(f'https://mailsac.com/api/addresses/{mail}/messages', headers=headers)
jon = req.json()

# Loop to revert back to main menu
def loop():
  input(f"{VIOLET} PRESS ENTER TO RETURN TO MAIN MENU")
  system("python3 main.py")

#MST Banner
system("clear") #Clears the previous session screen
print (VIOLET+"#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print (RED+"#------------------==================================================---------------------#")
print ("#------------------"+HIGHLIGHT+"| WELCOME TO COMPILING SCRIPTS BY MST PRODUCTIONS|"+END+RED+"---------------------#")
print ("#------------------==================================================---------------------#")
print (VIOLET+"#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print ("#-----------------------------------------------------------------------------------------#")
print ("#----------------------------------------------------------------------"+HIGHLIGHT+CYAN+"BY: Paras Dhiman --#"+END)
print ()
sleep(1)

# Diaplay main Menu
print (RED+"------------------------------------------------")
print (VIOLET+"            Choose your Choice                  ")
print (RED+"------------------------------------------------")
print (GREEN+"0: Save my API and prefrences")
print ("1: Read the last received mail.")
print ("2: List and read mails.")
print ("3: Delete Mails.")
print ("4: Check current email and its validity.")
print ("69: Exit"+END)
# User input for main menu choices.
print (RED+"================================================")
inp = int(input(f"{CYAN}Enter your choice (number){YELLOW}:"))
print (RED+"================================================")
system("clear")

# Response based condtions
# Saving of API and Mailsac Email address.
if inp == 0:
  system("python3 gen_credentials.py\n")
  loop()

# Showing of Last Email.
elif inp == 1:
  print(f"{BROWN}---------------------------------------------------------------")
  print(f"{RED}INDEX NO.              : {GREEN}{1} (latest message) out of {len(jon)} (total messages)")
  print(f"{RED}From                   : {GREEN}{jon[0]['from'][0]['name']} {CYAN}<{jon[0]['from'][0]['address']}>")
  print(f"{RED}To                     : {GREEN}{mail}")
  print(f"{RED}Date and Time          : {GREEN}{jon[0]['received']}{END}") 
  print(f"{RED}id code                : {GREEN}{jon[0]['_id']}")
  if len(jon[0]['attachments']) >= 1:  # Shows Attachment ID if exixts.
          ab =  jon[0]['attachments'][0]
          print(f"{RED}Attachment ID          : {GREEN}{ab}")
  ip = geocoder.ip(jon[0]['ip'])
  print(f"{RED}IP based Location      : {GREEN}{ip.city}")
  print(f"\n{VIOLET}SUBJECT: {YELLOW}{jon[0]['subject']}{END}")
  print(f"{BROWN}---------------------------------------------------------------")
  msg = requests.get(f'https://mailsac.com/api/text/{mail}/{jon[0]["_id"]}', headers=headers)
  print(f"{CYAN}{msg.text}")  
  if len(jon[0]['attachments']) >= 1: # For Downloading the Attachment.
          ab =  jon[0]['attachments'][0]
          att = requests.get(f"https://mailsac.com/api/addresses/{mail}/messages/{jon[0]['_id']}/attachments/{ab}", 
    headers=headers , allow_redirects=True)
          print(f"{BROWN}--------------------------------------------------------------\n\n")
          ask = input(f"{RED}Attachment Detected {BLUE}{att.headers.get('content-type')}.{RED} Do you want to download it? (yes/no) :") 
          ext = att.headers.get('content-type').partition('/')[2] #Extracts Extention of attachmnet
          if ask == "yes" or ask == "YES":
            if (path.exists('Downloads') != True):
              system("mkdir Downloads")
            nam = input(f"\n{YELLOW}Enter the name of file to download: {BLUE}") # custom name for file to download
            download_name = nam+"."+ext  # Final combined Download name
            open(f'{download_name}', 'wb').write(att.content)
            system(f"mv \'{download_name}\' Downloads")
            print(f"{CYAN}Attachment Downloaded to Download Folder")
          else:
            loop()
  print(f"{BROWN}---------------------------------------------------------------")
  loop()

# Listing of all emails.
elif inp == 2:
  if req.ok == True :
    #print(jon)
    print (f"\n{RED}=====================================================")
    rr = len(jon) # counts the number of total mails received.
    print(f"{BLUE}Total NO. of emails received on {RED}{mail}{CYAN}: {YELLOW}{rr}{END}")
    print (f"{RED}=====================================================\n")
    inp2 = int(input(f"{CYAN}Enter the no. of last emails you want to see: {YELLOW}:"))
    print (f"\n{RED}=====================================================\n")
    system("clear")
    if inp2 <= rr:
      for i in range(0,inp2):
        print(f"{BROWN}---------------------------------------------------------------")
        print(f"{RED}INDEX NO.              : {GREEN}{i+1}")
        print(f"{RED}From                   : {GREEN}{jon[i]['from'][0]['name']} {CYAN}<{jon[i]['from'][0]['address']}>")
        print(f"{RED}To                     : {GREEN}{mail}")
        print(f"{RED}Date and Time          : {GREEN}{jon[i]['received']}{END}") 
        print(f"{RED}id code                : {GREEN}{jon[i]['_id']}")   
        if len(jon[i]['attachments']) >= 1:  # Shows Attachment ID if exixts.
          ab =  jon[i]['attachments'][0]
          print(f"{RED}Attachment ID          : {GREEN}{ab}")
        ip = geocoder.ip(jon[i]['ip']) #Finds the location of The IP Address
        print(f"{RED}IP based Location      : {GREEN}{ip.city}")
        print(f"{VIOLET}SUBJECT: {YELLOW}{jon[i]['subject']}{END}")
 
      print (f"\n{RED}=====================================================")
      var3 = int(input(f"{CYAN}Enter the INDEX NO of mail you want to read: {YELLOW}:"))
      if var3 <= rr:
        print (f"{RED}=====================================================\n{END}")
        system("clear")
        print(f"{BROWN}---------------------------------------------------------------")
        msg = requests.get(f'https://mailsac.com/api/text/{mail}/{jon[var3-1]["_id"]}', headers=headers) #Reads the content of mail.
        print(f"{VIOLET}SUBJECT: {YELLOW}{jon[i]['subject']}{END}")
        print(f"{BROWN}--------------------------------------------------------------")
        print(f"{CYAN}{msg.text}")  # Prints the Messsage of Mail
        if len(jon[var3-1]['attachments']) >= 1: # For Downloading the Attachment.
          ab =  jon[var3-1]['attachments'][0]
          att = requests.get(f"https://mailsac.com/api/addresses/{mail}/messages/{jon[var3-1]['_id']}/attachments/{ab}", 
    headers=headers , allow_redirects=True)
          print(f"{BROWN}--------------------------------------------------------------\n\n")
          ask = input(f"{RED}Attachment Detected {BLUE}{att.headers.get('content-type')}.{RED} Do you want to download it? (yes/no) :") 
          ext = att.headers.get('content-type').partition('/')[2] #Extracts Extention of attachmnet
          if ask == "yes" or ask == "YES":
            print(f"{RED}Attachment ID          : {GREEN}{ab}")
            if (path.exists('Downloads') != True):
              system("mkdir Downloads")
            nam = input(f"\n{YELLOW}Enter the name of file to download: {BLUE}") # custom name for file to download
            download_name = nam+"."+ext  # Final combined Download name
            open(f'{download_name}', 'wb').write(att.content)
            system(f"mv \'{download_name}\' Downloads")
            print(f"{CYAN}Attachment Downloaded to Download Folder")
          else:
            loop()
          
        print(f"{BROWN}--------------------------------------------------------------\n\n")
        loop()
      else:  
        print(f"{RED}\n\n\nERROR! Range exceeded the no of present INDEX")
        print(f"{RED}Try Again within correct range of {CYAN}1-{rr} .")
        
        loop()
    else:
      print(f"{RED}\n\n\nERROR! Range exceeded the no of total present emails")
      print(f"{RED}Try Again within correct range of {CYAN}1-{rr} .")
      loop()
  else:
    print("Invalid Email Address")
    print("Please change the address")
    sleep(2)
    system("python3 gen_credentials.py")
    input(f"{VIOLET} PRESS ENTER TO RETURN TO MAIN MENUE")
    loop()

# Delete a Mail
elif inp == 3:
  if req.ok == True :
    #print(jon)
    print (f"\n{RED}=====================================================")
    rr = len(jon) # counts the number of total mails received.
    print(f"{BLUE}Total NO. of emails received on {RED}{mail}{CYAN}: {YELLOW}{rr}{END}")
    print (f"{RED}=====================================================\n")
    inp2 = int(input(f"{CYAN}Enter the no. of last emails you want to see: {YELLOW}:"))
    print (f"\n{RED}=====================================================\n")
    system("clear")
    if inp2 <= rr:
      for i in range(0,inp2):
        print(f"{BROWN}---------------------------------------------------------------")
        print(f"{RED}INDEX NO.              : {GREEN}{i+1}")
        print(f"{RED}From                   : {GREEN}{jon[i]['from'][0]['name']} {CYAN}<{jon[i]['from'][0]['address']}>")
        print(f"{RED}To                     : {GREEN}{mail}")
        print(f"{RED}Date and Time          : {GREEN}{jon[i]['received']}{END}") 
        print(f"{RED}id code                : {GREEN}{jon[i]['_id']}")
        ip = geocoder.ip(jon[i]['ip']) #Finds the location of The IP Address
        print(f"{RED}IP based Location      : {GREEN}{ip.city}")
        print(f"{VIOLET}SUBJECT: {YELLOW}{jon[i]['subject']}{END}")
 
      print (f"\n{RED}=====================================================")
      var3 = int(input(f"{CYAN}Enter the INDEX NO of mail you want to DELETE: {YELLOW}:"))
      if var3 <= rr:
        print (f"{RED}=====================================================\n{END}")
        system("clear")
        print(f"{BROWN}---------------------------------------------------------------")
        dell = requests.delete(f'https://mailsac.com/api/addresses/{mail}/messages/{jon[var3-1]["_id"]}', headers=headers) #Deleted the mail.
        if dell.status_code == 200 :
          print(f"{GREEN}Mail Deleted sucessfully")
          loop()
        else:
          print(f"{RED}Message Deletion failed, try again")
          loop()
        print(f"{VIOLET}SUBJECT: {YELLOW}{jon[i]['subject']}{END}")
        print(f"{BROWN}--------------------------------------------------------------")
        print(f"{CYAN}{msg.text}")
        print(f"{BROWN}--------------------------------------------------------------\n\n")
        loop()
      else:  
        print(f"{RED}\n\n\nERROR! Range exceeded the no of present INDEX")
        print(f"{RED}Try Again within correct range of {CYAN}1-{rr} .")
        
        loop()
    else:
      print(f"{RED}\n\n\nERROR! Range exceeded the no of total present emails")
      print(f"{RED}Try Again within correct range of {CYAN}1-{rr} .")
      loop()
  else:
    print("Invalid Email Address")
    print("Please change the address")
    sleep(2)
    system("python3 gen_credentials.py")
    input(f"{VIOLET} PRESS ENTER TO RETURN TO MAIN MENUE")
    loop()
    
# Check if Mail is valid or not.
elif inp == 4:
  if req.ok == True:
    print(f"\n\n{GREEN}Your email address: {mail}")
    print(f"{GREEN}Sucess! everything seems to be working fine\n")
    loop()
  else:
    print(f"\n\n{GREEN}Your email address: {mail}")
    print(f"{RED}ERROR! please change the email address or API{END}")
    loop()
# Exit    
elif inp == 69:
  print(f"\n\n{CYAN}   EXITING :-)")
  sleep(1)
  exit() 
# IF wrong choice choosed  
else:
  print(f"\n\n{RED}ERROR! Wrong input entered, please try again{END}\n\n")
  loop()