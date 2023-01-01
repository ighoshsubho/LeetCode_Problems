# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # take out elements one by one and put it in other list
        # If any operator occurs pop two elements and evaluate
        # After evaluation put it again into list
        # Last element is the result
        ops = {"+" : add, "-" : sub, "*" : mul, "/" : truediv}
        s=[]
        for t in tokens: s.append(int(ops[t](s.pop(-2),s.pop(-1)) if t in ops else t))
        return s[-1]