# this is test branch

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

def func(a, b):
    print('Сейчас сложатся два числа.')
    result = a + b
    return result


# this function reads file
def read_file(file_dir):
    file = open(file_dir, 'r')
    a = file.read()
    for i in range(len(a)):
        print(a[i])
    file.close()

# this function dor write to file anything
def write_file(file_dir, write_text):
    file = open(file_dir, 'w')
    file.write(write_text)
    file.close()


read_file("text.txt")
write_file('text.txt', '\n\nХУЙ)')
read_file('text.txt')
