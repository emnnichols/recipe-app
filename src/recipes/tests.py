from django.test import TestCase
from .models import Recipe

# Create your tests here.

class RecipeModelTest(TestCase):
  def setUpTestData():
    Recipe.objects.create(name='Tea', cooking_time=5, ingredients='tea leaves, water, sugar')
  
  # TEST RECIPE NAME
  def test_recipe_name(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('name').verbose_name

    self.assertEqual(field_label, 'name')

  def test_recipe_name_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('name').max_length

    self.assertEqual(max_length, 120)
  
  # TEST RECIPE COOKING TIME
  def test_cooking_time_min(self):
    recipe = Recipe.objects.get(id=1)
    value = recipe.cooking_time

    self.assertTrue(1 <= value <= 100)
  
  def test_cooking_time_type(self):
    recipe = Recipe.objects.get(id=1)
    value = recipe.cooking_time

    self.assertIsInstance(value, int)

  # TEST INGREDIENTS
  def test_ingredients_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('ingredients').max_length

    self.assertEqual(max_length, 200)
  
  # TEST DIFFICULTY
  def test_recipe_difficulty(self):
    recipe = Recipe.objects.get(id=1)
    difficulty = recipe.calc_difficulty()

    self.assertEqual(difficulty, 'Easy')