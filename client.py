import requests

DEBUG = True # Print out all data instead of just response. 

# Urls
BASE_URL = 'http://45.33.77.180/'
PORT = 80 # Not needed currently
GETRESP_URL = 'getresponse'

exit_vars = ["exit", "quit"] # If the user types anything in this list, the program will quit. 

# Banner
print("-"*50)
print("\t   ✨ Welcome to Cassandra! ✨")
print("-"*50)
print("Type a message and hit enter. Your message gets sent to the Cassie servers and processed using AI.\n"\
      "The first message might take a few seconds longer than the rest.\n\n")

print("Enter text to say to Cassandra")

# Functions to run

def assistant_help():
    print("-"*50)
    print("\t\tHELP")
    print("-"*50)


# Main Loop
while True:
    input_text = input(">>> ")
    
    if input_text in exit_vars:
        print("Exiting!")
        break
    
    resp = requests.post(BASE_URL + GETRESP_URL, data={"input": input_text}).json()
    resp_data = resp['data']

    if resp_data.get('func'):
        exec(f"{resp_data['func']}()")

    if DEBUG:
        print(resp_data)
    else:
        print("You: " + input_text)
        print("Cassie: " + resp_data['response'])
