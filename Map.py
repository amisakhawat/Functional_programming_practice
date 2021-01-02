# map applies a function to every item in a sequence, returning the resultant sequence

# in 90% case lambda and map function can be written in list comprehension.

numbers = [2,4,5,3,5,6,8]

print(list(map(lambda x: x * 2,  numbers)))

# Squaring a list of numbers
print(list( map(lambda x: x**2, numbers)))

# using list comprehension

square = [n*2 for n in numbers]
print(square)


double = [n*n for n in numbers]
print(double)
