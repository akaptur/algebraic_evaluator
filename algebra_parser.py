# algebra_parser.py
# James Wang and Katherine Ye, 18 Jun 2013

import re
"""Simple algebraic parser (without using eval)"""

class Evaluator(object):
    """algebra-parser.parse:: parse(String)

    Takes a string and returns the evaluated expression as int.
    Uses Shunting-Yard algorithm.
    Example: parse('1+3*2') => 7

    """

    LOW_PREC, HIGH_PREC = 1, 2

    def __init__(self):
        self.operators = {}
        # initialize with default operators
        self.add_operator('-', self.LOW_PREC, lambda x, y: x - y)
        self.add_operator('+', self.LOW_PREC, lambda x, y: x + y)
        self.add_operator('*', self.HIGH_PREC, lambda x, y: x * y)
        self.add_operator('/', self.HIGH_PREC, lambda x, y: x / y)
        self.final_exp = []
        self.operator_stack = []

    def add_operator(self, op_string, precedence, fn):
        assert precedence in [self.LOW_PREC, self.HIGH_PREC] # only two options for operator precedence
        self.operators[op_string] = {"precedence" : precedence, "operation" : fn}

    def evaluate(self, exp):
        exp = "".join(exp.split())
        tokens = self.tokenize(exp)
        self.parse_helper(tokens)
        return self.final_exp[0]

    def tokenize(self, exp):
        if not exp:
            return []
        digits_check = re.findall("(^\d+)(.*)", exp)
        if digits_check:
            token, rest = digits_check[0]
            return [token] + self.tokenize(rest)
        if exp[0] in self.operators.keys():
            return [exp[0]] + self.tokenize(exp[1:])
        raise Exception("Invalid character in expression, cannot tokenize")

    def parse_helper(self, post, prior=None):
        if not post:  # base case, end of recursion
            self.final_exp.append(prior)  # out of numbers, put prior into exp
            if self.operator_stack:
                self.operator_stack.reverse()
                for item in self.operator_stack:
                    self.pop_and_eval(item)
        else:  # more to go
            _next = post[0]
            if prior is not None:
                self.final_exp.append(prior)
                while (self.operator_stack and
                       self.operators[self.operator_stack[-1]]["precedence"] >=
                       self.operators[_next]["precedence"]):
                    op = self.operator_stack.pop()
                    self.pop_and_eval(op)
                self.operator_stack.append(_next)
                self.parse_helper(post[1:])
            else:
                self.parse_helper(post[1:], int(_next))

    def pop_and_eval(self, op):
        v2 = self.final_exp.pop()
        v1 = self.final_exp.pop()
        self.final_exp.append(self.operators[op]["operation"](v1, v2))


