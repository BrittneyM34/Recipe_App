from django import forms

CHART_CHOICES = (
    ('#1', 'Bar Chart'),
    ('#2', 'Pie Chart'),
    ('#3', 'Line Chart'),
)

# Define class-based form
class RecipeSearchForm(forms.Form):
    search_term = forms.CharField(max_length=200, required=False, label="Search Recipes")
    ingredients = forms.CharField(max_length=200, required=False)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)

