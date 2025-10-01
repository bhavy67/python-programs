order_amount = input("Enter the order amount: ")
try:
    order_amount = float(order_amount)
    if order_amount < 0:
        print("Order amount cannot be negative.")
    elif order_amount < 10:
        discount = 0.05
    elif order_amount < 50:
        discount = 0.10
    else:
        discount = 0.15
    final_amount = order_amount * (1 - discount)
    print(f"Final amount after discount: ${final_amount:.2f}")
except ValueError:
    print("Invalid input. Please enter a numeric value for the order amount.")
