def chai_customer():
    print("Welcome to the Chai Stall")
    order = yield
    while True:
        print(f"Preparing {order}")
        order = yield


stall = chai_customer()
next(stall)
stall.send("Masala Chai")
stall.send("Ginger Chai")