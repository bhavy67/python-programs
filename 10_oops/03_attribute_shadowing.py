class Chai:
    temperature = "Hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Warm"
cutting.cup = "Large"
print(cutting.temperature)
print(cutting.cup)

del cutting.temperature
print(cutting.temperature)

del cutting.cup
print(cutting.cup)