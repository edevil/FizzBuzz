#!/usr/bin/env python
import sys


class InvalidParamsException(Exception):
    pass


class Step1(object):
    def subst(self, num):
        if not num % 15:
            return 'fizzbuzz'
        elif not num % 5:
            return 'buzz'
        elif not num % 3:
            return 'fizz'
        else:
            return None

    def appendix(self):
        return ''


class Step2(Step1):
    def subst(self, num):
        if '3' in str(num):
            return 'lucky'
        else:
            return super(Step2, self).subst(num)


class Step3(Step2):
    def __init__(self):
        super(Step3, self).__init__()
        self.integers = 0
        self.substs = {}

    def subst(self, num):
        res = super(Step3, self).subst(num)
        if res is not None:
            if res in self.substs:
                self.substs[res] += 1
            else:
                self.substs[res] = 1
        else:
            self.integers += 1
        return res

    def appendix(self):
        apx = ''
        for term in ['fizz', 'buzz', 'fizzbuzz', 'lucky']:
            if term in self.substs:
                num = self.substs[term]
            else:
                num = 0
            apx += '\n{term}: {num}'.format(term=term, num=num)
        apx += '\ninteger: {num_integers}'.format(num_integers=self.integers)
        return apx


def fizzbuzzer(start, finish, transformer_class=Step1):
    transformer = transformer_class()
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
        computed = transformer.subst(num)
        if computed is not None:
            elements.append(computed)
        else:
            elements.append(str(num))
    return ' '.join(elements) + transformer.appendix()


def exit_usage():
    print('Usage:\n./fizzbuzz start finish')
    sys.exit(-1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        exit_usage()

    try:
        print(fizzbuzzer(sys.argv[1], sys.argv[2], Step3))
    except InvalidParamsException:
        exit_usage()
