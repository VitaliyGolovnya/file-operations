def read_cookbook (f="cookbook.txt", mode="rt"):
    cook_book = {}
    with open (f, mode, encoding="utf-8") as file:
        while True:
            dish = file.readline().strip()
            if not dish:
                break
            cook_book[dish] = []
            ingredients = dict()
            for i in range(int(file.readline())):
                lst = file.readline().strip().split(" | ")
                ingredients["ingredient_name"] = lst[0]
                ingredients["quantity"] = int(lst[1])
                ingredients["measure"] = lst[2]
                cook_book[dish] += [ingredients.copy()]
            file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes: list, person_count: int):
    shopping_list = dict()
    for dish in dishes:
        for ingredient in read_cookbook()[dish]:
            if ingredient["ingredient_name"] in shopping_list.keys():
                shopping_list[ingredient["ingredient_name"]]["quantity"] += ingredient["quantity"] * person_count
            else:
                shopping_list[ingredient["ingredient_name"]] = {
                    "measure" : ingredient["measure"],
                    "quantity" : ingredient["quantity"] * person_count 
                    }
    return shopping_list

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))