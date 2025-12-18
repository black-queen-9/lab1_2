def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    numbers = []
    print("Введите числа (для завершения введите 'end'):")
    while True:
        user_input = input()
        if user_input.lower() == 'end':
            break
        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Пожалуйста, введите целое число или 'end' для завершения.")

    bubble_sort(numbers)
    print("Отсортированный список:", numbers)


if __name__ == "__main__":
    main()
