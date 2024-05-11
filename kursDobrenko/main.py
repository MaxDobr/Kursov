from datetime import date
from functions import json_load
from functions import date_sorter
from functions import number_formatter

# Создаем список из json-файла
first_list = json_load("../operations.json")

# Удаляем из списка пустые элементы
for item in first_list.copy():
    if item == {}:
        first_list.remove(item)

# Создаем список, сортированный по датам операций
second_list = date_sorter(first_list)

# Создаем список из последних 5 выполненных операций
third_list = []
counter = 0
for item_ in second_list:
    if item_["state"] == "EXECUTED" and counter != 5:
        third_list.append(item_)
        counter += 1

# Выводим эти операции в удобном для пользователя виде
for item__ in third_list:
    thedate = date.fromisoformat(item__["date"][0:10])
    date_formated = thedate.strftime("%d.%m.%Y")
    description = item__["description"]
    amount = item__["operationAmount"]["amount"]
    currency_type = item__["operationAmount"]["currency"]["name"]
    incoming_account = item__["to"].split(" ")
    incoming_account_str = f"{' '.join(incoming_account[:-1])}" + f" {number_formatter(incoming_account[-1])}"
    if "from" in item__:
        original_account = item__["from"].split(" ")
        original_account_str = f"{' '.join(original_account[:-1])}"+f" {number_formatter(original_account[-1])}"
        print(f"{date_formated} {description}\n"
              f"{original_account_str} -> {incoming_account_str}\n"
              f"{amount} {currency_type}\n\n")
    else:
        print(f"{date_formated} {description}\n"
              f"-> {incoming_account_str}\n"
              f"{amount} {currency_type}\n\n")
