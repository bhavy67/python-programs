temperature = 40

while temperature < 100:
    print(f"Current temperature: {temperature}")
    if temperature > 70:
        print("It's getting hot!")
        break
    temperature += 10
else:
    print("Temperature reached 100 degrees.")