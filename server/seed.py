# server/seed.py

from server.app import create_app
from server.extensions import db
from server.models import User, Guest, Episode, Appearance
from datetime import date

app = create_app()

with app.app_context():
    print(" Seeding database...")


    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

    
    user = User(username="admin")
    user.set_password("password")
    db.session.add(user)

    
    guest1 = Guest(name="Trevor Noah", occupation="Comedian")
    guest2 = Guest(name="Zendaya", occupation="Actress")
    guest3 = Guest(name="Bill Gates", occupation="Philanthropist")

    db.session.add_all([guest1, guest2, guest3])


    episode1 = Episode(date=date(2025, 6, 1), number=1)
    episode2 = Episode(date=date(2025, 6, 2), number=2)

    db.session.add_all([episode1, episode2])
    db.session.flush()  


    a1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    a2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode1.id)
    a3 = Appearance(rating=3, guest_id=guest3.id, episode_id=episode2.id)

    db.session.add_all([a1, a2, a3])

    db.session.commit()
    print(" Done seeding!")
