import sympy, itertools
n = sympy.Symbol('n')
N = sympy.Symbol('N')

class Term():
    def __init__(self, value, color='Green'):
        self.value = value
        self.color = color

    def __str__(self):
        if str(type(self.value)) == "<class 'float'>":
            return str(round(self.value, 3)) + '(' + 'color: ' + self.color + ')'
        else:
            return str(self.value) + ' (' + 'color: ' + self.color + ')'

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __eq__(self, other):
        if self.value == -other.value:
            return True
        else:
            return False

class Sequence(Term):
    def __init__(self, function, b, l, nt):

        self.expr = function.apart()
        self.exprA = sympy.lambdify(n, self.expr.args[0])
        self.exprB = sympy.lambdify(n, self.expr.args[1])

        self.sequence = []
        self.endSequence = []

    ## First l-terms

        # Build the sequence
        for a in range(b, l + 1):
            self.sequence.append(Term(self.exprA(a)))
            self.sequence.append(Term(self.exprB(a)))

        # Match cancelling terms
        for tuple in itertools.combinations(self.sequence, r=2):
            if tuple[0] == tuple[1]:
                tuple[0].color = "Red"
                tuple[1].color = "Red"

        # Last term Brown
        for i in range(len(self.sequence)):
            if i == len(self.sequence) - 1:
                self.sequence[i].color = "Brown"

    ## N-terms

        # Build the sequence
        for i in reversed(range(nt)):
            self.endSequence.append(Term(self.exprA(N - i)))
            self.endSequence.append(Term(self.exprB(N - i)))

        # Match cancelling term
        for tuple in itertools.combinations(self.endSequence, r=2):
            if tuple[0] == tuple[1]:
                tuple[0].color = "Red"
                tuple[1].color = "Red"

        # Last term Brown
        for i in reversed((range(len(self.endSequence)))):
            if i == 0:
                self.endSequence[i].color = "Brown"

        # Concatenate sequences
        self.sequence += self.endSequence

    def __str__(self):

        string_values = []
        for term in self.sequence:
            string_values.append(str(term))
        return ', \n'.join(string_values)





