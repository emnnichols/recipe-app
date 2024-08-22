from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Recipe(models.Model):
  name = models.CharField(max_length=120)
  cooking_time = models.PositiveIntegerField(help_text='must be in minutes', validators=[MinValueValidator(1), MaxValueValidator(100)])
  ingredients = models.CharField(max_length=200, help_text='Ingredients must be separated by commas.')

  def calc_difficulty(self):
    time = self.cooking_time
    num_ing = len(self.ingredients.split(', '))

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