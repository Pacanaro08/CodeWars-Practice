import pytest, sys
sys.path.append('..')
from kata8 import cakes

@pytest.mark.parametrize('recipe, avaliable, expected', [
    ({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200,}, 2),
    ({"cream": 200,"flour": 300,"sugar": 150,"milk": 100,"oil": 100,}, {"sugar": 1700,"flour": 20000,"milk": 20000,"oil": 30000,"cream": 5000,},11),
    ({"apples": 3,"flour": 300,"sugar": 150,"milk": 100,"oil": 100,}, {"sugar": 500, "flour": 2000, "milk": 2000}, 0), 
    ({"eggs": 4, "flour": 400}, {}, 0),
    ({"cream": 1,"flour": 3,"sugar": 1,"milk": 1,"oil": 1,"eggs": 1,}, {"sugar": 1,"eggs": 1,"flour": 3,"cream": 1,"oil": 1,"milk": 1,}, 1),
])

def test_cakes(recipe, avaliable, expected):
    assert cakes(recipe, avaliable) == expected