inp = input().split()

if len(inp) >= 3:
    if inp[0].isnumeric() and inp[2].isnumeric():
        first, second = float(inp[0]), float(inp[2])
        if inp[1] == '+':
            result = first + second
        elif inp[1] == '-':
            result = first - second
        elif inp[1] == '*':
            result = first * second
        elif inp[1] == '/':
            result = first / second
        else:
            result = 0
        print(result)
    else:
        print('Введите числа!')
else:
    print('Некорректный ввод! Введите по шаблону: "2 + 2"')
