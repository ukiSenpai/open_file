import os.path
from pprint import pprint

try:
    path = os.path.join(os.getcwd(), "open", "recipes.txt")
except:
    print("Файла нет!")

with open(path) as file:
    cook_book = {}
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



get_shop_list_by_dishes(["Омлет"], 2)
print("--------------------")
get_shop_list_by_dishes(["Омлет", "Омлет"], 1)

