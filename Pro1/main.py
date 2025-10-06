# Python program that reads recipes from Excel and lets you search, filter, and view them through a simple menu.
# 10/04/2025
# M3Pro
# Haylee Paredes

from recipe_classes import DessertRecipe, MainCourseRecipe

def load_recipes_from_excel(filename):

    recipes = []
    
    try:
        try:
            import pandas as pd
            df = pd.read_excel(filename)
            
            def process_row(row_data):
                index, row = row_data
                try:
                    name = str(row['Name']).strip().title()
                    ingredients = [ing.strip() for ing in str(row['Ingredients']).split(',')]
                    steps = str(row['Steps']).strip()
                    recipe_type = str(row['Type']).strip()
                    is_vegetarian = str(row['Is_Vegetarian']).strip().upper() == 'TRUE'
                    
                    if recipe_type.lower() == 'dessert':
                        try:
                            sweetness = int(row['Sweetness_Level'])
                        except (ValueError, KeyError):
                            sweetness = None
                        return DessertRecipe(name, ingredients, steps, is_vegetarian, sweetness)
                    elif recipe_type.lower() == 'main course':
                        try:
                            spice = int(row['Spice_Level'])
                        except (ValueError, KeyError):
                            spice = None
                        return MainCourseRecipe(name, ingredients, steps, is_vegetarian, spice)
                    else:
                        print(f"Warning: Unknown recipe type '{recipe_type}' for {name}. Skipping.")
                        return None
                    
                except KeyError as e:
                    print(f"Warning: Missing required column in row {index + 2}: {e}")
                    return None
                except Exception as e:
                    print(f"Warning: Error processing row {index + 2}: {e}")
                    return None
            
            all_recipes = [process_row((idx, row)) for idx, row in df.iterrows()]
            recipes = [r for r in all_recipes if r is not None]
            
        except ImportError:

            print("Pandas not available. Using manual file reading...")
            with open(filename.replace('.xlsx', '.csv'), 'r') as file:
                lines = file.readlines()
                headers = [h.strip() for h in lines[0].split(',')]
                
                def process_line(line_data):
                    i, line = line_data
                    try:
                        values = [v.strip() for v in line.split(',')]
                        data = dict(zip(headers, values))
                        
                        name = data['Name'].strip().title()
                        ingredients = [ing.strip() for ing in data['Ingredients'].split(';')]
                        steps = data['Steps'].strip()
                        recipe_type = data['Type'].strip()
                        is_vegetarian = data['Is_Vegetarian'].upper() == 'TRUE'
                        
                        if recipe_type.lower() == 'dessert':
                            sweetness = int(data['Sweetness_Level'])
                            return DessertRecipe(name, ingredients, steps, is_vegetarian, sweetness)
                        elif recipe_type.lower() == 'main course':
                            spice = int(data['Spice_Level'])
                            return MainCourseRecipe(name, ingredients, steps, is_vegetarian, spice)
                        else:
                            return None
                    except Exception as e:
                        print(f"Warning: Error processing line {i}: {e}")
                        return None
                
                all_recipes = [process_line((i, line)) for i, line in enumerate(lines[1:], 2)]
                recipes = [r for r in all_recipes if r is not None]
        
        if not recipes:
            print("Warning: No valid recipes were loaded from the file.")
        else:
            print(f"Successfully loaded {len(recipes)} recipes.")
        
        return (recipes, None)
        
    except FileNotFoundError:
        error_msg = f"Error: File '{filename}' not found. Please ensure the Excel file is in the same directory as this program."
        print(error_msg)
        return ([], error_msg)
    except KeyError as e:
        error_msg = f"Error: Missing required column in Excel file: {e}. Required columns: Name, Ingredients, Steps, Type, Is_Vegetarian, Sweetness_Level, Spice_Level"
        print(error_msg)
        return ([], error_msg)
    except Exception as e:
        error_msg = f"Error loading recipes: {e}"
        print(error_msg)
        return ([], error_msg)


def display_all_recipes(recipes):

    if not recipes:
        print("\nNo recipes available to display.")
        return
    
    print(f"\n{'-'*60}")
    print(f"ALL RECIPES ({len(recipes)} total)")
    print(f"{'-'*60}")
    
    for idx, recipe in enumerate(recipes, 1):
        print(f"\n{idx}. {recipe.get_name()}")
        if isinstance(recipe, DessertRecipe):
            sweetness = recipe.get_sweetness_level()
            if sweetness is not None:
                print(f"   Type: Dessert | Sweetness: {sweetness}/10")
            else:
                print("   Type: Dessert | Sweetness: Not specified")
        elif isinstance(recipe, MainCourseRecipe):
            spice = recipe.get_spice_level()
            if spice is not None:
                print(f"   Type: Main Course | Spice: {spice}/5")
            else:
                print("   Type: Main Course | Spice: Not specified")
        print(f"   Vegetarian: {'Yes' if recipe.get_is_vegetarian() else 'No'}")
    
    print(f"\n{'-'*60}")
    
    try:
        choice = input("\nEnter recipe number to view details (or press Enter to return): ").strip()
        if choice:
            idx = int(choice) - 1
            if 0 <= idx < len(recipes):
                recipes[idx].display_recipe()
            else:
                print("Invalid recipe number.")
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print(f"Error: {e}")


def search_recipe_by_name(recipes):

    if not recipes:
        print("\nNo recipes available to search.")
        return
    
    search_term = input("\nEnter recipe name to search: ").strip().lower()
    
    if not search_term:
        print("Search term cannot be empty.")
        return
    
    matches = [recipe for recipe in recipes if search_term in recipe.get_name().lower()]
    
    if not matches:
        print(f"\nNo recipes found matching '{search_term}'.")
    elif len(matches) == 1:
        print("\nFound 1 recipe:")
        matches[0].display_recipe()
    else:
        print(f"\nFound {len(matches)} recipes:")
        for idx, recipe in enumerate(matches, 1):
            print(f"\n{idx}. {recipe.get_name()}")
            if isinstance(recipe, DessertRecipe):
                sweetness = recipe.get_sweetness_level()
                if sweetness is not None:
                    print(f"   Type: Dessert | Sweetness: {sweetness}/10")
                else:
                    print("   Type: Dessert | Sweetness: Not specified")
            elif isinstance(recipe, MainCourseRecipe):
                spice = recipe.get_spice_level()
                if spice is not None:
                    print(f"   Type: Main Course | Spice: {spice}/5")
                else:
                    print("   Type: Main Course | Spice: Not specified")
        
        try:
            choice = input("\nEnter number to view details (or press Enter to return): ").strip()
            if choice:
                idx = int(choice) - 1
                if 0 <= idx < len(matches):
                    matches[idx].display_recipe()
                else:
                    print("Invalid recipe number.")
        except ValueError:
            print("Invalid input.")
        except Exception as e:
            print(f"Error: {e}")


def filter_recipes_by_type(recipes):

    if not recipes:
        print("\nNo recipes available to filter.")
        return
    
    print("\nFilter Options:")
    print("1. Desserts")
    print("2. Main Courses")
    print("3. Vegetarian Recipes")
    print("4. Non-Vegetarian Recipes")
    
    try:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        filtered = []
        filter_name = ""
        
        if choice == '1':
            filtered = [r for r in recipes if isinstance(r, DessertRecipe)]
            filter_name = "Desserts"
        elif choice == '2':
            filtered = [r for r in recipes if isinstance(r, MainCourseRecipe)]
            filter_name = "Main Courses"
        elif choice == '3':
            filtered = [r for r in recipes if r.get_is_vegetarian()]
            filter_name = "Vegetarian Recipes"
        elif choice == '4':
            filtered = [r for r in recipes if not r.get_is_vegetarian()]
            filter_name = "Non-Vegetarian Recipes"
        else:
            print("Invalid choice.")
            return
        
        if not filtered:
            print(f"\nNo {filter_name.lower()} found.")
            return
        
        print(f"\n{'-'*60}")
        print(f"{filter_name.upper()} ({len(filtered)} total)")
        print(f"{'-'*60}")
        
        for idx, recipe in enumerate(filtered, 1):
            print(f"\n{idx}. {recipe.get_name()}")
            if isinstance(recipe, DessertRecipe):
                sweetness = recipe.get_sweetness_level()
                if sweetness is not None:
                    print(f"   Sweetness: {sweetness}/10")
                else:
                    print("   Sweetness: Not specified")
            elif isinstance(recipe, MainCourseRecipe):
                spice = recipe.get_spice_level()
                if spice is not None:
                    print(f"   Spice: {spice}/5")
                else:
                    print("   Spice: Not specified")
            print(f"   Vegetarian: {'Yes' if recipe.get_is_vegetarian() else 'No'}")
        
        print(f"\n{'='*60}")
        
        view_choice = input("\nEnter recipe number to view details (or press Enter to return): ").strip()
        if view_choice:
            idx = int(view_choice) - 1
            if 0 <= idx < len(filtered):
                filtered[idx].display_recipe()
            else:
                print("Invalid recipe number.")
                
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"Error: {e}")


def display_menu():

    print("\n" + "-"*60)
    print("RECIPE MANAGEMENT SYSTEM")
    print("-"*60)
    print("1. View All Recipes")
    print("2. Search Recipe by Name")
    print("3. Filter Recipes by Type")
    print("4. Exit")
    print("-"*60)


def run_menu(recipes):

    display_menu()
    
    try:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            display_all_recipes(recipes)
            run_menu(recipes)
        elif choice == '2':
            search_recipe_by_name(recipes)
            run_menu(recipes)
        elif choice == '3':
            filter_recipes_by_type(recipes)
            run_menu(recipes)
        elif choice == '4':
            print("\n" + "-"*60)
            print("Thank you for using the Recipe Management System!")
            print("Goodbye!")
            print("-"*60 + "\n")
            return
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            run_menu(recipes)
            
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        run_menu(recipes)
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting.")
        return
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        run_menu(recipes)


def main():

    print("\n" + "-"*60)
    print("Welcome to the Recipe Management System!")
    print("-"*60)
    
    recipes, error = load_recipes_from_excel('recipe_data.xlsx')
    
    if error or not recipes:
        print("\nCannot proceed without recipe data. Exiting.")
        return
    
    run_menu(recipes)


if __name__ == "__main__":
    main()