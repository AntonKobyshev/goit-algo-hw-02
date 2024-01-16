from collections import deque

def is_palindrome(input_str):

    input_str = input_str.replace(" ", "").lower()

    char_deque = deque(input_str)

    while len(char_deque) > 1:
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
