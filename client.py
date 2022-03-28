import requests
from rich import print
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')

DEBUG = config.getboolean("Client", "debug") # Print additional data if DEBUG = True

# Urls
BASE_URL = f"http://{config.get('Client', 'server_ip')}/"
PORT = config.get('Client', 'server_port')
GETRESP_URL = 'getresponse'

if DEBUG:
    print(BASE_URL, PORT, GETRESP_URL)

exit_vars = ["exit", "quit"] # If the user types anything in this list, the program will quit. 

# Banner
print("-"*50)
print("[orchid]\t   ✨ Welcome to Cassandra! ✨[/orchid]")
print("-"*50)
print("[grey70]Type a message and hit enter. Your message gets sent to the Cassie server and processed using AI.\n"\
      "The first message might take a few seconds longer than the rest.\n\n[/grey70]")

print("Enter text to say to Cassandra")

# Functions
def assistant_help():
    print("-"*50)
    print("\t\tHELP")
    print("-"*50)

def create_note():
    # do stuff
    print("Create a new note")

# Main Loop
while True:
    print("[purple blink]>>> [/purple blink]", end='')
    input_text = input()
    if input_text in exit_vars:
        print("Exiting!")
        break
    
    resp = requests.post(BASE_URL + GETRESP_URL, data={"input": input_text}).json() # Request the URL and save the JSON
    resp_data = resp['data']

    if DEBUG is True:
        print(resp_data)

    else:
        print("You: " + input_text)
        print("Cassie: " + resp_data['response'])

    if resp_data.get('func'): # check if there is a function along with response
        exec(f"{resp_data['func']}()")  # execute function given to us by server

