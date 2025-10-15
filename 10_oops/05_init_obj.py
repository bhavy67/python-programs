class Chai_order:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"This is a {self.size} ml cup of {self.type} chai."
    

first_order = Chai_order("Masala", 200)
print(first_order.summary())

second_order = Chai_order("Ginger", 150)
print(second_order.summary())