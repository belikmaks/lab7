institutions = {
    "Школа": [1000, 1200, 350],
    "Технікум": [200, 100],
    "Училище": [200],
}

def display_values(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def add_entry(dictionary, key, value):
    if key in dictionary:
        print(f"Запис з ключем '{key}' вже існує!")
    else:
        dictionary[key] = value
        print(f"Запис '{key}' додано.")

def remove_entry(dictionary, key):
    try:
        del dictionary[key]
        print(f"Запис '{key}' видалено.")
    except KeyError:
        print(f"Запис з ключем '{key}' не знайдено!")

def display_sorted(dictionary):
    for key in sorted(dictionary.keys()):
        print(f"{key}: {dictionary[key]}")

def sum_school_students(dictionary):
    if "Школа" in dictionary:
        total_students = sum(dictionary["Школа"])
        print(f"Кількість учнів шкіл: {total_students}")
    else:
        print("У словнику немає даних про 'Школа'")

def main():
    while True:
        print("\nОберіть дію:")
        print("1 - Вивести всі значення словника")
        print("2 - Додати запис до словника")
        print("3 - Видалити запис зі словника")
        print("4 - Вивести словник за відсортованими ключами")
        print("5 - Обчислити загальну кількість учнів шкіл")
        print("0 - Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            display_values(institutions)
        elif choice == "2":
            key = input("Введіть назву закладу: ")
            values = input("Введіть кількість учнів через кому (наприклад: 300, 400): ").split(',')
            values = [int(v.strip()) for v in values]
            add_entry(institutions, key, values)
        elif choice == "3":
            key = input("Введіть назву закладу для видалення: ")
            remove_entry(institutions, key)
        elif choice == "4":
            display_sorted(institutions)
        elif choice == "5":
            sum_school_students(institutions)
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір, спробуйте знову.")

if __name__ == "__main__":
    main()
