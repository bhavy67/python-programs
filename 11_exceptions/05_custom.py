def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "lemon"]:
        raise ValueError(f"Flavor '{flavor}' is not available.")
    print(f"Brewing {flavor} chai!")

brew_chai("cardamom")