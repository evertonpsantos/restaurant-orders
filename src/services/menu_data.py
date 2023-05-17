from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.populate_menu(source_path)

    def populate_menu(self, path):
        menu = dict()
        file_content = self.read_file_data(path)

        for dish in file_content:
            new_dish = Dish(dish["dish"], float(dish["price"]))

            if new_dish not in menu:
                menu[new_dish] = new_dish

            menu[new_dish].add_ingredient_dependency(
                Ingredient(dish["ingredient"]),
                int(dish["recipe_amount"])
            )

        return set(menu)

    def read_file_data(self, source_path):
        with open(source_path) as file:
            return list(csv.DictReader(file))
