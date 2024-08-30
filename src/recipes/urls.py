from django.urls import path
from .views import home, RecipeListView, RecipeDetailView

app_name = 'recipes'

## Maps the '' address to the home function-based view
urlpatterns = [
  path('', home),
  path('recipes/', RecipeListView.as_view(), name='list'),
  path('recipes/<pk>', RecipeDetailView.as_view(), name='detail'),
]