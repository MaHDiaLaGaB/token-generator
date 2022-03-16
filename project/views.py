from flask import Blueprint, render_template, jsonify
from .main import PassGenerator


view = Blueprint('view', __name__)


@view.route('/')
def home():
    return render_template("index.html")


@view.route('/get_pass')
def get_pass():
    pass_generator = PassGenerator()
    password = pass_generator.password_generator()
    return jsonify(password)


@view.route('/token')
def token():
    return render_template("token.html")


@view.route('/get_token')
def get_token():
    token_generator = PassGenerator()
    token = token_generator.token_generator()
    return jsonify(token)
