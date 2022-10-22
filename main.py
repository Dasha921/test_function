def sum_of_arguments(*args):
    args = list(args)
    result = [str(i) for i in args]
    s = ''.join(result)
    if s.isdigit() == True:
        return sum(args)
    else:
        return "Error: some arguments is not number"


print(sum_of_arguments(1, 2, 3, 4, 5))


def palindrom(st):
    if st[::] == st[::-1]:
        return True
    else:
        return False
print(palindrom("потоп"))




