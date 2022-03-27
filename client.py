import requests

# Urls
BASE_URL = 'http://45.33.77.180/'
PORT = 80 # Not needed currently
GETRESP_URL = 'getresponse'

exit_vars = ["q", "exit", "quit"] # If the user types anything in this list, the program will quit. 

# Banner
print("-"*50)
print("Welcome to Cassandra!")
print("-"*50)
print("Type a message and hit enter. Your message gets sent to the Cassie servers and processed using AI.\n"\
    "The first message might take a few seconds longer than the rest.\n\n")
# Main Loop

print("Enter text to say to Cassandra")
while True:
    input_text = input(">>> ")
    
    if input_text in exit_vars:
        print("Exiting!")
        break

    print("You: " + input_text)
    print("Cassie: " + requests.post(BASE_URL + GETRESP_URL, data={"input": input_text}).json()['data']['response'])
