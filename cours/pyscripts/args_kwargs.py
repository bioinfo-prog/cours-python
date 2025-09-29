def fct(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))

# prog principal
print("Cas 1: fct()")
fct()
print()

print("Cas 2: fct(1, 2, 3)")
fct(1, 2, 3)
print()

print("Cas 3: fct(z=1, y=2)")
fct(z=1, y=2)
print()

print("Cas 4: fct(1, 2, z=2, gogo=\"toto\")")
fct(1, 2, z=2, gogo="toto")
print()
