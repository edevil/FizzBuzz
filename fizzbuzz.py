#!/usr/bin/env python
import sys


class InvalidParamsException(Exception):
    pass


def fizzbuzzer(start, finish):
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
        if not num % 15:
            elements.append('fizzbuzz')
        elif not num % 5:
            elements.append('buzz')
        elif not num % 3:
            elements.append('fizz')
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
        print(fizzbuzzer(sys.argv[1], sys.argv[2]))
    except InvalidParamsException:
        exit_usage()
