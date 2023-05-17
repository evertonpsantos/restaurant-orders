from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1.
def test_ingredient():
    test_ingredient = Ingredient("carne")
    test_ingredient_equal = Ingredient("carne")
    test_ingredient2 = Ingredient("salmão")

    assert hash(test_ingredient) != hash(test_ingredient2)
    assert test_ingredient == test_ingredient_equal
    assert hash(test_ingredient) == hash(test_ingredient_equal)
    assert test_ingredient2.name == "salmão"
    assert repr(test_ingredient2) == "Ingredient('salmão')"
    assert test_ingredient_equal.restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }
