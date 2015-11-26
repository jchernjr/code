import math

# Euler Problem #50:
# Find a prime under 1-million, that is the sum of the most consecutive primes.

def buildSieve(n):
    """Return an array of True/False, where the value at each index says whether that index is a prime,
    for numbers up to, but not including, n."""
    sieve = [True] * n
    sieve[0] = sieve[1] = False # 0 and 1 aren't primes

    # For every number, k, in the range, mark 2k, 3k, 4k, ... as non-primes
    for k in xrange(2, int(math.sqrt(n))):
        for i in xrange(2*k, n, k):
            sieve[i] = False

    return sieve


def getPrimesUpTo(n):
    return [i for (i, b) in enumerate(buildSieve(n)) if b]


def findPrimeSumOfRunLength(primesList, primeSet, runLength):
    """Makes sums of consecutive prime numbers from the `primeslist`,
    by summing exactly `runLength` consecutive numbers, and returns info about
    the first one it finds, in the form (sum, [list of addends]).
    If none was found, returns None.

    Note that `primeSet` must include primes at least as large as the largest sum
    from the `primeList`, or else, there's no way to tell whether those larger sums
    are primes.
    """
    numbers = primesList
    for i in xrange(len(numbers) - runLength + 1):
        thisSlice = numbers[i : i+runLength]
        thisSum = sum(thisSlice)

        if thisSum in primeSet:
            return thisSum, thisSlice
    return None

def findLongestRunLength(primesList, primeSet):
    longestRun = 0
    longestAnswer = (0, [])

    for runLength in xrange(1, len(primesList) + 1):
        answer = findPrimeSumOfRunLength(primesList, primeSet, runLength)
        if answer:
            longestRun = runLength
            longestAnswer = answer
            print "Longest run so far: " + str(longestRun) + \
                " sum=" + str(longestAnswer[0]) + \
                ", starting at " + str(longestAnswer[1][0])

    return longestAnswer


def doProblem():
    N = 1000000
    primesList = getPrimesUpTo(N)
    primeSet = set(primesList)
    findLongestRunLength(primesList, primeSet)


import time
def runtimer(fn, args, nIterations=1):
    start = time.clock()
    for i in xrange(nIterations):
        fn(*args)
    finish = time.clock()
    print "Time=" + str(finish-start) + ", for Iterations=" + str(nIterations)

