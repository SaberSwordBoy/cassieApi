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
    for i in string:
        if i in FILTER_CHARS:
            string = string.replace(i, "")
    return string

def get_ai_response(input_message):
    return chatbot.assistant.request(input_message)

class GetResponse(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('input', required=True)  # add args
        args = parser.parse_args()  # parse arguments to dictionary
        response = get_ai_response(args['input'])

        print(f"[#] Responded to query '{args['input']}' with {response}")
        return {'data': {
            "response": response
        }}, 200  # return data with 200 OK

    def get(self):
        return 'Submit a post request', 200 # return data with 200 OK

api.add_resource(GetResponse, '/getresponse')
if __name__ == '__main__':
    app.run()