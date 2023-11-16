#######
# Interview question that asks to simulate a warehouse that can only
# maintain N products at once. Once N products are created, throw an exception
# that too many products exist.
#
# Create routines to create new, delete, and print products
#######
class TooManyProducts(Exception):
    """Exception raised when too many products."""
    pass

class Product:
    name = None
    counter = 0

    def __init__(self, name):
        self.name = name
        Product.counter += 1

    def __del__(self):
        self.name = None
        Product.counter -= 1


####### Main starts here ########
products = list()
max_products = 3

def newProd(prod_name):
    if Product.counter == max_products:
        raise(TooManyProducts)
    products.append(Product(prod_name))
    print("Created a new {0}".format(prod_name))

def removeProd(prod_name):
    found = False
    for i in range(0,len(products)):
        if products[i].name == prod_name:
            print("Found {0} in index {1}".format(prod_name, i))
            products.pop(i)
            print("Removed a {0}".format(prod_name))
            found = True
            break
    if not found:
        print("Product with name {0} not found".format(prod_name))
    


newProd("laptop")
print(Product.counter)
newProd("bookcase")
print(Product.counter)
removeProd("bookcase")
print(Product.counter)
removeProd("book")
newProd("book")
newProd("lamp")
try:
    newProd("window")
except TooManyProducts:
    print("Expected error. Too many products")
removeProd("book")
    

                


