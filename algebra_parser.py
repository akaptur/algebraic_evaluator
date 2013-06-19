# algebra_parser.py
# James Wang and Katherine Ye, 18 Jun 2013

"""Simple algebraic parser (without using eval)"""

class Evaluator(object):
    """algebra-parser.parse:: parse(String)

    Takes a string and returns the evaluated expression as int.
    Uses Shunting-Yard algorithm.
    Example: parse('1+3*2') => 7

    """

    def __init__(self):
        self.operators = {}
        # initialize with default operators
        self.add_operator('-', 1, lambda x, y: x - y)
        self.add_operator('+', 1, lambda x, y: x + y)
        self.add_operator('*', 2, lambda x, y: x * y)
        self.add_operator('/', 2, lambda x, y: x / y)
        self.final_exp = []
        self.operator_stack = []

    def add_operator(self, op_string, precedence, fn):
        assert precedence in [1, 2] # only two options for operator precedence
        self.operators[op_string] = {"precedence" : precedence, "operation" : fn}


    def evaluate(self, exp):
        self.parse_helper(exp)
        return self.final_exp[0]

    def parse_helper(self, post, prior=None):
        if not post:  # base case, end of recursion
            self.final_exp.append(prior)  # out of numbers, put prior into exp
            if self.operator_stack:
                self.operator_stack.reverse()
                for item in self.operator_stack:
                    self.pop_and_eval(item)
        else:  # more to go
            _next = post[0]
            if prior:  # prior is not none
                if not _next in self.operators.keys():  # if is number
                    self.parse_helper(post[1:], prior * 10 + int(_next)) #AK: what is this 10?
                else:  # if it is an operator
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


