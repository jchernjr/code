
# Brute force search for a Pythagorean triplet (a^2 + b^2 = c^2)

def isPythagTriplet(a, b, c):
  return (a*a + b*b == c*c)

def main():
  TARGET_SUM = 1000

  KNOWN_SQUARES = makeSquares(1, TARGET_SUM)
 
  # Check all pairs of integers (a,b) 
  # To avoid checking duplicates (a,b) (b,a), enforce a <= b <= c.
  for a in xrange(1, TARGET_SUM):
    for b in xrange(a, TARGET_SUM):
      # See if this choice of (a,b) leaves enough room for a large enough c.
      c = TARGET_SUM - a - b
      if c < a or c < b:
        continue

      # See if this choice of (a,b) yields a valid hypotenuse c.
      if isPythagTriplet(a, b, c):
        print a, b, c
