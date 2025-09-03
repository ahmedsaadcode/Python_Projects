products = []
i= 0
while True :
    product = input("Enter a product name:")
    if product.lower() == "done" or len(product) == 0:
        break
    quantity = float(input("Enter a quantity: "))
    price = float(input("Enter a price: "))
    total = quantity * price
    products.append((total))
    products.sort()
    print("-"*15)
    print(f"Product name: {product}")
    print(f"Quantity: {quantity}")
    print(f"Price: {price}")
    print("-"*15)
    print(f"Total item cost: {total}") 
    print("-"*30)
    i += 1
print(f"Thank you to visit ahmed 's shop")
j = 1
while True :
    if i == 0 :
        break
    print(f"The price {j} is : {products[i-1]}")
    i -= 1
    j += 1