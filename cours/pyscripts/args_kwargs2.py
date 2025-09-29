def fct(a, b, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))
    return
    
print("Cas 1: fct(1, 2)")
fct(1, 2)
print()

print("Cas 2: fct(1, 2, 3, 4)")
fct(1, 2, 3, 4)
print()

print("Cas 3: fct(1, 2, 3, 4, z=-2)")
fct(1, 2, 3, 4, z=-2)
print()

print("Cas 4: fct(1, 2, 3, 4, x=2, z=34, y=-67)")
fct(1, 2, 3, 4, x=2, z=34, y=-67)

