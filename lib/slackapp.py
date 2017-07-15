from flask import Flask, request, jsonify, abort
application = Flask(__name__)

@application.route("/rt", methods=['POST'])
def rt():
    abort(403)
    text = request.form.get('text', None)
    return jsonify({
	"response_type": "in_channel",
        "text": "https://rt.tss.its.nyu.edu/Ticket/Display.html?id=" + text
    })

