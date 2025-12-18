def bubble_sort(arr, reverse=False):
    """Простая сортировка пузырьком"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if not reverse:
                # По возрастанию
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                # По убыванию
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    print("=== СОРТИРОВКА ПУЗЫРЬКОМ ===")

    # 1. Ввод чисел
    numbers = []
    print("Вводите числа. Для окончания введите 'стоп':")

    while True:
        num = input("Число: ")
        if num == "стоп":
            break
        try:
            numbers.append(float(num))
        except:
            print("Ошибка! Введите число или 'стоп'")

    if not numbers:
        print("Вы не ввели чисел!")
        return

    print(f"Вы ввели: {numbers}")

    # 2. Выбор направления сортировки
    print("\nКак сортировать?")
    print("1 - по возрастанию (от меньшего к большему)")
    print("2 - по убыванию (от большего к меньшему)")

    choice = input("Выберите 1 или 2: ")

    # 3. Сортировка и вывод
    if choice == "1":
        sorted_nums = bubble_sort(numbers.copy(), reverse=False)
        print(f"\nОтсортировано по возрастанию: {sorted_nums}")
    elif choice == "2":
        sorted_nums = bubble_sort(numbers.copy(), reverse=True)
        print(f"\nОтсортировано по убыванию: {sorted_nums}")
    else:
        print("Неправильный выбор! Сортирую по возрастанию.")
        sorted_nums = bubble_sort(numbers.copy(), reverse=False)
        print(f"\nОтсортировано по возрастанию: {sorted_nums}")


if __name__ == "__main__":
    main()
