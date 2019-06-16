

class Formatter(object):
	
	""" Family Formatter """
	def family_formatter(self, family_obj):
		return {
			'id': family_obj.id,
			'surname': family_obj.surname
		}