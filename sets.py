#sets dont allow duplicates
#sets are optimized for lookups

courses={'Maths','Physics','History','CompSci'}
print(courses)

#add a duplicate item - ignored
courses.add('Maths')
print(courses)

courses.add('PoliticalScience')
print(courses)

#Operations on sets
courses1 = {'Maths','History','Arts','Physics'}
print(courses.intersection(courses1))
print(courses.difference(courses1))
print(courses.union(courses1))