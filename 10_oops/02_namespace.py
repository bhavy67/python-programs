class Chai:
    origin = "India"

# print(Chai.origin)

Chai.is_hot = True
# print(Chai.is_hot)

#Creating objects
masala_tea = Chai()
print(masala_tea.origin)
print(masala_tea.is_hot)

masala_tea.is_hot = False
print(masala_tea.is_hot)

masala_tea.flavor = "Spicy"
print(masala_tea.flavor)