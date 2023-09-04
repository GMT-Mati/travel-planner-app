from app.routes import bp

@bp.route('/trips')
def trips():
	return 'Trips Page'

@bp.route('/create_trip')
def create_trip():
	return 'Create Trip Page'


