from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models import Episode
from server.extensions import db

episode_bp = Blueprint('episodes', __name__, url_prefix='/episodes')

@episode_bp.route('', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([
        {'id': e.id, 'date': e.date.isoformat(), 'number': e.number}
        for e in episodes
    ])
@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify(episode.to_dict()), 200


@episode_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify(message="Episode deleted"), 200
