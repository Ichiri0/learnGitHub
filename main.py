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

num1, num2 = 10, 15

print(func(num1, num2))

