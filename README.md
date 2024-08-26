# Recipe App
## Overview
The recipe app is a web application built with Python using the Django framework with recipes being stored in a SQLite database. 
Recipe app allows users to sign up, login, and logout; while using the application, users can create, modify, and search recipes. 
While looking at a list of recipes, users can also request more details about a recipe -- such as name, cooking time, ingredient list, and difficulty (which is automatically calculated by cooking time and number of ingredients)

## Apps
### recipes

<details>
<summary> models </summary>
  
#### The Recipe model includes the following:
  
  - `name` ( CharField, max length of 120 )
  - `cooking_time` ( Positive Integer, must be in the range of 1 - 100, should be given in minutes )
  - `ingredients` ( CharField, max length of 200, each ingredient should be separated by a comma )
  - Defines the `calc_difficulty` function to calculate a recipes difficulty given the num of ingredients and cooking time

</details>

<details>
<summary> tests </summary>

#### `RecipeModelTest` creates the following test data:
  ```
  name = 'Tea'
  cooking_time = 5
  ingredients = 'tea leaves, water, sugar'
  ```

#### `RecipeModelTest` includes the following tests:

##### `test_recipe_name`
  > checks if object name and the verbose_name of the `name` field are equal

##### `test_recipe_name_max_length`
  > checks if the parameter `max_length` for `name` equals 120

##### `test_cooking_time_min`
  > checks if the `cooking_time` value is between 1 and 100

##### `test_cooking_time_type`
  > checks if the `cooking_time` value is an integer

##### `test_ingredients_max_length`
  > checks if the parameter `max_length` for `ingredients` equals 200

##### `test_recipe_difficulty`
  > calls `calc_difficulty()` on test recipe to ensure it calculates the expected 'Easy' difficulty

</details>

<details>
<summary> views </summary>
  
##### home
  > Accepts web request

  > Returns the `recipes/recipes_home.html` template

</details>
