#A Generator is also a function which remembers where it stopped previously
# It is called through next()
#Example 1:
def give_numbers():
    yield 1
    yield 2
    yield 3

g = give_numbers()
print(next(g))
print(next(g))
print(next(g))


#Example 2: Infinite generator (Counter)
def counter():
    n = 1
    while True:
        yield n
        n += 1

c = counter()
print(next(c))
print(next(c))
print(next(c))
print(next(c))