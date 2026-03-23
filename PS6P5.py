# Input phase (before loop)
response = input("Do you want to enter an order? (Yes/No): ")

# Process
total_discount = 0

while response == "Yes":
    # Input inside loop
    quantity = float(input("Enter quantity: "))
    price = float(input("Enter price: "))

    # Calculate extended price
    extended_price = quantity * price

    # Determine discount
    if extended_price > 10000:
        discount = extended_price * 0.25
    else:
        discount = extended_price * 0.10

    # Calculate total
    total = extended_price - discount

    # Output per order
    print("Extended Price:", extended_price)
    print("Discount:", discount)
    print("Total:", total)

    # Sum discounts
    total_discount = total_discount + discount

    # Ask again (loop control)
    response = input("Do you want to enter another order? (Yes/No): ")

# Final output after loop
print("Total of all discounts:", total_discount)