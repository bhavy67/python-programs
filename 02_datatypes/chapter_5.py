device_status = "active"
temperature = 38

if device_status == "active":
    print("Device is active")
    if temperature > 37:
        print("Warning: High temperature!")
    else:
        print("Temperature is normal.")
else:
    print("Device is inactive")