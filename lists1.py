courses=['History','Maths','Physics','CompSci']

print(courses)

print(courses[0])  #Access first item with index
print(courses[3])  #Access last item with index

print(courses[-1]) #Another way of accessing last item

#slicing
print(courses[0:2]) #Print values upto second index  ie.e 0 & 1

print(courses[:2]) # start index defaults to 0

print(courses[2:]) # end index is infered as well

#add items - at the end
courses.append('Arts')
print(courses)

#insert items at specified location
courses.insert(0,'Stats')
print(courses)


#add one list to other
courses_2=['Literature','PoliticalSci']
#courses.insert(0, courses_2)
print(courses)

print(courses[0])

#Above has inserted one list as it in another list what we wanted was to insert list contents - we need to use extend for that
courses.extend(courses_2)
print(courses)

#reomve elements based on name
courses.remove("Arts")
print(courses)
print(courses.pop())
print(courses)

#reverse list
sorted=sorted(courses)
print(sorted)
print(courses.reverse())




















