def call_counter():
    count = 1
    while True:
        yield count
        count += 1


def count_calls(func):
    counter = call_counter()

    def wrapper(*args, **kwargs):
        call_num = next(counter)        # get next call number
        print(f"Call number: {call_num}")
        return func(*args, **kwargs)
    return wrapper


@count_calls
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
say_hello("Bob")
say_hello("Charlie")
