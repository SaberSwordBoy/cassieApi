import flask
from flask_restful import Api, Resource, reqparse
import json
import random
import chatbot

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
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('input', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary
        response = get_ai_response(args['input'])

        if response == "":
            return "No input", 400

        print(f"[#] Responded to query '{args['input']}' with {response}") # Print out query/response
        
        return {'data': {
            "response": response
        }}, 200  # return data with 200 OK

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
    app.run(host="", port=80) # host needs to be server IP or will not work. Port 80 works best. 
