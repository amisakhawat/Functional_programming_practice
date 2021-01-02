n = [2,3,4,5,6,7]

n1 = list(map(lambda x:x**2,n))
print(list(filter(lambda x: x > 6,n1)))


# using list comprehension.

my_another_list = [x for x in n if x > 6]

print(my_another_list)

# another example of list comprehension.
num = [2, 3, 4, 5, 6, 7, 89]

my_list = [n for n in num if n % 2 == 0]

print(my_list)


