from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from server.extensions import db
from server.models import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data.get("username") or not data.get("password"):
        return jsonify(error="Username and password required"), 400

    if User.query.filter_by(username=data["username"]).first():
        return jsonify(error="User already exists"), 409

    user = User(username=data["username"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()

    return jsonify(message="User created"), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get("username")).first()

    if user and user.check_password(data.get("password")):
        token = create_access_token(identity=user.id)
        return jsonify(token=token), 200

    return jsonify(error="Invalid credentials"), 401
