courses=['Hist','Comp','Math','Social']

#itereate over the list
for item in courses:
	print(item)

#get index while iterating  use enumerate function
for index,course in enumerate(courses):
	print('{} : {}'.format(index, course))

#default index is 0, we can specify explicit value for index to start at
print("Same list with index start of 2")
for index,course in enumerate(courses,start=2):
	print('{} : {}'.format(index, course))

#convert list into a string
courses_str=','.join(courses)
print(courses_str)
