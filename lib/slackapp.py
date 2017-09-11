import ConfigParser
import re
from flask import Flask, request, jsonify, abort

application = Flask(__name__)

@application.route("/rt", methods=['POST'])
def rt():
    validate_token(request)
    text = request.form.get('text', None)
    if not re.match("^[0-9]{6}$", text):
    	abort(500)
    return jsonify({
	"response_type": "in_channel",
        "text": "<Ticketing Link>" + text
    })

def validate_token(request):
	config = ConfigParser.ConfigParser()
	config.read("../etc/token.ini")
	if request.form.get('token', None) != config.get("Slack", "token"):
		abort(403)
