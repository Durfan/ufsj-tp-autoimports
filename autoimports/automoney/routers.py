class DBRouter(object):

	def db_for_read(self, model, **hints):

		if model._meta.app_label == 'automoney':
			return 'dbautoapps'
		return None
 
	def db_for_write(self, model, **hints):

		if model._meta.app_label == 'automoney':
			return 'dbautoapps'
		return None
 
	def allow_syncdb(self, db, model):

		if db == 'dbautoapps':
			return model._meta.app_label == 'automoney'
		elif model._meta.app_label == 'automoney':
			return False
		return None