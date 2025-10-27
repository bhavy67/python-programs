def serve_chai(order):
    try:
        print(f"Serving {order}")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Chai served successfully!")
    finally:
        print("Thank you for visiting our chai shop.")

serve_chai("Masala Chai")
