seat_type = input("Enter the seat type (Sleeper, AC, Non-AC, General, Luxury): ").lower()

match seat_type:
    case "sleeper":
        price = 150
    case "ac":
        price = 300
    case "non-ac":
        price = 200
    case "general":
        price = 100
    case "luxury":
        price = 500
    case _:
        price = 0
        print("Invalid seat type entered.")

print(f"Price for {seat_type} seat: ${price}")