def test_sum_two():
    # Тест 1: правильные аргументы
    result = sum_two(1, 2)
    print(result)  # Ожидаем 3

    # Тест 2: неправильный аргумент (float вместо int)
    try:
        sum_two(1, 2.4)
    except TypeError:
        print("Test 2 passed: TypeError was raised")
    else:
        print("Test 2 failed: TypeError was not raised")

    # Тест 3: недостаточно аргументов
    try:
        sum_two(1)
    except TypeError:
        print("Test 3 passed: TypeError was raised")
    else:
        print("Test 3 failed: TypeError was not raised")

    # Тест 4: больше аргументов чем ожидалось
    try:
        sum_two(1, 2, 3)
    except TypeError:
        print("Test 4 passed: TypeError was raised")
    else:
        print("Test 4 failed: TypeError was not raised")

# Запуск тестов
test_sum_two()