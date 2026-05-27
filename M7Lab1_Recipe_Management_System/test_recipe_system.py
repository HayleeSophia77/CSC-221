# Unit tests for Recipe Management System
# 12/07/2025
# M7 PyInstaller Assignment
# Haylee Paredes

import unittest
from recipe_classes import Recipe, DessertRecipe, MainCourseRecipe


class TestRecipeBaseClass(unittest.TestCase):
    
    def setUp(self):

        self.recipe = Recipe(
            name="Test Recipe",
            ingredients=["flour", "sugar", "eggs"],
            steps="Mix ingredients and bake at 350°F for 30 minutes",
            is_vegetarian=True
        )
    
    def test_recipe_creation(self):

        self.assertEqual(self.recipe.get_name(), "Test Recipe")
        self.assertEqual(len(self.recipe.get_ingredients()), 3)
        self.assertIn("flour", self.recipe.get_ingredients())
        self.assertTrue(self.recipe.get_is_vegetarian())
    
    def test_recipe_getters(self):

        self.assertEqual(self.recipe.get_name(), "Test Recipe")
        self.assertEqual(self.recipe.get_ingredients(), ["flour", "sugar", "eggs"])
        self.assertIn("Mix", self.recipe.get_steps())
        self.assertTrue(self.recipe.get_is_vegetarian())
    
    def test_recipe_setters(self):

        self.recipe.set_name("Updated Recipe")
        self.assertEqual(self.recipe.get_name(), "Updated Recipe")
        
        self.recipe.set_ingredients(["milk", "butter"])
        self.assertEqual(len(self.recipe.get_ingredients()), 2)
        
        self.recipe.set_steps("New steps")
        self.assertEqual(self.recipe.get_steps(), "New steps")
        
        self.recipe.set_is_vegetarian(False)
        self.assertFalse(self.recipe.get_is_vegetarian())
    
    def test_ingredients_list_conversion(self):

        recipe_with_string = Recipe("Test", "not a list", "steps", True)
        self.assertEqual(recipe_with_string.get_ingredients(), [])


class TestDessertRecipe(unittest.TestCase):
    
    def setUp(self):

        self.dessert = DessertRecipe(
            name="Chocolate Cake",
            ingredients=["chocolate", "eggs", "flour", "sugar"],
            steps="Mix, bake, and frost",
            is_vegetarian=True,
            sweetness_level=8
        )
        
        self.dessert_no_sweetness = DessertRecipe(
            name="Sugar-Free Cake",
            ingredients=["flour", "eggs"],
            steps="Bake",
            is_vegetarian=True,
            sweetness_level=None
        )
    
    def test_dessert_creation(self):

        self.assertEqual(self.dessert.get_name(), "Chocolate Cake")
        self.assertEqual(self.dessert.get_sweetness_level(), 8)
        self.assertTrue(self.dessert.get_is_vegetarian())
    
    def test_sweetness_level_getter(self):

        self.assertEqual(self.dessert.get_sweetness_level(), 8)
        self.assertIsNone(self.dessert_no_sweetness.get_sweetness_level())
    
    def test_sweetness_level_setter_valid(self):

        result = self.dessert.set_sweetness_level(5)
        self.assertTrue(result)
        self.assertEqual(self.dessert.get_sweetness_level(), 5)
        
        result = self.dessert.set_sweetness_level(1)
        self.assertTrue(result)
        self.assertEqual(self.dessert.get_sweetness_level(), 1)
        
        result = self.dessert.set_sweetness_level(10)
        self.assertTrue(result)
        self.assertEqual(self.dessert.get_sweetness_level(), 10)
    
    def test_sweetness_level_setter_invalid(self):

        result = self.dessert.set_sweetness_level(0)
        self.assertFalse(result)
        self.assertEqual(self.dessert.get_sweetness_level(), 8)
        
        result = self.dessert.set_sweetness_level(11)
        self.assertFalse(result)
        self.assertEqual(self.dessert.get_sweetness_level(), 8)
    
    def test_adjust_sweetness_increase(self):

        result = self.dessert.adjust_sweetness(2)
        self.assertIn("adjusted", result.lower())
        self.assertEqual(self.dessert.get_sweetness_level(), 10)
    
    def test_adjust_sweetness_decrease(self):

        result = self.dessert.adjust_sweetness(-3)
        self.assertIn("adjusted", result.lower())
        self.assertEqual(self.dessert.get_sweetness_level(), 5)
    
    def test_adjust_sweetness_at_limit(self):

        self.dessert.set_sweetness_level(10)
        result = self.dessert.adjust_sweetness(5)
        self.assertIn("remains", result.lower())
        self.assertEqual(self.dessert.get_sweetness_level(), 10)
        
        self.dessert.set_sweetness_level(1)
        result = self.dessert.adjust_sweetness(-5)
        self.assertIn("remains", result.lower())
        self.assertEqual(self.dessert.get_sweetness_level(), 1)
    
    def test_adjust_sweetness_none(self):

        result = self.dessert_no_sweetness.adjust_sweetness(2)
        self.assertIn("cannot adjust", result.lower())
        self.assertIsNone(self.dessert_no_sweetness.get_sweetness_level())
    
    def test_format_for_display(self):

        formatted = self.dessert.format_for_display()
        self.assertIn("Chocolate Cake", formatted)
        self.assertIn("8/10", formatted)
        self.assertIn("Vegetarian", formatted)


class TestMainCourseRecipe(unittest.TestCase):
    
    def setUp(self):

        self.main_course = MainCourseRecipe(
            name="Spaghetti Bolognese",
            ingredients=["spaghetti", "ground beef", "tomato sauce"],
            steps="Cook pasta, make sauce, combine",
            is_vegetarian=False,
            spice_level=3
        )
        
        self.main_course_no_spice = MainCourseRecipe(
            name="Plain Pasta",
            ingredients=["pasta"],
            steps="Boil",
            is_vegetarian=True,
            spice_level=None
        )
    
    def test_main_course_creation(self):

        self.assertEqual(self.main_course.get_name(), "Spaghetti Bolognese")
        self.assertEqual(self.main_course.get_spice_level(), 3)
        self.assertFalse(self.main_course.get_is_vegetarian())
    
    def test_spice_level_getter(self):

        self.assertEqual(self.main_course.get_spice_level(), 3)
        self.assertIsNone(self.main_course_no_spice.get_spice_level())
    
    def test_spice_level_setter_valid(self):

        result = self.main_course.set_spice_level(2)
        self.assertTrue(result)
        self.assertEqual(self.main_course.get_spice_level(), 2)
        
        result = self.main_course.set_spice_level(1)
        self.assertTrue(result)
        self.assertEqual(self.main_course.get_spice_level(), 1)
        
        result = self.main_course.set_spice_level(5)
        self.assertTrue(result)
        self.assertEqual(self.main_course.get_spice_level(), 5)
    
    def test_spice_level_setter_invalid(self):

        result = self.main_course.set_spice_level(0)
        self.assertFalse(result)
        self.assertEqual(self.main_course.get_spice_level(), 3)
        
        result = self.main_course.set_spice_level(6)
        self.assertFalse(result)
        self.assertEqual(self.main_course.get_spice_level(), 3)
    
    def test_adjust_spice_increase(self):

        result = self.main_course.adjust_spice_level(1)
        self.assertIn("adjusted", result.lower())
        self.assertEqual(self.main_course.get_spice_level(), 4)
    
    def test_adjust_spice_decrease(self):

        result = self.main_course.adjust_spice_level(-2)
        self.assertIn("adjusted", result.lower())
        self.assertEqual(self.main_course.get_spice_level(), 1)
    
    def test_adjust_spice_at_limit(self):

        self.main_course.set_spice_level(5)
        result = self.main_course.adjust_spice_level(3)
        self.assertIn("remains", result.lower())
        self.assertEqual(self.main_course.get_spice_level(), 5)
        
        self.main_course.set_spice_level(1)
        result = self.main_course.adjust_spice_level(-3)
        self.assertIn("remains", result.lower())
        self.assertEqual(self.main_course.get_spice_level(), 1)
    
    def test_adjust_spice_none(self):

        result = self.main_course_no_spice.adjust_spice_level(2)
        self.assertIn("cannot adjust", result.lower())
        self.assertIsNone(self.main_course_no_spice.get_spice_level())
    
    def test_format_for_display(self):

        formatted = self.main_course.format_for_display()
        self.assertIn("Spaghetti Bolognese", formatted)
        self.assertIn("3/5", formatted)
        self.assertIn("Non-Vegetarian", formatted)


class TestInheritance(unittest.TestCase):
    
    def test_dessert_is_recipe(self):

        dessert = DessertRecipe("Test", ["ingredient"], "steps", True, 5)
        self.assertIsInstance(dessert, Recipe)
        self.assertIsInstance(dessert, DessertRecipe)
    
    def test_main_course_is_recipe(self):

        main = MainCourseRecipe("Test", ["ingredient"], "steps", False, 3)
        self.assertIsInstance(main, Recipe)
        self.assertIsInstance(main, MainCourseRecipe)
    
    def test_dessert_has_recipe_methods(self):

        dessert = DessertRecipe("Test", ["flour"], "bake", True, 7)
        self.assertTrue(hasattr(dessert, 'get_name'))
        self.assertTrue(hasattr(dessert, 'set_name'))
        self.assertTrue(hasattr(dessert, 'get_ingredients'))
        self.assertTrue(hasattr(dessert, 'display_recipe'))
    
    def test_main_course_has_recipe_methods(self):

        main = MainCourseRecipe("Test", ["pasta"], "boil", False, 2)
        self.assertTrue(hasattr(main, 'get_name'))
        self.assertTrue(hasattr(main, 'set_name'))
        self.assertTrue(hasattr(main, 'get_ingredients'))
        self.assertTrue(hasattr(main, 'display_recipe'))


if __name__ == '__main__':

    unittest.main(verbosity=2)






