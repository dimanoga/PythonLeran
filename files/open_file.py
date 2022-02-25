import contextlib


@contextlib.contextmanager
def open_file(file, mode):
    f = open(file, mode)
    try:

        yield f
    finally:
        print('close file',file)
        f.close()


result = []
with open('test1.txt', 'r') as file:
    result = file.read().strip().split('\n')

result.reverse()
print(result)
with open('test1.txt','w') as file:
    file.write(result.pop(0))
    for line in result:
        print(line)
        file.write('\n' + line)

