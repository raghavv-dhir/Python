def inspect(label, obj):
    print(f"{label:<20} | value={obj} | id={id(obj)} | type={type(obj).__name__}")


def immutable_demo(x):
    inspect("function start", x)
    x = x + 5
    inspect("function end  ", x)


def mutable_demo(lst):
    inspect("function start", lst)
    lst.append(5)
    inspect("function end  ", lst)


def rebind_demo(lst):
    inspect("function start", lst)
    lst = [9, 9, 9]
    inspect("function end  ", lst)


def inplace_vs_new(lst):
    inspect("function start", lst)
    lst.sort()
    inspect("after sort()  ", lst)
    lst = sorted(lst)
    inspect("after sorted()", lst)


a = 10
inspect("caller start", a)
immutable_demo(a)
inspect("caller end  ", a)

print()

b = [1, 2]
inspect("caller start", b)
mutable_demo(b)
inspect("caller end  ", b)

print()

c = [3, 4]
inspect("caller start", c)
rebind_demo(c)
inspect("caller end  ", c)

print()

d = [3, 1, 2]
inspect("caller start", d)
inplace_vs_new(d)
inspect("caller end  ", d)
