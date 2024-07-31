from django.db import models

# Create your models here.
class Recipe(models.Model):
    # Class attributes
    recipe_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    ingredients = models.CharField(
        max_length=120,
        help_text="Enter the ingredients, separated by a comma"
    )
    cooking_time= models.IntegerField(help_text="Enter the cooking time in minutes")
    difficulty= models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

