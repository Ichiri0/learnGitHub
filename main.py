# this is test branch

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
