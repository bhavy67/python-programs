def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Cardamom Chai"
    yield "Green Tea"

def full_menu():
    yield "Lemon Tea"
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(f"Serving {chai}")

def chai_stall():
    try:
        while True:
            order = yield
            print(f"Preparing {order}")
    except:
        print("Cleaning up the stall...")

stall = chai_stall()
next(stall)
stall.send("Masala Chai")
stall.close()