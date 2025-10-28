def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        total_cost = price * quantity
        print(f"Total cost: {total_cost}")
    except KeyError as e:
        print(f"Key Error: {e}")
    except TypeError as e:
        print(f"Type Error: {e}")

process_order("masala", 2)
process_order("cardamom", "two")
