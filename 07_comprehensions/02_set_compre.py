favourite_chais =[
    "Masala Chai",
    "Ginger Chai",
    "Cardamom Chai",
    "Lemon Chai",
    "Green Tea",
    "Black Tea",
    "Masala Chai",
]

unique_chais = {chai for chai in favourite_chais}
print(unique_chais)

recipes = {
    "Masala Chai": ["Tea Leaves", "Water", "Milk", "Spices", "Sugar"],
    "Ginger Chai": ["Tea Leaves", "Water", "Milk", "Ginger", "Sugar"]
}

unique_spices = {spice for recipe in recipes.values() for spice in recipe}
print(unique_spices)

# for recipe in recipes.values():
#     for spice in recipe:
#         unique_spices.add(spice)