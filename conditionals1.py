user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in == True:
	print('Admin Page')
else:
	print('Invalid credentials')

if user == 'Admin' or logged_in == True:
	print('Admin Page')
else:
	print('Invalid credentials')


if not logged_in:
	print('Not logged in')