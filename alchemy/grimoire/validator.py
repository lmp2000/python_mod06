def validate_ingredients(ingredients: str) -> str:
    valid_elements = ["fire", "water", "earth", "air"]
    ingr = ingredients.split()
    for ingredient in ingr:
        if ingredient not in valid_elements:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"