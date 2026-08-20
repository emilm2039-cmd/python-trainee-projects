# day_01_greeting.py
# День 1: базовое взаимодействие с пользователем

def get_age():
    while True:
        try:
            birth_year_str = input("В каком году ты родился? ")
            birth_year = int(birth_year_str)
            current_year = 2024
            age = current_year - birth_year

            if age < 0 or age > 120:
                print("Кажется, тут ошибка: возраст должен быть от 0 до 120 лет. Попробуй ещё раз.")
                continue

            return age
        except ValueError:
            print("Пожалуйста, введи корректный год (числами).")

def main():
    name = input("Как тебя зовут? ")
    age = get_age()

    print(f"Привет, {name}! Тебе {age} лет.")

if __name__ == "__main__":
    main()
