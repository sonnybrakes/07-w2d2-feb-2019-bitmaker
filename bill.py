# B is for Bacon Bill

def print_bill(item='bacon'): # defining a function named print_bill()
    print()
    print("B is for {}".format(item)) # built-in print() function
    print("--------------")
    print("$2.00 {}".format(item))
    print("--------------")
    print()
    print("Please Come Again!")
    print()
    print()

print_bill()
print_bill('veggie bacon')
