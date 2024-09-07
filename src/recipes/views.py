from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .forms import RecipeSearchForm
from .models import Recipe
from .utils import get_chart

import pandas as pd

# Create your views here.
@login_required
def get_queryset(request):
    form = RecipeSearchForm(request.POST or None)
    # Initialize dataframe
    recipes_df = None
    qs = None
    chart = None

    if request.method == 'POST':
      recipe_search = request.POST.get('recipe_search')
      chart_type = request.POST.get('chart_type')

      qs = Recipe.objects.filter(
          Q(name__icontains=recipe_search) |
          Q(ingredients__icontains=recipe_search) |
          Q(name=recipe_search)
        )

      if qs:
        recipes_df = pd.DataFrame(qs.values())

        chart = get_chart(chart_type, recipes_df, recipe_search)

        #convert the dataframe to HTML
        recipes_df=recipes_df.to_html()

      else:
        qs = 'No recipes found'

    context = {
      'form': form,
      'recipes_df': recipes_df,
      'qs': qs,
      'chart': chart}

    return render(request, 'recipes/recipe_search.html', context)

class RecipeListView(LoginRequiredMixin, ListView):
  model = Recipe
  template_name = 'recipes/recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = Recipe
  template_name = 'recipes/recipe_detail.html'