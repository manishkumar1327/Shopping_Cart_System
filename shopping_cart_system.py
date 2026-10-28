# Shopping Cart System 

products = {"pen": 10, "notebook": 50, "bag": 500}
cart = {}


def view_products():
    print("\nProducts:")
    for name in products:
        print(name.title(), "- Rs.", products[name])


def add_item():
    name = input("Product name: ").lower()
    if name not in products:
        print("Invalid product!")
        return
    if not (qty := input("Quantity: ")).isdigit() or int(qty) < 1:
        print("Invalid quantity! Enter 1 or more.")
        return
    cart[name] = cart.get(name, 0) + int(qty)
    print(name.title(), "x" + qty, "added.")


def remove_item():
    name = input("Product to remove: ").lower()
    if name in cart:
        del cart[name]
        print(name.title(), "removed.")
        view_cart()
    else:
        print("Item not in cart.")


def view_cart():
    print("\nYour Cart:")
    subtotal = 0
    for name in cart:
        total = products[name] * cart[name]
        subtotal += total
        print(name.title(), "x", cart[name], "= Rs.", total)
    print("Subtotal: Rs.", subtotal)
    return subtotal


def checkout():
    subtotal = view_cart()
    discount = subtotal * 0.10 if subtotal > 500 else 0
    gst = (subtotal - discount) * 0.18
    total = subtotal - discount + gst
    print("\n----- BILL -----")
    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("GST     :", gst)
    print("TOTAL   :", total)


while True:
    print("\n1.View Products  2.Add  3.Remove  4.View Cart  5.Checkout  6.Exit")
    choice = input("Choose: ")
    if choice == "1":
        view_products()
    elif choice == "2":
        add_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        view_cart()
    elif choice == "5":
        checkout()
        break
    elif choice == "6":
        break
    else:
        print("Invalid choice!")
