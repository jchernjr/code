from collections import defaultdict

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

# We'll start from N = 1 and build upwards.
# At each N, we try to increase the components of all 2x2 matrices M=(a,b,c,d)
# until they would cause the trace of the squared matrices M*M to reach or exceed N.
# We'll keep track of all the squares from this round, so that if any can be
# constructed from more than 1 unique M*M, we'll find them.

def searchNextRound(n, prevFrontier):
    """Searches for the next set of squared matrices with trace < N,
    that have not been found already.

    prevFrontier: the set of input matrices checked in the last round, N-1.
    For the first round, N = 1, this should be a set containing a single 2x2 zero matrix.
    """
    currFrontier = set()


# Data structure: keep track of all the square matrices we've found so far, organized by trace.
# I.e. for each trace = k, we'll have a set of matrices with trace(M) = k.
#
# Each matrix M should also remember which inputs made it, so each matrix will be associated with a list.
# 
# Thus, this will be a Dict[trace] --> Dict[Squared Matrix M] --> List of input Matrix/Matrices
def searchOneRound(n, history):
    # All input matrices are captured in this history for now.
    # Find the input matrices that created outputs at n-1.
    # Increment those matrices' elements, make squares from them, and add to the history.
    lastLevelResults = history[n-1]

    def listExtractor(accum, nextListOfInputs):
        accum.extend(nextListOfInputs)
        return accum

    lastLevelInputs = reduce(listExtractor, lastLevelResults.values(), [])

    for inputMatrix in lastLevelInputs:
        # Increment each element by 1 and see what squared result each one yields.
        a, b, c, d = inputMatrix
        childMatrices = [
            (a+1, b, c, d),
            (a, b+1, c, d),
            (a, b, c+1, d),
            (a, b, c, d+1)]

        for childMatrix in childMatrices:
            m = square(childMatrix)
            tr = trace(m)

            # Then put it in the history (guarantees that every child matrix is captured somewhere)
            if tr not in history:
                history[tr] = defaultdict(list)
            history[tr][m].append(childMatrix)

def initialHistory():
    # Map of trace 0 to the 0-squared matrix and its input.
    zero = (0,0,0,0)
    history = defaultdict(dict)
    history[0] = {zero: [zero]}
    return history


def searchUpToN(n):
    history = initialHistory()
    for i in xrange(1, n+1):
        searchOneRound(i, history)

    return history
