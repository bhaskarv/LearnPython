#Dictionary is used to store name value pairs
student = {'name':'John','age':'25','courses':['Maths','CompSci']}

print(student)
print(student['name'])
print(student['courses'])

#print(student['phone']) #throws error - KeyError

#use get to avoid error
print(student.get('phone'))  #This returns None


student['phone'] = '555-2222'

student['name'] = 'Jane' #Overwrites name

print(student)

#update multiple values
student.update({'name':'John','phone':'3333-1111'})
print(student)

#delete an entry
del student['age']
print(student)

#another way to delete
courses=student.pop('courses')
print(courses)
print(student)


#various functions
print(len(student)) #prints count of keys
print(student.keys())
print(student.values())
print(student.items())

#iterate
for var in student:   #bydefault dict is iterated by key
	print(var)


#iterate by key & value
for var, var1 in student.items():
	print(var, var1)






