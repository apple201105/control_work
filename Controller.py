# Controller (Контроллер) - управляет логикой  связывает модель с представлением
from Model import add,subtract,multiply,divide
from View import get_numbers,show_result, show_message, display_menu


def main():
    while True:
        choice = display_menu()

        if choice == "0":
            show_message("Пока!")
            break
        elif choice in ["1", "2", "3", "4"]:
            a, b = get_numbers()
            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            elif choice == "4":
                result = divide(a, b)
            show_result(result)
        else:
            show_message("Неверный выбор, попробуй снова")
if __name__ == "__main__":
    main()