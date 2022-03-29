import requests
from rich import print
import configparser
import os 

config = configparser.ConfigParser()
config.read('config/config.ini')

DEBUG = config.getboolean("Client", "debug") # Print additional data if DEBUG = True

# Urls
BASE_URL = f"http://{config.get('Client', 'server_ip')}/"
PORT = config.get('Client', 'server_port')
GETRESP_URL = 'getresponse'

if DEBUG:
    print(BASE_URL, PORT, GETRESP_URL)

# Banner
print("-"*50)
print("[orchid]\t   ✨ Welcome to Cassandra! ✨[/orchid]")
print("-"*50)
print("[grey70]Type a message and hit enter. Your message gets sent to the Cassie server and processed using AI.\n"\
      "The first message might take a few seconds longer than the rest.\nType 'help' for Cassie help, and '!help' for client help\n\n[/grey70]")

print("Enter text to say to Cassandra")

# Client functions
def client_help():
    os.system('cls')
    os.system('clear')
    print("-"*50)
    print("\t\tCLIENT HELP")
    print("-"*50)

# Assistant Functions
def assistant_help():
    print("-"*50)
    print("\t\tHELP")
    print("-"*50)

def create_note():
    print("-"*50)
    print("Create a note")
    print("-"*50)

def send_email():
    print("-"*50)
    print("Send Email")
    print("-"*50)

# Main Loop
while True:
    print("[purple blink]>>> [/purple blink]", end='')
    input_text = input()
    
    if input_text == '!exit': # exit
        print("Exiting!")
        break
    elif input_text == '!clear' or input_text == '!cls': # clear the screen
        os.system('cls')
        os.system('clear')
        continue
    elif input_text == '!help': # call the help function
        client_help()
        continue
    
    try: resp = requests.post(BASE_URL + GETRESP_URL, data={"input": input_text}).json() # Request the URL and save the JSON
    except ConnectionError: resp = {'data': {'response': '[red]UNABLE TO CONNECT TO SERVER[/red]'}}
    except requests.exceptions.ConnectionError: resp = {'data': {'response': '[red]UNABLE TO CONNECT TO SERVER[/red]'}} 
        
    resp_data = resp['data']
    
    if resp_data.get('func'): # check if there is a function along with response
        exec(f"{resp_data['func']}()")  # execute function given to us by server
        
    elif DEBUG:
        print(resp_data)

    else:
        print("You: " + input_text)
        print("Cassie: " + resp_data['response'])

