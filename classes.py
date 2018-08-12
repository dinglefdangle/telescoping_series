from sympy import Symbol, lambdify
from itertools import combinations
n = Symbol('n')
N = Symbol('N')

class Term():
    def __init__(self, value, color='Green'):
        self.value = value
        self.color = color

    def __str__(self):
        if type(self.value)is float: # when Term is numeric
            return str(round(self.value, 3))
        else: # when Term is symbolic
            return str(self.value)

    def cancel(self, other):
        if self.value == -other.value:
            return True
        else:
            return False

class Sequence():
    def __init__(self, function, s, e, Ns):

        self.expr = function.apart()
        self.exprA = lambdify(n, self.expr.args[0])
        self.exprB = lambdify(n, self.expr.args[1])





    #~ First e-terms
        self.num_sequence = []
        # Build the sequence
        for a in range(s, e + 1):
            self.num_sequence.append(Term(self.exprA(a)))
            self.num_sequence.append(Term(self.exprB(a)))

        # Match cancelling terms
        for tuple in combinations(self.num_sequence, r=2):
            if tuple[0].cancel(tuple[1]):
                tuple[0].color = "Red"
                tuple[1].color = "Red"
        self.num_sequence[-1].color = "Brown" # Last term brown

    #~ N-terms
        self.end_sequence = []
        # Build the sequence
        for i in reversed(range(Ns + 1)):
            self.end_sequence.append(Term(self.exprA(N - i)))
            self.end_sequence.append(Term(self.exprB(N - i)))

        # Match cancelling terms
        for tuple in combinations(self.end_sequence, r=2):
            if tuple[0].cancel(tuple[1]):
                tuple[0].color = "Red"
                tuple[1].color = "Red"
        self.end_sequence[0].color = "Brown" # Last term Brown

    #~ Concatenate sequences

        self.sequence = self.num_sequence + self.end_sequence

    def __str__(self):

        output = []
        for term in self.sequence:
            output.append(str(term) + ' ' + term.color)
        return ', \n'.join(output)



