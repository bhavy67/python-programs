class ChaiUtils:
    @staticmethod
    def clean_ingredients(ingredients):
        return [ingredient.strip().lower() for ingredient in ingredients]
    
raw_ingredients = ["  Tea Leaves  ", " Milk ", " Sugar ", " Spices "]

cleaned = ChaiUtils.clean_ingredients(raw_ingredients)
print(cleaned)