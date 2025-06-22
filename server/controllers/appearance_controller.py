from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models import Appearance
from server.extensions import db

appearance_bp = Blueprint('appearances', __name__, url_prefix='/appearances')

@appearance_bp.route('', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    
    try:
        rating = data['rating']
        guest_id = data['guest_id']
        episode_id = data['episode_id']
    except KeyError as e:
        return jsonify(error=f"Missing field: {e.args[0]}"), 400

    appearance = Appearance(
        rating=rating,
        guest_id=guest_id,
        episode_id=episode_id
    )

    if not appearance.validate():
        return jsonify(error="Rating must be between 1 and 5"), 400

    db.session.add(appearance)
    db.session.commit()

    return jsonify(appearance.to_dict()), 201
