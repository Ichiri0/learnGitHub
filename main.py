# this is test branch

def func(a, b):
    print('Сейчас сложатся два числа.')
    result = a + b
    return result

# this function reads file
def test(file_dir):
    file = open(file_dir, 'r')
    a = file.read()
    for i in range(len(a)):
        print(a[i])
    file.close()

test("text.txt")

