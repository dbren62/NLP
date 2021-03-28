remainder = lambda num: num % 2

print(remainder(5))

product = lambda x, y: x * y

print(product(2,3))

def testfunc(num):
    return lambda x:x * num

result1 = testfunc(10)
result2 = testfunc(100)

print(result1(9))
print(result2(9))

numbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]

filtered_list = list(filter(lambda num: (num>7), numbers_list))

print(filtered_list)

#map() function returns a map object(which is an iterator) of the result of
#applying the given function to each item of a given iterable

# Return double of n
def addition(n):
    return n+n

# We double all numbers using regular function
numbers = [1,2,3,4]
result = map(addition, numbers)
print(list(result))

# The same using lambda
numbers = [1,2,3,4]
result = map(lambda n: n +n, numbers)
print(list(result))

# The same using omabda with 2 arguments
numbers = [1,2,3,4]
numbers2 = [5,6,7,8]
result = list(map(lambda n, y: n + y, numbers, numbers2))
print(result)

