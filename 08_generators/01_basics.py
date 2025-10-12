def serve_chai():
    yield "Masala Chai"
    yield "Ginger Chai"
    yield "Cardamom Chai"

stall = serve_chai()

# for chai in stall:
#     print(f"Serving {chai}")

def get_chai_list():
    return ["Masala Chai", "Ginger Chai", "Cardamom Chai"]

#Generator
def get_chai_generator():
    yield "Masala Chai"
    yield "Ginger Chai"
    yield "Cardamom Chai"

chai = get_chai_generator()
print(next(chai))
print(next(chai))
print(next(chai))