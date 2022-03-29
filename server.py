import flask
from flask_restful import Api, Resource, reqparse
import chatbot
from rich import print
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')

DEBUG = config.getboolean('Server', "Debug")
HOST = config.get('Server', 'ip')
PORT = config.get('Server', 'port')

print("="*50)
print("\t\tStarting up...")
print("="*50)

app = flask.Flask(__name__)
api = Api(app)

FILTER_CHARS = ["!", ",", '"', '"', "?", ".", "@", "#", "$", "%", "^", "&", "*", "(", ")","}", "{", "[", "]"]

def remove_unwanted_chars(string):
    """Remove Filter Chars from the input string"""
    return "".join(i for i in string if not i in FILTER_CHARS)

def get_ai_response(input_message):
    """Request a response to input from the chatbot"""
    return chatbot.assistant.request(input_message)

class GetResponse(Resource):
    """
    Page for getting responses to input
    """
    def post(self):
        data_resp = {'data':{}}
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('input', required=True)  # add input argument
        args = parser.parse_args()  # parse arguments to dictionary
        if args['input'] == "" or args['input'] == " ": return "ERROR: No Input", 400 # return No Input with 400 ERROR if there is no input

        response = get_ai_response(args['input']).lower()

        # Check for special functions/responses
        if response == "help": 
            data_resp['data']['func'] = "assistant_help"
        elif response == "note": 
            data_resp['data']['func'] = "create_note"
        elif response == 'email':
            data_resp['data']['func'] = 'send_email'

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
    app.run(host=HOST, port=PORT) # host needs to be server IP or will not work. Port 80 works best. 