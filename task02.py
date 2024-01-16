from collections import deque

def is_palindrome(input_str):
    # Функція для визначення, чи є рядок паліндромом

    # Видаляємо пробіли та переводимо все в нижній регістр
    input_str = input_str.replace(" ", "").lower()

    # Створюємо deque з рядка
    char_deque = deque(input_str)

    while len(char_deque) > 1:
        # Порівнюємо перший та останній символи
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

if __name__ == "__main__":
    try:
        input_str = input("Введіть рядок для перевірки на паліндром: ")
        result = is_palindrome(input_str)

        if result:
            print(f"Рядок '{input_str}' є паліндромом.")
        else:
            print(f"Рядок '{input_str}' не є паліндромом.")

    except KeyboardInterrupt as err:
        print(err)
