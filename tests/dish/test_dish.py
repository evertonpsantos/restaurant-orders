import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import (
    Ingredient,
    Restriction,
)


# Req 2
def test_dish():
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Baozi", -33.34)

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Baozi", "Trinta e três")

    test_recipe = Dish("Jiaozi", 35.55)
    test_recipe_equal = Dish("Jiaozi", 35.55)
    test_recipe_different = Dish("Baozi", 33.34)

    assert test_recipe.name == "Jiaozi"
    assert test_recipe.price == 35.55

    assert test_recipe == test_recipe_equal
    assert test_recipe != test_recipe_different
    assert hash(test_recipe) == hash(test_recipe_equal)
    assert hash(test_recipe) != hash(test_recipe_different)
    assert repr(test_recipe) == "Dish('Jiaozi', R$35.55)"
    assert repr(test_recipe_different) == "Dish('Baozi', R$33.34)"

    test_recipe.add_ingredient_dependency(Ingredient("carne"), 1)
    assert test_recipe.get_ingredients() == {Ingredient("carne")}
    assert test_recipe.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
