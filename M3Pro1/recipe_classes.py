# Python program that reads recipes from Excel and lets you search, filter, and view them through a simple menu.
# 10/04/2025
# M3Pro
# Haylee Paredes

class Recipe:
    
    def __init__(self, name, ingredients, steps, is_vegetarian):

        self.__name = name
        self.__ingredients = ingredients if isinstance(ingredients, list) else []
        self.__steps = steps
        self.__is_vegetarian = is_vegetarian
    
    # Getters
    def get_name(self):
        
        return self.__name
    
    def get_ingredients(self):

        return self.__ingredients
    
    def get_steps(self):

        return self.__steps
    
    def get_is_vegetarian(self):

        return self.__is_vegetarian
    
    # Setters
    def set_name(self, name):

        self.__name = name
    
    def set_ingredients(self, ingredients):

        self.__ingredients = ingredients if isinstance(ingredients, list) else []
    
    def set_steps(self, steps):

        self.__steps = steps
    
    def set_is_vegetarian(self, is_vegetarian):

        self.__is_vegetarian = is_vegetarian
    
    def display_recipe(self):

        print("\n" + "-"*60)
        print(f"Recipe: {self.__name.upper()}")
        print("-"*60)
        print("\nIngredients:")
        for idx, ingredient in enumerate(self.__ingredients, 1):
            print(f"  {idx}. {ingredient.strip()}")
        print(f"\nSteps: {self.__steps}")
        print(f"Vegetarian: {'Yes' if self.__is_vegetarian else 'No'}")
        print("-"*60)


class DessertRecipe(Recipe):

    def __init__(self, name, ingredients, steps, is_vegetarian, sweetness_level):

        super().__init__(name, ingredients, steps, is_vegetarian)
        self.__sweetness_level = sweetness_level
    
    # Getter
    def get_sweetness_level(self):

        return self.__sweetness_level
    
    # Setter
    def set_sweetness_level(self, sweetness_level):

        if 1 <= sweetness_level <= 10:
            self.__sweetness_level = sweetness_level
            return True
        else:
            print("Error: Sweetness level must be between 1 and 10")
            return False
    
    def display_recipe(self):

        print("\n" + "-"*60)
        print(f"Dessert Recipe: {self.__name.upper()}")
        print("-"*60)
        print("\nIngredients:")
        for idx, ingredient in enumerate(self.__ingredients, 1):
            print(f"  {idx}. {ingredient.strip()}")
        print(f"\nSteps: {self.__steps}")
        print(f"Vegetarian: {'Yes' if self.__is_vegetarian else 'No'}")
        if self.__sweetness_level is not None:
            print(f"Sweetness Level: {self.__sweetness_level}/10")
        else:
            print("Sweetness Level: Not specified")
        print("-"*60)
    
    def adjust_sweetness(self, adjustment):

        if self.__sweetness_level is None:
            return "Cannot adjust sweetness - level not specified for this recipe"
        
        old_level = self.__sweetness_level
        new_level = max(1, min(10, self.__sweetness_level + adjustment))
        self.__sweetness_level = new_level
        
        if new_level == old_level:
            return f"Sweetness level remains at {old_level}/10 (already at limit)"
        return f"Sweetness adjusted from {old_level}/10 to {new_level}/10"
    
    def format_for_display(self):

        veg_status = "Vegetarian" if self.__is_vegetarian else "Non-Vegetarian"
        return f"{self.__name} | Sweetness: {self.__sweetness_level}/10 | {veg_status}"


class MainCourseRecipe(Recipe):
    
    def __init__(self, name, ingredients, steps, is_vegetarian, spice_level):

        super().__init__(name, ingredients, steps, is_vegetarian)
        self.__spice_level = spice_level
    
    # Getter
    def get_spice_level(self):

        return self.__spice_level
    
    # Setter
    def set_spice_level(self, spice_level):

        if 1 <= spice_level <= 5:
            self.__spice_level = spice_level
            return True
        else:
            print("Error: Spice level must be between 1 and 5")
            return False
    
    def display_recipe(self):

        print("\n" + "-"*60)
        print(f"Main Course Recipe: {self.__name.upper()}")
        print("-"*60)
        print("\nIngredients:")
        for idx, ingredient in enumerate(self.__ingredients, 1):
            print(f"  {idx}. {ingredient.strip()}")
        print(f"\nSteps: {self.__steps}")
        print(f"Vegetarian: {'Yes' if self.__is_vegetarian else 'No'}")
        if self.__spice_level is not None:
            print(f"Spice Level: {self.__spice_level}/5")
        else:
            print("Spice Level: Not specified")
        print("-"*60)
    
    def adjust_spice_level(self, adjustment):

        if self.__spice_level is None:
            return "Cannot adjust spice - level not specified for this recipe"
        
        old_level = self.__spice_level
        new_level = max(1, min(5, self.__spice_level + adjustment))
        self.__spice_level = new_level
        
        if new_level == old_level:
            return f"Spice level remains at {old_level}/5 (already at limit)"
        return f"Spice level adjusted from {old_level}/5 to {new_level}/5"
    
    def format_for_display(self):

        veg_status = "Vegetarian" if self.__is_vegetarian else "Non-Vegetarian"
        return f"{self.__name} | Spice: {self.__spice_level}/5 | {veg_status}"