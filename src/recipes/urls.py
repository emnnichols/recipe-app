from django.urls import path
from .views import RecipeListView, RecipeDetailView, get_queryset

app_name = 'recipes'

## Maps the '' address to the home function-based view
urlpatterns = [
  path('recipes/', RecipeListView.as_view(), name='list'),
  path('recipes/search', get_queryset, name='search'),
  path('recipes/<pk>', RecipeDetailView.as_view(), name='detail'),
]