from django.test import TestCase, Client
from .models import Recipe
from .forms import RecipeSearchForm

# Create your tests here.

class RecipeModelTest(TestCase):
  ## 
  # Creates recipe object for Tea to use for testing
  ##
  def setUpTestData():
    Recipe.objects.create(name='Tea', cooking_time=5, ingredients='tea leaves, water, sugar')
  
  ## TEST RECIPE NAME
  # store test recipe object and verbose_name metadata
  ##
  def test_recipe_name(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('name').verbose_name

    self.assertEqual(field_label, 'name')

  ## TEST RECIPE NAME LENGTH
  # store test recipe object and max_length metadata
  # compares the max_length of the field equals 120
  ##
  def test_recipe_name_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('name').max_length

    self.assertEqual(max_length, 120)
  
  ## TEST RECIPE COOKING TIME
  # stores cooking_time value from test recipe object
  # checks if value is more than/equal or less than/equal to 1 and 100, respectively
  ##
  def test_cooking_time_min(self):
    recipe = Recipe.objects.get(id=1)
    value = recipe.cooking_time

    self.assertTrue(1 <= value <= 100)
  
  ## TEST RECIPE COOKING TIME TYPE
  # stores cooking_time value from test recipe object
  # checks if value is an integer
  ##
  def test_cooking_time_type(self):
    recipe = Recipe.objects.get(id=1)
    value = recipe.cooking_time

    self.assertIsInstance(value, int)

  ## TEST INGREDIENTS
  # stores max_length parameter of the ingredients field
  # compares the max_length of the field equals 120
  ##
  def test_ingredients_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('ingredients').max_length

    self.assertEqual(max_length, 200)
  
  ## TEST DIFFICULTY
  # calls the calc.difficulty() on the test recipe object
  # based on the number of ingredients and cooking time, difficulty should equal Easy
  ##
  def test_recipe_difficulty(self):
    recipe = Recipe.objects.get(id=1)
    difficulty = recipe.calc_difficulty()

    self.assertEqual(difficulty, 'Easy')

  ## TEST RECIPE URL
  # absolute url retrieved should equal /recipes/<pk>
  ## 
  def test_get_absolute_url(self):
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(recipe.get_absolute_url(), '/recipes/1')

  ## TEST INGREDIENT LIST
  # Gets length of ingredient list and compares value
  ##
  def test_ingredient_list(self):
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(len(recipe.get_ingredient_list()), 3)

class RecipeFormTest(TestCase):

  def setUpTestData():
    Recipe.objects.create(name='Tea', cooking_time=5, ingredients='tea leaves, water, sugar')
    Recipe.objects.create(name='Lemon Rice', cooking_time=30, ingredients='lemons, rice, water')

  ## TEST SEARCH FUNCTION
  def test_search_request(self):
    client = Client()

    data = {'recipe_search': 'sugar', 'chart_type': '#1'}
    response = client.post('/recipes/search', data)

    self.assertEqual(response.status_code, 200)

  def test_form_valid(self):
    data = {'recipe_search': 'sugar', 'chart_type': '#1'}
    response = RecipeSearchForm(data)

    self.assertTrue(response.is_valid())
  
  def test_search_ingredient(self):
    client = Client()

    input = {'recipe_search': 'water', 'chart_type': '#1'}
    response = client.post('/recipes/search', input)
    data = response.content
    
    self.assertTrue('Tea' in data.decode())
    self.assertTrue('Lemon Rice' in data.decode())

  def test_search_recipe(self):
    client = Client()

    input = {'recipe_search': 'lemon rice', 'chart_type': '#1'}
    response = client.post('/recipes/search', input)
    data = response.content
    
    self.assertTrue('Lemon Rice' in data.decode())