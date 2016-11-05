#!bin/python
import requests
import json
from apiKey import API_KEY


class Recipe(object):
    def __init__(self, ing, page):
        self.ing = ing
        self.page = page

    def valid(self, inp):
        valid_publishers = ['All Recipes', 'Back to Her Roots', 'BBC Food', 'Bon Appetit', 'Closet Cooking',
                            'Cookin Canuck', 'Epicurious', 'Food Republic', 'Framed Cooks', 'Healthy Delicious',
                            'Jamie Oliver', "Lisa's Kitchen", "My Baking Addiction", "Panini Happy", "PBS Food",
                            "Pillsbury Baking", "Real Simple", "Two Peas and Their Pod", "Vintage Mixer",
                            "What's Gaby Cooking", "Whats Gaby Cooking"]
        if inp in valid_publishers:
            return True
        return False

    def returnRecipe(self):
        response = list()
        num = 0
        page = requests.get(
            'http://food2fork.com/api/search?key=' + API_KEY + '&q=' + self.ing + '&page=' + str(self.page))
        parsed = json.loads(page.text)
        count = parsed['count']
        for i in range(0, count):
            if self.valid(parsed['recipes'][i]['publisher']):
                temp = {'title': parsed['recipes'][i]['title'], 'id': parsed['recipes'][i]['recipe_id']}
                response.append(temp)
                num += 1
        return response

