from flask import Blueprint, jsonify
from server.models import Guest

guest_bp = Blueprint('guests', __name__, url_prefix='/guests')

@guest_bp.route('', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([
        {'id': g.id, 'name': g.name, 'occupation': g.occupation}
        for g in guests
    ])
