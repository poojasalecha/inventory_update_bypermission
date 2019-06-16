""" User Formatter """
def user_formatter(self, user_obj): 
	return {
		'id': user_obj.id,
		'email': user_obj.email,
		'is_vendor': user_obj.is_vendor,
		'name': ''
	}
