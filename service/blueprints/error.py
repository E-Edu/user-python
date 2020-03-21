from flask import Blueprint, render_template, abort,request, jsonify


error = Blueprint('error-handler', __name__)


@error.app_errorhandler(400)
def handle_400_error(e):
    return jsonify({'error': 'Bad request'}), 400


@error.app_errorhandler(403)
def handle_403_error(e):
    return jsonify({'error': 'Forbidden'}), 403


@error.app_errorhandler(404)
def handle_404_error(e):
    return jsonify({'error': 'Page not found'}), 404


@error.app_errorhandler(405)
def handle_405_error(e):
    return jsonify({'error': 'Method not allowed'}), 405


@error.app_errorhandler(500)
def handle_500_error(e):
    return jsonify({'error': 'Internal server error'}), 500

