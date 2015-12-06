from collections import defaultdict
from math import sqrt

# Project Euler #420
# Find F(N), defined as
# the number of positive-integer matrices whose trace (diagonal sum) is less than N
# and can also be expressed as the square of two (or more?) different positive-integer matrices.

# In this problem, we'll just use a tuple (a, b, c, d) to represent a 2x2 matrix
# [ a  b ]
# [ c  d ]
#
# Multiplication and trace operations will accept this type of tuple.

def square(m):
    """Squares a 2x2 matrix."""
    a, b, c, d = m
    return (a*a + b*c, a*b + b*d, a*c + c*d, b*c + d*d)

def trace(m):
    """Return the trace of a 2x2 matrix, that is, the sum of its diagonal elements."""
    a, b, c, d = m
    return a + d

class squaresUpTo(object):
    """Generator that yields squares from 1 up to, and including, an upper limit."""
    def __init__(self, max_val):
        self.max_val = max_val
        self.i = 1 # next number to be squared

    def __iter__(self):
        return self

    def next(self):
        val = self.i * self.i
        if val <= self.max_val:
            self.i += 1
            return val
        else:
            raise StopIteration()


class factorPairs(object):
    """Generator that yields all non-repeating factor pairs for the given integer,
    i.e. if there is a factorization (a, b) where a*b=n, it will not also emit (b, a)."""
    def __init__(self, integer):
        self.integer = integer
        self.curr_factor = 1
        self.max_factor = int(sqrt(integer))

    def __iter__(self):
        return self

    def next(self):
        while self.curr_factor <= self.max_factor:
            foundNextPair = self.integer % self.curr_factor == 0
            self.curr_factor += 1
            if foundNextPair:
                return (self.curr_factor, self.integer / self.curr_factor)

        raise StopIteration()


def generateSquaredMatricesWithTrace(tr):
    """Generates all squared matrices (made by squaring a positive-integer matrix)
    that have the exact trace specified.

    Uses the fact that trace((a b; c d)^2) = a^2 + 2bc + d^2 to find all these matrices
    without requiring additional inputs, as would be required by a recursive approach.

    Returns them in the format: {squaredMatrix: [list of input matrices]}
    """
    results = defaultdict(list)
    # Strategy:
    # a^2 and d^2 terms must be perfect square integers, so loop over those first.
    #
    # 2bc is leftover after subtracting a^2 and d^2 from the required trace.
    # 2bc must be even; otherwise, this choice of (a, d) does not yield an integer matrix.
    # Finally, find all ways to factor bc into pairs of integer factors, and construct
    # input matrices from (a, b, c, d).
    #
    # Finally, remember that all values (a, b, c, d) must be positive, so we still require:
    # a^2 + d^2 < tr, so that 2bc > 0.
    for aSqr in squaresUpTo(tr - 3): # leaves at least 1 for dSqr, and 2 for 2bc
        for dSqr in squaresUpTo(tr - aSqr - 2): # leaves at least 2 for 2bc
            two_bc = tr - aSqr - dSqr
            if two_bc % 2 == 0:
                a, d = int(sqrt(aSqr)), int(sqrt(dSqr))
                bc = two_bc / 2

                for (b, c) in factorPairs(bc):
                    if b == c:
                        inputMatrices = [(a, b, c, d)]
                    else:
                        inputMatrices = [(a, b, c, d), (a, c, b, d)] # reverse b,c if unique

                    for inputMatrix in inputMatrices:
                        results[square(inputMatrix)].append(inputMatrix)

    return results


def countDoubleSquares(matrixMap):
    """Sees how many matrices in the given map of {squaredMatrix: [inputs]}
    have two or more inputs.
    """
    count = 0

    # Loop way, to print out results
    for (square, inputs) in matrixMap.items():
        if len(inputs) >= 2:
            count += 1

            print "Matrix " + str(square) + " can be formed by: "
            for inputMatrix in inputs:
                print "   " + str(inputMatrix) + "^2"

    return count


def searchUpToN(N):
    count = 0
    for n in xrange(N):
        matrixMap = generateSquaredMatricesWithTrace(n)
        count += countDoubleSquares(matrixMap)
        print "Done with trace " + str(n)

    print "Found " + str(count)
