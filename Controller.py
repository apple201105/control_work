# Controller (Контроллер) - управляет логикой  связывает модель с представлением
from Model import add,subtract,multiply,divide
from View import get_numbers,show_result, show_message, display_menu


def main():
    while True:
        choice = display_menu()

        if choice == "0":
            show_message("Пока!")
            break
        elif choice in ["+", "-", "*", "/"]:
            a, b = get_numbers()
            if choice == "+":
                result = add(a, b)
            elif choice == "-":
                result = subtract(a, b)
            elif choice == "*":
                result = multiply(a, b)
            elif choice == "/":
                result = divide(a, b)
            show_result(result)
        else:
            show_message("Неверный выбор, попробуй снова")
if __name__ == "__main__":
    main()
