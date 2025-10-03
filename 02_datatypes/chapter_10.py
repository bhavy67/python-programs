users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 200, "coupon": "P30"},
    {"id": 3, "total": 300, "coupon": "P40"},
]

discounts = {
    "P20": (0.2, 0),
    "P30": (0.3, 10),
    "P40": (0.4, 20),
}

for user in users:
    percentage, fixed = discounts.get(user["coupon"], (0, 0))
    discount_amount = user["total"] * percentage + fixed