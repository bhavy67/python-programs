chai_types = ["Masala", "Ginger", "Cardamom"]


strong_chai = list(filter(lambda x: x=='Ginger', chai_types))
not_strong_chai = list(filter(lambda x: x!='Ginger', chai_types))
print(strong_chai)
print(not_strong_chai)