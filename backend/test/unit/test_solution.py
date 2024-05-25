import pytest

from unittest.mock import MagicMock, patch
from src.controllers.recipecontroller import RecipeController
from src.static.diets import Diet

# add your test case implementation here
@pytest.mark.unit
def test_id_1():
    with patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes', autospec=True) as mocked_readiness_recipies:
        readinessDict = {}
        mocked_readiness_recipies.return_value = readinessDict
        mockedDao = MagicMock()
        rc = RecipeController(dao=mockedDao)
        diet = Diet.VEGAN

    assert rc.get_recipe(diet, True) == None 
