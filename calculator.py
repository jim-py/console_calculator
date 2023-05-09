inp = input().split()

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
