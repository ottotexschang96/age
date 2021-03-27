driving = input('Have you driven before:')
if driving != 'yes' and driving != 'no':
	print('Please say yes or no!')
	raise SystemExit 

age = input('Your age:')
if driving == 'yes':
	if int(age) >=18:
		print('Pass through!')
	else:
		print('Please tell me why you have driven before?')
elif driving == 'no':
	if int(age) >=18:
		print('Why waiting? You should get a license now!')
	else:
		print('Please be patient for several year.')
