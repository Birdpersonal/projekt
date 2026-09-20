# title = "Книга С.И. Змеев - Как стать змеей"
# price = 1200
# discount = 6
# sales = 241
#
# if sales > 150:
#     title += "[Популярно!]"
# if discount > 0:
#     title += "[Скидка]"
# if discount > 10:
#     title += "[Акция!]"
#
# print(title)


# python_count = int(input("Сколько питонов?"))
#
# last_digit = python_count % 10
#
# if 11 <= python_count <= 19:
#     morphy = "Питонов"
# elif last_digit == 1:
#     morphy = "Питон"
# elif 2 <= last_digit <= 4:
#     morphy = "Питона"
# else:
#     morphy = "Питонов"
#
# print(python_count, morphy)


# welcome = input("Привет!
# \nПредлагаю проверить свои знания английского!Напиши, как тебя зовут.")
# print(f"Привет {welcome}, начнем тренировку!")
# answer = 0
# score = 0
# question_1 = input("My name ___ Vova.")
# if question_1 == "is":
#     answer += 1
#     score += 10
#     print("Ответ верный!\nВы получаете 10 баллов!")
# else:
#     print("Неправильно.\nПравильный ответ: is")
#
# question_2 = input("I ___ a coder.")
# if question_2 == "am":
#     answer += 1
#     score += 10
#     print("Ответ верный!\nВы получаете 10 баллов!")
# else:
#     print("Неправильно.\nПравильный ответ: am")
#
# question_3 = input("I live ___ Moscow.")
# if question_3 == "in":
#     answer += 1
#     score += 10
#     print("Ответ верный!\nВы получаете 10 баллов!")
# else:
#     print("Неправильно.\nПравильный ответ: in")
#
# avr = int(answer / 3 * 100)
# print(f"Вот и всё, {welcome}!
# \nВы ответили на {answer} вопросов из 3 верно.\nВы заработали {score}
# баллов.Это {round(avr,2)} процентов.")


# shopping_list = ["яблоки", "молоко"]
# destination = input("Куда пойдем?")
# if destination in "на пикник":
#     shopping_list.append("шашлык")
#     shopping_list.append("дрова")
# elif destination in "в гости":
#     shopping_list.append("вино")
#     shopping_list.append("торт")
# elif destination in "никуда":
#     shopping_list.append("попкорн")
#     shopping_list.append("мороженое")
# else:
#     shopping_list.append("попкорн")
#     shopping_list.append("мороженое")
# print(f"Ваш список покупок: {len(shopping_list)} товара - {shopping_list}")


# expenses = [200, 450, 320, 1100, 650, 280, 325, 490, 830, 420]
# sum_expenses = 0
# for i in expenses:
#     sum_expenses += i
#
# print(f"Всего потрачено: {sum_expenses}")


# medals = ["gold", "gold", "silver","gold",
# "bronze", "silver", "gold", "gold", "silver", "chocolate"]
#
# gold_medals = 0
# silver_medals = 0
# bronze_medals = 0
# chocolate_medals = 0
#
# for i in medals:
#     if i == "gold":
#         gold_medals += 1
#     elif i == "silver":
#         silver_medals += 1
#     elif i == "bronze":
#         bronze_medals += 1
#     else:
#         chocolate_medals += 1
#
# print(f"""Золотых медалей: {gold_medals}
# Серебрянных медалей {silver_medals}
# Бронзовых медалей: {bronze_medals}
# Шоколадных медалей: {chocolate_medals}""")

# price = int(input("Введите полную сумму покупки: "))
# mount = int(input("Введите количество месяцев рассрочки: "))
# for i in range(1, 12):
#     payment_mount = int(price / i)
#
#     print(f"{i} месяц - {payment_mount} руб")

# print(f"Сумма вашей покупки: {price}. На {mount} месяцев.
# Ежемесячный платеж будет: {round(price / mount, 2)}")

# debt = 10000
#
# while True:
#
#     nums = int(input("Сколько готовы внести: "))
#     remains = debt - nums
#     debt -=nums
#     print(f"Ваш долг: {remains}")
#     if debt <= 0:
#         print("Ваши долги выплачены")
#         break

# ввод списков и счетчиков
# questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
# answers = ["is", "am", "in"]
# count = 0
# sum = 0
#
# #приветствие
# name = input("""Привет!
# Предлагаю проверить свои знания английского!
# Наберите "ready", чтобы начать!  """)
# if name == "ready":
#     #начало цикла
#     while sum <= 2:
#         answer = input(questions[sum])
#         if answer == answers[sum]:
#             print("Ответ верный!")
#             count += 1
#             sum += 1
#         else:
#             print(f"Неправильно. Правильный ответ: {answers[sum]}")
#             sum += 1
#     #подведение итогов
#     print(f"Вот и всё! Вы ответили на {count} вопросов из {len(questions)}
#     верно,это {round(count / len(answers) * 100, 2)} процентов.")
# else:
#     print("Кажется, вы не хотите играть. Очень жаль.")


# if name == "ready":
#     answer_1 = input(questions[0])
#     if answer_1 == answers[0]:
#         print("Ответ верный!")
#         count += 1
#     else:
#         print(f"Неправильно. Правильный ответ: {answers[0]}")
#     answer_2 = input(questions[1])
#     if answer_2 == answers[1]:
#         print("Ответ верный!")
#         count += 1
#     else:
#         print(f"Неправильно. Правильный ответ: {answers[1]}")
#     answer_3 = input(questions[2])
#     if answer_3 == answers[2]:
#         print("Ответ верный!")
#         count += 1
#     else:
#         print(f"Неправильно. Правильный ответ: {answers[2]}")
#
#     print(f"Вот и всё! Вы ответили на {count} вопросов из {len(questions)}
#     верно,это {round(count / len(answers) * 100, 2)} процентов.")
# else:
#     print("Кажется, вы не хотите играть. Очень жаль.")


# string = "Мама, я графоман, спасити!"
#
# letter_count = 0
# words_count = 0
#
# for i in string:
#     if i == " ":
#         words_count += 1
#     if i not in [",", ".", "!", " "]:
#         letter_count += 1
#
# print(f"Букв: {letter_count}")
# print(f"Количество слов: {words_count + 1}")


# messange = """всем привет кто пришел изучать #питон и добро пожаловать в чат!
# Будем тут общаться, учиться, делать приложения вместе с
# @happysnake, @angrycoder, @mewton
# """
#
# people_mentioned = []
# tags_mentioned = []
#
# messange_replace = messange.replace(",", " " )
# messange_split = messange.split()
# print(messange_split)
# for i in messange_split:
#     if i[0] == "@":
#         people_mentioned.append(i)
#     elif i[0] == "#":
#         tags_mentioned.append(i)
#
# people_mentioned_join = " ".join(people_mentioned)
# tags_mentioned_join = " ".join(tags_mentioned)
#
# print(f"Упомянуты люди: {people_mentioned_join}")
# print(f"Упомянуты теги: {tags_mentioned_join}")


# dictionary = {
#     "cat" : "кошка",
#     "dog" : "собака",
#     "own" : "сова"
# }
# while True:
#     user_input = input("ВВедите слово: ")
#     if user_input not in dictionary:
#         print("Не знаю таких слов")
#     else:
#         transete = dictionary[user_input]
#
#         print(f"Перевод: {transete}")


# store = {
#     "яблоки" : 100,
#     "груши" : 200,
#     "ананасы" : 300
# }
# user_input = input("Введите фрукт: ")
# user_input_2 = input("Введите вес в граммах: ")
# if user_input not in store:
#     print("Такого продукта в магазине нет")
# elif not user_input_2.isdigit():
#     print("Введите коректное число")
# else:
#     print(f"Продукт: {user_input}, весом: {user_input_2} грамм,
#     выходит по стоимости {store[user_input] * int(user_input_2) / 1000} ")


# guests = {
#     "Алексей" : 500,
#     "Василиса" : 1200,
#     "Олег" : 950,
#     "Даша" : 8000,
# }
# guests_name = ", ".join(guests.keys())
# print(f"Гости: {guests_name}. \nВсего к оплате: {sum(guests.values())}")


# my_skills = set(["python", "flask", "django", "критическое мышление",
# "планирование", "перегововры", "html", "css"])
#
# backend_skills  = {"linux", "terminal", "python", "flask", "django",
# "restapi"}
# frontend_skills = {"html", "css", "javascripts"}
# soft_skills = {"презентация", "планирование", "перегововры",
# "лидерство", "критическое мышление"}
#
# result_1 = frontend_skills.difference(my_skills)
# print(result_1)
# result_2 = my_skills.intersection(backend_skills)
# print(result_2)
# result_3 = backend_skills.union(frontend_skills)
# result_3_1 = my_skills.difference(result_3)
# print(result_3_1)
# result_4 = my_skills.issubset(soft_skills)
# print(result_4)
# result_5 = backend_skills.union((frontend_skills))
# print(result_5)


# def fullname_split(fullname_str):
#      # surname = "Гавривов"
#      # name = "Юлиан"
#      # patronymic = "Александрович"
#      name_eror = fullname_str.split()
#
#
#      return (name_eror[0], name_eror[1], name_eror[2])
# surname, name, patronymic = fullname_split("Гавривов Юлиан Александрович")
# print(name)


# store = [
#     {"name" : "Яблоки", "price" : "100", "available" : "40"},
#     {"name" : "Апельсины", "price" : "200", "available" : "20"},
#     {"name" : "Гранаты", "price" : "400", "available" : "5"}
# ]
#
# for i in store:
#     i["price"] = round(int(i["price"]) / 2)
#
# print(store)


# list = [1, 2, 3]
# for i in range(len(list):
#     print(i)


# words_to_decode = ['java', 'python', 'ruby', 'php', 'fortran',
# 'javascript', 'kotlin', 'swift', 'basic', 'pascal']


# def morse_encode(morse, word):
#     # word_split = list(word.split(','))
#     words = ""
#     for k in morse:
#         for i in word:
#             words += morse.get(i)
#             words += " "
#             # print(words)
#         return words
#
# print(morse_encode(morse, word = 'python'))

#
# # Пишите свой код ниже
# def morse_decode(morse, list_):
#     print(list_.split())
#     words = ""
#     for k in list_.split():
#         for i, v in morse.items():
#             if k == v:
#                 words += i
#     return words
#
# print(morse_decode(morse, '.--- .- ...- .-'))


# def calculate_total_cost(list_):
#     sum_ = 0
#
#     for i in list_:
#         for k, v in i.items():
#             if k == "price":
#                 sum_ += v * i["quantity"]
#
#     return sum_
#
# print(calculate_total_cost([
# {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
# {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
# {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5}]))


# Напишите функцию filter_products_by_price(),
# которая принимает на вход список продуктов и верхний порог цены
# и возвращает список продуктов,
# цена которых не превышает заданную максимальную цену. Если у
# продукта не указана цена, это не должно
# приводить к ошибке, при получении значения по ключу, если ключа
# в словаре нет - цена должна равняться 0
# (используйте метод get()).

# def filter_products_by_price(list_, max_price):
#     products_price = []
#     for i in list_:
#         i.get("price", 0)
#         if i["price"] <= max_price:
#             products_price.append(i)
#
#     return products_price
#

# # Пишите свой код ниже
#
# def filter_products_by_price(list_, max_price):
#     try:
#         products_price = []
#         for i in list_:
#             i.get("price", 0)
#             if i["price"] <= max_price:
#                 products_price.append(i)
#
#         return products_price
#     except:
#         return list_
#
#
# max_price = 200
# print(filter_products_by_price([{}], max_price))


# Пишите свой код ниже
# Вам предоставлен список словарей, в котором перечислены товары.
#
# Напишите функцию find_product_by_name(), которая принимает список
# продуктов и имя для поиска и возвращает
# информацию о продукте по его имени. Если продукт не найден в списке,
# функция возвращает строку «Продукт с
# таким именем не найден в списке». Если у продукта отсутствует имя,
# это не должно привести к ошибке.


# def find_product_by_name(list_, str_):
#     for i in list_:
#         if i.get("name") == str_:
#             return i
#     return "Продукт с таким именем не найден в списке"
#
# name = "Apple"
# print(find_product_by_name([
# {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
# {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5}, ],
# name))


# Вам предоставлен список словарей, в котором перечислены товары.
#
# Напишите функцию sort_products_by_quantity(). Функция должна
# принимать на вход список продуктов и
# направление сортировки (атрибут должен иметь имя ascending)
# со значением по умолчанию False (булевое значение)
# и сортировать продукты по количеству в порядке возрастания или убывания.
# Если в функцию не передан аргумент направления сортировки,
# сортировка должна проходить в порядке возрастания
# количества товаров (от меньшего к большему). Если у продукта
# не указано количество, это не должно привести к ошибке,
# при получении значения по ключу, если ключа в словаре
# нет - количество должно равняться 0 (используйте метод get()).

# products = [
# {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
# {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
# {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
# {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
# {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
# {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
# {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12,
# "brand": "ABC"},
# {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7,
# "brand": "XYZ"},
# {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3,
# "brand": "DEF", "discount": 10},
# {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
# {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30,
# "organic": True},
# {"name": "Chocolate", "category": "sweets", "price": 250,
# "quantity": 10, "brand": "GHI", "flavor": "Dark"}
# ]
#
#
# def sort_products_by_quantity(products, ascending=False):
#     result = sorted(
#     products, key=lambda p: p.get("quantity", 0), reverse=ascending)
#     return result
#
# sorted_by_quantity = sort_products_by_quantity([
# {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
# {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
# {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12,
#  "brand": "ABC"}], ascending=True)
# print(sorted_by_quantity)


# # Вам предоставлен список словарей, в котором перечислены товары.
# #
# # Напишите функцию average_price_per_category(), которая принимает
# на вход список продуктов и возвращает
# # новый словарь, где ключи — категории, а значения — средняя цена
# продуктов в каждой категории. Округлите
# # результат вычисления до 1 знака после запятой. Если у продукта
# отсутствует категория, это не должно привести к ошибке.
#
# def average_price_per_category(list_):
#     result = {}
#     for i in list_:
#         category = i.get("category", "unknown")
#         if "price" not in i:
#             continue
#         price = i.get("price")
#         if category not in result:
#             result[category] = []
#         result[category].append(price)
#         print(result)
#     for k, v in result.items():
#         avg_price = sum(v)/len(v)
#         result[k] = round(avg_price, 1)
#
#     return result
#
#
#
# print(average_price_per_category(products))


# Вам предоставлен список словарей в котором перечислены товары.
#
# Напишите функцию group_products_by_category(products), которая
# принимает на вход список продуктов и
# возвращает словарь, где ключи — категории, а значения — списки
# продуктов в каждой категории. Если у
# продукта отсутствует категория, это не должно привести к ошибке.
# Такой продукт игнорируется программой.

# def group_products_by_category(products: list[dict]) -> dict:
#     """функция которая возвращает словарь с категориями и
#     продуктами в каждой категории"""
#
#     result: dict = {}
#     for i in products:
#         if "category" in i:
#             category = i["category"]
#             if category not in result:
#                 result[category] = []
#             result[category].append(i)
#
#     return result
#
#
# grouped_by_category = group_products_by_category([{}])
# print(grouped_by_category)
#
#
# help(group_products_by_category)
