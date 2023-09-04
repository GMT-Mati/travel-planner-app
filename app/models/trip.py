from app import db

class Trip(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)

	# Add more filelds and methodes as needed
