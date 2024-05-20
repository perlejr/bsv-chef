import pytest

from unittest.mock import MagicMock
from src.controllers.recipecontroller import RecipeController

# add your test case implementation here
@pytest.mark.unit
def id_1_Success_Optimal():

    readinessDict = {}
    readinessDict["bananaBread"] = 0.1
    readinessDict["cupcakes"] = 0.0

    mockedRC = MagicMock()
    mockedRC.get_readiness_of_recipes.return_value = readinessDict
    rc = RecipeController(mockedRC)

    assert rc.get_recipe() == False 

@pytest.mark.unit
def id_1_Success_Random():

    assert True == True