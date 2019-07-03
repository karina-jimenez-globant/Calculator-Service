from __future__ import division
from flask import jsonify
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class Calculator(object):

    def __init__(self, number1, number2, function):
        self.number1 = number1
        self.number2 = number2
        self.function = function
        self.result = 0

    def calc_addition(self):
        self.result = self.number1 + self.number2

    def calc_multiplication(self):
        self.result = self.number1 * self.number2

    def calc_division(self):
        r = round(self.number1 / self.number2, 2)
        self.result = r

    def calc_subtraction(self):
        self.result = self.number1 - self.number2

    def call_calc(self):
        f = self.function
        message = dict({})

        if f == "addition":
            self.calc_addition()
        elif f == "subtraction":
            self.calc_subtraction()
        elif f == "multiplication":
            self.calc_multiplication()
        elif f == "division":
            try:
                self.calc_division()
            except ZeroDivisionError, err:
                logging.error("ZeroDivisionError %s", err)
                message["error"] = "Zero division error"
                return message, 500
        message["result"] = self.result
        return message, 200
