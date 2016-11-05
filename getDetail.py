#!bin/python
from lxml import html
import requests
import json
import apiKey

publisher_tag = {"All Recipes": '//span[@class="recipe-directions__list--item"]/text()',
                 "Back to Her Roots": '//li[@class="instruction"]/text()',
                 "BBC Food": '//p[@class="recipe-method__list-item-text"]/text()',
                 "Bon Appetit": '//div[@class="text" and @itemprop="recipeInstructions"]/text()',
                 "Closet Cooking": '//li[@itemprop="recipeInstructions"]/text()',
                 "Cookin Canuck": '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()',
                 "Epicurious": '//li[@class="preparation-step"]/text()',
                 "Food Republic": '//span[@itemprop="recipeInstructions"]/ol/li/text()',
                 "Framed Cooks": '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()',
                 "Healthy Delicious": '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()',
                 "Jamie Oliver": '//ol[@class="recipeSteps"]/li/text()',
                 "Lisa's Kitchen": '//li[@itemprop="recipeInstructions"]/p/text()',
                 "My Baking Addiction": '//span[@itemprop="recipeInstructions"]/ol/li/text()',
                 "Panini Happy": '//li[@class="instruction"]/text()',
                 "PBS Food": '//ol[@class="instructions"]/li/span[@class="txt"]/text()',
                 "Pillsbury Baking": '//ul[@itemprop="recipeInstructions"]/li/text()',
                 "Real Simple": '//section[@class="directions recipe-info-section" and @itemprop="recipeInstructions"]/div/ol/li/text()',
                 "Two Peas and Their Pod": '//div[@class="instructions" and @itemprop="recipeInstructions"]/p/text()',
                 "Vintage Mixer": '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()',
                 "Whats Gaby Cooking": '//li[@class="instruction" and @itemprop="recipeInstructions"]/text()'}


class RecipeDetail(object):
    def __init__(self, id):
        self.id = id

    def return_detail(self):
        page = requests.get('http://food2fork.com/api/get?key=' + apiKey.API_KEY + '&rId=' + self.id)
        parsed = json.loads(page.text)

        if parsed['recipe']['publisher'] in publisher_tag:
            tag = publisher_tag[parsed['recipe']['publisher']]
        else:
            tag = 404

        if tag == 404:
            return {'status': 'false'}
        else:
            tree = html.fromstring(requests.get(parsed['recipe']['source_url']).content)
            directions = tree.xpath(tag)
            return {'status': 'true',
                    'title': parsed['recipe']['title'],
                    'image_url': parsed['recipe']['image_url'],
                    'ingredients': parsed['recipe']['ingredients'],
                    'direction': directions}
