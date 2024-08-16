from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Recipe
# to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm, RecipeForm
import pandas as pd
from .utils import get_recipename_from_id, get_chart
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

@login_required
def search_view(request):
    form = RecipeSearchForm(request.POST or None)
    recipe_df = None
    chart = None

    # check if button is clicked
    if request.method =='POST':
        # search_term = request.POST.get('search_term')
        chart_type = request.POST.get('chart_type')
        
        # apply filter to extract data
        qs = Recipe.objects.filter()
        if qs:
            recipe_df=pd.DataFrame(qs.values())
            # recipe_df['Link'] = recipe_df.apply(lambda row: f'<a href="./detail.html?{row["recipe_id"]}" target="_blank">{row["name"]}</a>', axis=1)
            chart=get_chart(chart_type, recipe_df, labels=recipe_df['name'].values)
            recipe_df=recipe_df.to_html(escape=False)
        
    context={
        'form': form,
        'recipe_df': recipe_df,
        'chart': chart,
    }
        # load the search page
    return render(request, 'recipes/search.html', context)

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipe_list')  # Redirect to the recipe list after saving
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})
