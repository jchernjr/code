
# Euler Problem #50:
# Find a prime under 1-million, that is the sum of the most consecutive primes.

def buildSieve(n):
    """Return an array of True/False, where the value at each index says whether that index is a prime,
    for numbers up to, but not including, n."""
    sieve = [True] * n
    sieve[0] = sieve[1] = False # 0 and 1 aren't primes

    # For every number, k, in the range, mark 2k, 3k, 4k, ... as non-primes
    for k in xrange(2, n):
        for i in xrange(2*k, n, k):
            sieve[i] = False

    return sieve


def getPrimesUpTo(n):
    return [i for (i, b) in enumerate(buildSieve(n)) if b]

