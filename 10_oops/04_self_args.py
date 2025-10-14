class Chai_cup:
    size = 150 #ml

    def describe(self):
        return f"This chai cup holds {self.size} ml of chai."
    
small_cup = Chai_cup()
print(small_cup.describe())
print(Chai_cup.describe(small_cup))

