from server.extensions import db

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))

    guest = db.relationship('Guest', back_populates='appearances')
    episode = db.relationship('Episode', back_populates='appearances')

    def validate(self):
        return 1 <= self.rating <= 5

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "guest_id": self.guest_id,
            "episode_id": self.episode_id
        }
