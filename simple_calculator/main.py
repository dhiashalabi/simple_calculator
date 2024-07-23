# -*- coding: utf-8 -*-

import operator
from functools import reduce


class SimpleCalculator:
    def add(self, *args):
        return reduce(operator.add, args)

    def sub(self, *args):
        return reduce(operator.sub, args)

    def mul(self, *args):
        if not all(args):
            raise ValueError()
        return reduce(operator.mul, args)

    def div(self, a, b):
        if b == 0:
            return float("inf")
        return a / b

    def avg(self, it, lt=None, ut=None):
        count = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            count += 1
            total += number

        if count == 0:
            return 0

        return total / count
