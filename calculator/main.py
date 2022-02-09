# -*- coding: utf-8 -*-
class Calc:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b
    
    def div(self, a, b):
        try:
            a / b
        except ZeroDivisionError():
            raise ValueError("You can not divide by 0")