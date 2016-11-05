#!/usr/bin/python
from flask import Flask, jsonify, request
from getRecipe import Recipe
from getDetail import RecipeDetail
from imageRec import Image

app = Flask(__name__)


@app.route('/image', methods=['GET', 'POST'])
def imageRecog():
    if request.method == 'POST':
        image_file = request.files['image']
        obj = Image(image_file.read())
        return jsonify(obj.getIng())


@app.route('/recipes', methods=['GET'])
def getRecipe():
    ing = request.args.get('ingredients')
    page = request.args.get('page')
    obj = Recipe(ing, page)
    return jsonify(obj.returnRecipe())


@app.route('/recipe/<string:recipe_id>', methods=['GET'])
def getRecipes(recipe_id):
    obj = RecipeDetail(recipe_id)
    return jsonify(obj.return_detail())


if __name__ == '__main__':
    app.run(port=8000, debug=True)
