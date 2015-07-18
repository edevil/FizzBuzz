#!/usr/bin/env python
import sys


class InvalidParamsException(Exception):
    pass


def step1_f(num):
    if not num % 15:
        return 'fizzbuzz'
    elif not num % 5:
        return 'buzz'
    elif not num % 3:
        return 'fizz'
    else:
        return None


def step2_f(num):
    if '3' in str(num):
        return 'lucky'
    else:
        return step1_f(num)


def fizzbuzzer(start, finish, comp_fun=step2_f):
    try:
        i_start = int(start)
        i_finish = int(finish)
    except ValueError:
        raise InvalidParamsException()
    else:
        if i_finish < i_start:
            raise InvalidParamsException()

    elements = []
    for num in range(i_start, i_finish+1):
        computed = comp_fun(num)
        if computed is not None:
            elements.append(computed)
        else:
            elements.append(str(num))
    return ' '.join(elements)


def exit_usage():
    print('Usage:\n./fizzbuzz start finish')
    sys.exit(-1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        exit_usage()

    try:
        print(fizzbuzzer(sys.argv[1], sys.argv[2], step2_f))
    except InvalidParamsException:
        exit_usage()
