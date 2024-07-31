from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):

    def setUpTestData():
        Recipe.objects.create(name='Salad', ingredients='Lettuce, Cheese, Tomato', cooking_time='5', difficulty='Easy')

    def test_recipe_name(self):
        recipe = Recipe.objects.get(recipe_id=1)

        field_label = recipe._meta.get_field('name').verbose_name

        self.assertEqual(field_label, 'name')

    def test_ingredients_max_length(self):
        recipe = Recipe.objects.get(recipe_id=1)

        max_length = recipe._meta.get_field('ingredients').max_length

        self.assertEqual(max_length, 120)

    def test_cooking_time(self):
        recipe = Recipe.objects.get(recipe_id=1)

        field_label = recipe._meta.get_field('cooking_time').verbose_name

        self.assertEqual(field_label, 'cooking time')
        
    def test_difficulty(self):
        recipe = Recipe.objects.get(recipe_id=1)

        field_label = recipe._meta.get_field('difficulty').verbose_name

        self.assertEqual(field_label, 'difficulty')