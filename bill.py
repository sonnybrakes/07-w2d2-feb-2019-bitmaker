# B is for Bacon Bill

def print_header():
    print()
    print("B is for Bacon") # built-in print() function
    print()
    print("--------------")

def print_item(item):
    print("$2.00 {}".format(item))

def print_footer():
    print_header()
    print("--------------")
    print()
    print("Please Come Again!")
    print()

def print_bill(item): # defining a function named print_bill()
    print_header()
    print_item(item)
    print_footer()

print_bill('bacon')
