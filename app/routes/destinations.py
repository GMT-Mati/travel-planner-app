from app.routes import bp

@bp.route('/destinations')
def destinations():
	return 'Destinations Page'

@bp.route('add_destination')
def add_destination():
	return 'Add Destination Page'


