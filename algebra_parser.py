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
        """ Tokenizes expression into numbers and operators."""
        if not exp:
            return []
        digits_check = re.findall("(^\d+)(.*)", exp)
        if digits_check:
            token, rest = digits_check[0]
            return [int(token)] + self.tokenize(rest)
        if exp[0] in self.operators.keys():
            return [exp[0]] + self.tokenize(exp[1:])
        raise Exception("Invalid character in expression, cannot tokenize")

    def parse_helper(self, post, prior=None):
        print "Parse helper: ", post, prior
        print "operator stack: ", self.operator_stack
        print "final_exp: ", self.final_exp
        if not post:  # base case, end of recursion
            self.final_exp.append(prior)  # out of numbers, put prior into exp
            if self.operator_stack:
                self.operator_stack.reverse()
                for item in self.operator_stack:
                    self.pop_and_eval(item)
        else:  # more to go
            if prior is not None:
                next_op = post[0]
                self.final_exp.append(prior)
                print "just before while: ", self.final_exp
                while (self.operator_stack and
                       self.operators[self.operator_stack[-1]]["precedence"] >=
                       self.operators[next_op]["precedence"]):
                    op = self.operator_stack.pop()
                    self.pop_and_eval(op)
                self.operator_stack.append(next_op)
                self.parse_helper(post[1:])
            else:
                next_num = post[0]
                self.parse_helper(post[1:], next_num)

    def pop_and_eval(self, op):
        v2 = self.final_exp.pop()
        v1 = self.final_exp.pop()
        self.final_exp.append(self.operators[op]["operation"](v1, v2))


