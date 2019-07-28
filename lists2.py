courses=['Hist','Comp','Math','Social']
print(courses)
courses.reverse()
print(courses)
courses.sort()
print(courses)

nums=[4,10,3,1,6,9,14]
print(nums)
nums.sort()
print(nums)

#Reverse sort
courses.sort(reverse=True)
print(courses)

nums.sort(reverse=True)
print(nums)

sourted_courses=sorted(courses)  #Original list is kept intact
print(sourted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

#index
print('Index Of Hist',courses.index("Hist"))
print('Is Finance in list',' Finance' in courses)
print('Is Comp in list','Comp' in courses)