from django.test import TestCase
from .models import Recipe
from .forms import RecipeSearchForm
from django.contrib.auth.models import User

# Create your tests here.
class RecipeModelTest(TestCase):
    # set up non-modified objects used by all test methods
    def setUpTestData():
        Recipe.objects.create(
            name = "Salad",
            ingredients = "Lettuce, Shredded Cheese, Tomato",
            cooking_time = 5,
        )

    # NAME
    def test_recipe_name(self):
        # get a recipe object to test
        recipe = Recipe.objects.get(recipe_id=1)

        # get metadata for 'name' field and use it to query its data
        field_label = recipe._meta.get_field("name").verbose_name

        # compare the value to the expected result
        self.assertEqual(field_label, "name")

    def test_recipe_name_max_length(self):
        # get a recipe object to test
        recipe = Recipe.objects.get(recipe_id=1)

        # get metadata for 'name' field and use it to query its data
        max_length = recipe._meta.get_field("name").max_length

        # compare the value to the expected result
        self.assertEqual(max_length, 50)

    # INGREDIENTS
    def test_ingredients_max_length(self):
        # get a recipe object to test
        recipe = Recipe.objects.get(recipe_id=1)

        # get metadata for 'ingredients' field and use it to query its data
        max_length = recipe._meta.get_field("ingredients").max_length

        # compare the value to the expected result
        self.assertEqual(max_length, 225)

    # COOKING TIME
    def test_cooking_time_value(self):
        # get a recipe object to test
        recipe = Recipe.objects.get(recipe_id=1)

        # get metadata for 'cooking_time' field and use it to query its data
        cooking_time_value = recipe.cooking_time

        # compare the value to the expected result
        self.assertIsInstance(cooking_time_value, int)

    # DIFFICULTY
    def test_difficulty_calculation(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(recipe_id=1)

        # Call the method to calculate difficulty 
        calculated_difficulty = recipe.calculate_difficulty()

        # Assert the result
        self.assertEqual(calculated_difficulty, 'Easy')

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(recipe_id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')

class RecipeFormTest(TestCase):

    def test_form_validity(self):
        # form with all fields filled
        form_data = {
            'search_term': 'Salad',
            'ingredients': 'Lettuce, Tomato, Cheese',
            'chart_type': '#1',
        }
        form = RecipeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cooking_time_validation(self):
        form_data_invalid = {
            'cooking_time': -2
        }
        form_invalid = RecipeSearchForm(data=form_data_invalid)
        self.assertFalse(form_invalid.is_valid())


class RecipeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        # Set up data for the view tests.
        cls.recipe = Recipe.objects.create(
            name='View Test Recipe',
            ingredients='Ingredient1,Ingredient2,Ingredient3',
            cooking_time=20,
            difficulty='Medium',
        )

        # For the test_login_required_for_list_view
    def test_login_required_for_list_view(self):
        response = self.client.get('/list/')
        self.assertRedirects(response, '/login/?next=/list/')

    # For the test_login_required_for_detail_view
    def test_login_required_for_detail_view(self):
        response = self.client.get(f'list/{self.recipe.pk}/')
