from sets_categories_data import (ALCOHOLS)

def clean_ingredients(food, ingredientes):
    menu = food,  set(ingredientes)
    return menu

def check_drinks(bebida, ingre):
    ingredientes = set(ingre)
    if ingredientes.intersection(ALCOHOLS):
        return (f"{bebida} Cocktail")
    else: 
        return (f"{bebida} Mocktail")
    
