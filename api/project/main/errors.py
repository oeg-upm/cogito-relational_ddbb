from flask import json, make_response, jsonify
from . import main

@main.app_errorhandler(400)
def error_handler_400():
    return make_response(jsonify({"error": "Bad request"}), 400)

"""@main.app_errorhandler(404)
def error_handler_404():
    return make_response(jsonify({"error": "Not found"}), 404)"""


@main.app_errorhandler(500)
def error_handler_500():
    return make_response(jsonify({"error": "Server error"}), 500)