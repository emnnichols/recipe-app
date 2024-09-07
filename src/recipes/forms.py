from django import forms

CHART_CHOICES = {
  ('#1', 'Bar Chart'),
  ('#2', 'Pie Chart'),
  ('#3', 'Line Chart')
}

class RecipeSearchForm(forms.Form):
  recipe_search = forms.CharField(max_length=120, label='Enter Recipe / Ingredient', required=False)
  chart_type = forms.ChoiceField(choices=CHART_CHOICES, label='Choose a Chart Type')