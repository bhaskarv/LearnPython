#tuples are like immutable lists they can't be modified

list_1=['History','Maths','Physics','CompSci']
list_2=list_1

print(list_1)
print(list_2)

list_1[0]='Arts'

#As can be seen below, adding to list_1 changed list_2 as well
print(list_1)
print(list_2)

#now take a look at a tuple
touple_1=('History','Maths','Phisics','CompSci')
touple_2 = touple_1

print(touple_1)
print(touple_2)

#trying to modify hte touple gives error
touple_1[0]='Arts'

#Guideline : If you want to access and modfiy use list, if you just want to iterate and access use touple