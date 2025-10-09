tea_prices = {
    "Masala Chai": 20,
    "Ginger Chai": 25,
    "Cardamom Chai": 30,
    "Lemon Chai": 15,
    "Green Tea": 10,
}

tea_prices_inr = {tea: price * 82 for (tea, price) in tea_prices.items()}
print(tea_prices_inr)