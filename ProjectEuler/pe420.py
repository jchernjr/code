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
# At each trace of N, we take all the input matrices that yielded squares of one lesser trace (N-1)
# and increase each of the components of those matrices (making "child" matrices) and see what squares we get.
# Some of the squares may have trace greater than N (possibly much greater), but that's ok;
# we'll keep track of them for future use, i.e. (1) in case any of them can be made by squaring
# a different input matrix in the future, we'll know, and (2) to keep track of the input matrices that yielded
# square matrices of each trace.
#
# The key to this approach is that we'll cover everything eventually, without missing any gaps,
# because we always go to "bigger" and "bigger" matrices (higher valued elements),
# and because the trace of their squares never decrease:
# A 2x2 matrix M=(a,b,c,d) has trace(M) = (a^2 + bc) + (bc + d^2), so an increase in any element increases the trace.
#
# We'll keep track of all the squared matrices from this round, so that if we eventually
# find that any of them can be constructed from more than 1 unique input, we'll detect them.
#
# After we utilize the info from trace N-1 to generate the next set of child matrices from it,
# we can delete the info for trace N-1, because everything we generated from it will necessarily
# have a higher trace... nothing will ever come back to "fill in" a lower trace.

# Data structure: keep track of all the square matrices we've found so far, organized by trace.
# I.e. for each trace = k, we'll have a set of matrices with trace(M) = k.
#
# Each matrix M should also remember which inputs made it, so each matrix will be associated with a list.
# 
# Thus, this will be a Dict[trace] --> Dict[Squared Matrix M] --> set of input Matrix/Matrices
def generateOneRound(n, history):
    """Generates square matrices of level n or higher (i.e. trace >= n) by taking
    the input matrices of level n-1, incrementing them to make "child matrices",
    and then squaring each of those to make the new "square matrices".

    The new square matrices may not all be in the same level; in fact, they will probably
    not even be in level n; all we know is that they will be in some higher level than n-1
    because when we increment any element of the input matrix, the trace necessarily increases.

    By the time this round (and all previous rounds) are over, we are guaranteed to have generated
    every square matrix that belongs to level n.
    """
    # Find the input matrices that created outputs at n-1.
    # Increment those matrices' elements, make squares from them, and add to the history.
    lastLevelResults = history[n-1]
    print "Last level results (level " + str(n-1) + "): " + str(lastLevelResults)

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
                history[tr] = defaultdict(set)
            history[tr][m].add(childMatrix)

def initialHistory():
    # Map of trace 0 to the 0-squared matrix and its input.
    zero = (0,0,0,0)
    history = defaultdict(dict)
    history[0] = {zero: set([zero])}
    return history


def countDoubleSquares(n, history):
    """Sees how many matrices at level n (trace = n) are formed by multiple unique squares.
    Should check this after generating matrices for level n, above."""
    count = 0

    thisLevelResults = history[n]
    for (square, inputSet) in thisLevelResults.items():
        if len(inputSet) >= 2:
            count += 1

            print "Matrix " + str(square) + " can be formed by: "
            for inputMatrix in inputSet:
                print "   " + str(inputMatrix) + "^2"

    return count


def searchUpToN(N):
    history = initialHistory()
    for n in xrange(1, N+1):
        generateOneRound(n, history)
        countDoubleSquares(n, history)
        #del history[n-1]

    return history
