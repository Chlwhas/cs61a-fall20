def pow(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y % 2 == 0:
        return pow(x, y // 2) ** 2
    else:
        return x * pow(x, y - 1)

print(pow(2, 32))

