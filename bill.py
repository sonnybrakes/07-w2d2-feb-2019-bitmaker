# B is for Bacon Bill

def print_bill(price, item='bacon'): # defining a function named print_bill()
    print()
    print("B is for {}".format(item)) # built-in print() function
    print("--------------")
    print("${} {}".format(price, item))
    print("--------------")
    print()
    print("Please Come Again!")
    print()
    print()

print_bill('4.00')
print_bill('5.00', 'veggie bacon')
