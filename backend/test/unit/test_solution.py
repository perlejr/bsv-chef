import pytest

from unittest.mock import MagicMock, patch
from src.controllers.recipecontroller import RecipeController
from src.static.diets import Diet

# add your test case implementation here
@pytest.mark.unit
def test_id_1():
    mockedDao = MagicMock()
    rc = RecipeController(items_dao=mockedDao)
    with patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes', autospec=True) as mocked_get_readiness_of_recipes:
        readinessDict = { "Waffles": 0.5, "Bananabread": 0.7, "Pancakes": 0.2}
        mocked_get_readiness_of_recipes.return_value = readinessDict
        diet = Diet.VEGETARIAN

        assert rc.get_recipe(diet, True) ==  "Bananabread"

@pytest.mark.unit
def test_id_2():
    mockedDao = MagicMock()
    rc = RecipeController(items_dao=mockedDao)
    with patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes', autospec=True) as mocked_get_readiness_of_recipes:
        readinessDict = { "Waffles": 0.5, "Bananabread": 0.7, "Pancakes": 0.2, "Random": 0.0}
        mocked_get_readiness_of_recipes.return_value = readinessDict
        diet = Diet.VEGETARIAN
        with patch('random.randint') as mockrandint:
            mockrandint.return_value = 3

            assert rc.get_recipe(diet, False) ==  "Random" 

@pytest.mark.unit
def test_id_3():
    with patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes', autospec=True) as mocked_readiness_recipes:
        readinessDict = {}
        mocked_readiness_recipes.return_value = readinessDict
        mockedDao = MagicMock()
        rc = RecipeController(items_dao=mockedDao)
        diet = Diet.VEGAN

    assert rc.get_recipe(diet, True) == None 
