print('Hello, World!')


def func(a, b):
    print('Сейчас сложатся два числа.')
    result = a + b
    return result

def hui():
    a = [i for i in range(0, 10)]
    for j in range(len(a)):
        print(a[j])

hui()

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))


print(func(num1, num2))

