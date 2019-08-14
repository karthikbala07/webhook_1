# import flask dependencies
from flask import Flask, request, make_response, jsonify

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!'

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    if (req.get('queryResult').get('action') == 'school'):
         return {'fulfillmentText': 'The name of the school is ABPS'}
         print("The name of the school is ABPS")
    elif (req.get('queryResult').get('action') == 'college'):
         return {'fulfillmentText': 'The name of the college is SSN'}
         print("The name of the college is SSN")

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
    app.run()
