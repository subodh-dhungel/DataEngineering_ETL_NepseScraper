x = 10  # Global namespace

def outer():
    y = 20  # Enclosing namespace

    def inner():
        z = 30  # Local namespace
        print(x, y, z)  # Accessing global, enclosing, and local variables

    inner()

outer()

print(globals())
print(locals())