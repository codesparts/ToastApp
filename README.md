# ToastAppAPI

### For Testing (First Time Only) -
    git clone https://github.com/codesparts/ToastAppAPI.git
    cd ToastAppAPI
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    ./app.py

### For Getting Recipes
[GET] http://localhost:8000/recipes?ingredients=<ingredient_list>&page=<page_no>

#### For Getting Directions
[GET] http://localhost:8000/recipe/<recipe_id>

### Get Items From Image
[POST] http://localhost:8000/image
In BODY for 'form-data' set image to uploaded file


