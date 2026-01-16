#Question: Write a single Python program that programmatically demonstrates how
# Python passes arguments to functions using:
# Immutable objects
# Mutable objects
# Mutation vs rebinding
# In-place vs non–in-place operations
#
# The output of the program should prove that Python uses pass-by-assignment, using
# only code and printed evidence.
# use this standard function
# def inspect(label, obj):
#     print(f"{label:<30} | value={obj} | id={id(obj)} | type={type(obj).__name__}")


def inspect(label, obj):
    print(f"{label:<30} | value={obj} | id={id(obj)} | type={type(obj).__name__}")


print("\n" + "="*70)
print("IMMUTABLE OBJECT (int) — REBINDING ONLY")
print("="*70)

def immutable_demo(x):
    inspect("inside before x", x)
    x += 1                     # non–in-place (rebinding)
    inspect("inside after x", x)

a = 10
inspect("outside before a", a)
immutable_demo(a)
inspect("outside after a", a)


print("\n" + "="*70)
print("MUTABLE OBJECT (list) — MUTATION")
print("="*70)

def mutable_mutation_demo(lst):
    inspect("inside before lst", lst)
    lst.append(99)             # in-place mutation
    inspect("inside after lst", lst)

b = [1, 2, 3]
inspect("outside before b", b)
mutable_mutation_demo(b)
inspect("outside after b", b)


print("\n" + "="*70)
print("MUTABLE OBJECT (list) — REBINDING")
print("="*70)

def mutable_rebinding_demo(lst):
    inspect("inside before lst", lst)
    lst = lst + [99]           # non–in-place (rebinding)
    inspect("inside after lst", lst)

c = [1, 2, 3]
inspect("outside before c", c)
mutable_rebinding_demo(c)
inspect("outside after c", c)


print("\n" + "="*70)
print("IN-PLACE vs NON–IN-PLACE OPERATIONS")
print("="*70)

d = [10, 20]
inspect("before += ", d)
d += [30]                      # in-place for list
inspect("after += ", d)

e = [10, 20]
inspect("before + ", e)
e = e + [30]                   # non–in-place
inspect("after + ", e)


print("\n" + "="*70)
print("PASS-BY-ASSIGNMENT PROOF")
print("="*70)
print(
    "• Function parameters receive object REFERENCES\n"
    "• Mutation affects caller when object is shared\n"
    "• Rebinding never affects caller\n"
    "• No variables are passed — only object references"
)
