# B is for Bacon Bill
def print_bill(*items): # defining a function named print_bill()
    print(items)
    # print_header()
    # print_item(item)
    # print_footer()

def print_header():
    print()
    print("B is for Bacon") # built-in print() function
    print()
    print("--------------")

def print_item(item):
    print("$2.00 {}".format(item))

def print_footer():
    print("--------------")
    print()
    print("Please Come Again!")
    print()

print_bill('bacon', 'bacon', 'veggie bacon')
