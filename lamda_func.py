# The “lambda” syntax allows to create function definitions in a declarative way.


print((lambda x:  x*2) (2))

# Can be also written like this way
dj = (lambda x:  x*2)

print(dj(2))

# Another function
print((lambda x, y: x+y)(4, 8))


# Alternate way
addition = (lambda x, y: x * y)

print(addition(7, 9))

# Sorting authors name by length and letter

authors = ["Sak", "Khurshed", "Rahim", "Karim"]

print(sorted(authors, key=len))

print(sorted(authors))

print(sorted(authors, key=lambda name: name.split()[-1]))

# Returning max value
# Finding maximum value in using lambda or map function is unnecessary as we have builtin max function.

print((lambda x,y: x if x > y else y)(3,5))

# Alternate way
mx = (lambda x,y: x if x > y else y)

print(mx(8,19))

# Returning max value using built in max function.
numbers = [3,4,2,56,5]

print(max(numbers))

# using list comprehension

number = [2,3,7,9,10]

result = [x for x in number if x > 6]
print(f"your result is {result}")




























