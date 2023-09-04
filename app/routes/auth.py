from app.routes import bp

@bp.route('/login')
def login():
	return 'Login Page'

@bp.route('/register')
def register():
	return 'Register Page'


