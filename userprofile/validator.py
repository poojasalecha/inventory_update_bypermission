""" Validate Login """
def validate_login(data):
    if not data['email'] or data['email'] == '':
        return False
    if not data['password'] or data['password'] == '':
        return False
    return True
""" Valdiate signup """
def validate_signup(data): 
	if not data['password'] or data['password'] == '':
	    return False
	if not data['email'] or data['email'] == '':
	    return False
	return True