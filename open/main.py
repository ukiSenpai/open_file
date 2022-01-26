import os.path
import sys
from pprint import pprint




def get_shop_list_by_dishes(dishes, person_count):
    sum_ingredient = {}
    for dish in dishes:
        for ingredients in cook_book[dish]:
            ingredient_name, quantity, measure = ingredients.values()
            if ingredient_name in sum_ingredient:
                sum_ingredient[ingredient_name]["quantity"] += (int(quantity) * person_count)
            else:
                sum_ingredient[ingredient_name] = {"measure": measure, "quantity": (int(quantity) * person_count)}

    pprint(sum_ingredient)





def parse_dish_book(path):
    with open(path, encoding="UTF-8") as file:
        for dish in file:
            dish_name = dish.strip()
            count = int(file.readline().strip())
            value_data = []
            for ingredients in range(count):
                ingredient_name, quantity, measure = file.readline().strip().split(" | ")
                value_data.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})

            cook_book[dish_name] = value_data
            file.readline()

    pprint(cook_book)
    print("--------------------")


if __name__ == '__main__':
    cook_book = {}
    path = os.path.join(os.getcwd(), "recipes.txt")
    if not os.path.exists(path):
        print(f"file {path} not exists")
        sys.exit(1)
    parse_dish_book(path)
    get_shop_list_by_dishes(["Омлет"], 2)
    print("--------------------")
    get_shop_list_by_dishes(["Омлет", "Омлет"], 1)