# B is for Bacon Bill

def print_bill(item): # defining a function named print_bill()
    print()
    print("B is for {}".format(item)) # built-in print() function
    print()
    print("--------------")
    print("2.00 {}".format(item))
    print("--------------")
    print()
    print("Please Come Again!")
    print()

print_bill('veggie bacon')
print_bill('bacon')
