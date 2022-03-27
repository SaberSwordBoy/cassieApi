import flask
from flask_restful import Api, Resource, reqparse
import json
import random
import chatbot
from rich import print

DEBUG = False

print("Starting up...")

app = flask.Flask(__name__)
api = Api(app)

FILTER_CHARS = ["!", ",", '"', '"', "?", ".", "@", "#", "$", "%", "^", "&", "*", "(", ")",]

def remove_unwanted_chars(string):
    """Remove Filter Chars from the input string"""
    for i in string: 
        if i in FILTER_CHARS: 
            string = string.replace(i, "")
    return string

def get_ai_response(input_message):
    """Request a response to input from the chatbot"""
    return chatbot.assistant.request(input_message)

class GetResponse(Resource):
    """
    Page for getting responses to input
    """
    def post(self):
        data_resp = {'data': {}}
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('input', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary
        if args['input'] == "" or args['input'] == " ": return "ERROR: No Input", 400 # return No Input with 400 ERROR if there is no input

        response = get_ai_response(args['input']).lower()

        if response == "help": # check for special responses
            data_resp['data']['func'] = "assistant_help"
        elif response == "note": 
            data_resp['data']['func'] = "create_note"

        data_resp['data']['response'] = response
        print(f"[green][✅] Responding to query '{args['input']}' with {response}, data: {data_resp}[/green]") # Print out query/response
        return data_resp, 200  # return data with 200 OK

    def get(self):
        return 'How did you GET here? (You should submit a POST request)', 200 # return data with 200 OK

class Index(Resource):
    """
    Default page, nothing really here. Maybe add HTML?
    """
    def get(self):
        return "Welcome to Cassandra! To get started, submit a post request to /getresponse with some input.", 200

# Add the pages
api.add_resource(Index, "/")
api.add_resource(GetResponse, '/getresponse')

# Run the program
if __name__ == '__main__':
    app.run(host="45.33.77.180", port=80) # host needs to be server IP or will not work. Port 80 works best. 
