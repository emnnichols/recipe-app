from django.db import models
from django.shortcuts import reverse
## 
# Imported Value Validators
# To ensure cooking time is at least 1 minute and no more than 100 minutes
##
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Recipe(models.Model):
  name = models.CharField(max_length=120)
  ##
  #  Ensure cooking time is a positive integer and at least a minute
  ##
  cooking_time = models.PositiveIntegerField(help_text='must be in minutes', validators=[MinValueValidator(1), MaxValueValidator(100)])
  ingredients = models.CharField(max_length=200, help_text='Ingredients must be separated by commas.')
  pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
  ##
  # Gets cooking time and ingredients from self
  # Splits the ingredient list at each comma in order to find list length
  # These values are used to calculate the recipes difficulty when called
  ##
  def calc_difficulty(self):
    time = self.cooking_time
    num_ing = len(self.ingredients.split(', '))
    ##
    # Checks if cooking time is less than or more than/equal to 10 minutes
    # For either time, it then checks if number of ingredients is less than or more than/eqaual to 4
    ##
    if time < 10:
      if num_ing < 4:
        difficulty = 'Easy'
        return difficulty
      elif num_ing >= 4:
        difficulty = 'Medium'
        return difficulty
    elif time >= 10:
      if num_ing < 4:
        difficulty = 'Intermediate'
        return difficulty
      elif num_ing >= 4:
        difficulty = 'Hard'
        return difficulty
      
  def __str__(self):
    return str(self.name)
  
  def get_ingredient_list(self):
    cleaned_ing = self.ingredients.strip()
    return cleaned_ing.split(',')

  def get_absolute_url(self):
    return reverse ('recipes:detail', kwargs={'pk': self.pk})