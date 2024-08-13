from .models import Recipe
from io import BytesIO
import base64
import matplotlib.pyplot as plt

# define a function that takes the ID
def get_recipename_from_id(val):
    # this ID is used to retrieve the name from the record
    recipename=Recipe.objects.get(recipe_id=val)   
    # the name is returned
    return recipename

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()

    return graph

def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig=plt.figure(figsize=(6,3))
    # Counting the number of ingredients for each recipe
    data['no_ingredients'] = data['ingredients'].apply(lambda x: len(x.split(',')))

    # Bar chart
    if chart_type =='#1':
        plt.bar(data['name'], data['cooking_time'])
        plt.xlabel('Recipe Name')
        plt.ylabel('Number of Minutes')
        plt.title('Bar Chart of Cooking Time')

    # Pie chart
    elif chart_type == '#2':
        plt.pie(data['no_ingredients'], labels=data['name'], autopct='%1.1f%%' )
        plt.title('Pie Chart of Number of Ingredients')

    # Line chart
    elif chart_type == '#3':
        plt.plot(data['name'], data['no_ingredients'])
        plt.xlabel('Recipe Name')
        plt.ylabel('Number of Ingredients')
        plt.title('Line Chart of Number of Ingredients')

    else:
        print('Unknown chart type')

    plt.tight_layout()

    chart = get_graph()
    return chart