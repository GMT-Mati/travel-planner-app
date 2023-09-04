class Config(object):
	SECRET_KEY = 'your-secret-key'
	# Add other configuration variables here

class DevelopmentConfig(Config):
	DEBUG = True

class ProductionConfig(Config):
	DEBUG = False
	# Add production configurations here


config = {
	'development' : DevelopmentConfig,
	'production' : ProductionConfig,
	'defoult' : DevelopmentConfig
}
