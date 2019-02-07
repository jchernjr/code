# Tuples are (Altitude, RPM, inches MP, % pwr, Fuel gph, TAS mph)
data = [
  (2500, 2000, 17, 35, 7, 105),
  (2500, 2000, 18, 39, 7.5, 113),
  (2500, 2000, 19, 43, 8.2, 121),
  (2500, 2000, 20, 47, 8.7, 126),
  (2500, 2200, 20, 55, 10.2, 138),
  (2500, 2200, 21, 59, 10.8, 142),
  (2500, 2200, 22, 63, 11.4, 146),
  (2500, 2200, 23, 67, 12.1, 149),
  (2500, 2300, 20, 59, 11, 142),
  (2500, 2300, 21, 62, 11.5, 145),
  (2500, 2300, 22, 67, 12.2, 149),
  (2500, 2300, 23, 71, 13.1, 154),
  (2500, 2450, 20, 63, 12, 148),
  (2500, 2450, 21, 68, 12.7, 151),
  (2500, 2450, 22, 72, 13.4, 154),
  (2500, 2450, 23, 76, 14.2, 158),
  (5000, 2000, 16, 34, 6.8, 103),
  (5000, 2000, 17, 37, 7.3, 111),
  (5000, 2000, 18, 41, 7.9, 118),
  (5000, 2000, 19, 45, 8.5, 126),
  (5000, 2200, 20, 57, 10.5, 143),
  (5000, 2200, 21, 60, 11, 146),
  (5000, 2200, 22, 64, 11.7, 151),
  (5000, 2200, 23, 68, 12.4, 155),
  (5000, 2300, 20, 60, 11.2, 146),
  (5000, 2300, 21, 64, 11.9, 151),
  (5000, 2300, 22, 69, 12.6, 155),
  (5000, 2300, 23, 73, 13.4, 158),
  (5000, 2450, 20, 65, 12.2, 151),
  (5000, 2450, 21, 70, 13, 156),
  (5000, 2450, 22, 73, 13.6, 159),
  (5000, 2450, 23, 78, 14.5, 163),
  (7500, 2000, 16, 36, 7, 107),
  (7500, 2000, 17, 39, 7.6, 116),
  (7500, 2000, 18, 43, 8.1, 123),
  (7500, 2000, 19, 47, 8.7, 131),
  (7500, 2200, 18, 51, 9.7, 138),
  (7500, 2200, 19, 54, 10.2, 143),
  (7500, 2200, 20, 58, 10.7, 148),
  (7500, 2200, 21, 62, 11.4, 152),
  (7500, 2300, 18, 54, 10.5, 142),
  (7500, 2300, 19, 58, 11, 147),
  (7500, 2300, 20, 62, 11.6, 151),
  (7500, 2300, 21, 66, 12.2, 156),
  (7500, 2450, 18, 58, 11, 147),
  (7500, 2450, 19, 62, 11.7, 152),
  (7500, 2450, 20, 67, 12.4, 157),
  (7500, 2450, 21, 71, 13.1, 161),
  (10000, 2000, 15, 35, 6.9, 105),
  (10000, 2000, 16, 38, 7.4, 114),
  (10000, 2000, 17, 40, 7.8, 120),
  (10000, 2000, 18, 44, 8.4, 128),
  (10000, 2200, 16, 45, 8.7, 129),
  (10000, 2200, 17, 49, 9.3, 136),
  (10000, 2200, 18, 52, 9.8, 142),
  (10000, 2200, 19, 56, 10.4, 148),
  (10000, 2300, 16, 47, 9.2, 134),
  (10000, 2300, 17, 51, 9.8, 141),
  (10000, 2300, 18, 56, 10.5, 147),
  (10000, 2300, 19, 60, 11.1, 152),
  (10000, 2450, 16, 51, 10, 141),
  (10000, 2450, 17, 55, 10.6, 146),
  (10000, 2450, 18, 60, 11.2, 152),
  (10000, 2450, 19, 63, 11.9, 156),
  (15000, 2000, 14, 34, 6.8, 101),
  (15000, 2000, 15, 37, 7.3, 112),
  (15000, 2000, 16, 40, 7.8, 122),
  (15000, 2200, 14, 40, 8, 120),
  (15000, 2200, 15, 44, 8.6, 130),
  (15000, 2200, 16, 47, 9.1, 138),
  (15000, 2300, 14, 42, 8.5, 127),
  (15000, 2300, 15, 47, 9.1, 136),
  (15000, 2300, 16, 50, 9.6, 143),
  (15000, 2450, 14, 46, 9.2, 135),
  (15000, 2450, 15, 50, 9.8, 142),
  (15000, 2450, 16, 54, 10.4, 150),
  (20000, 2200, 12, 35, 7.2, 103),
  (20000, 2200, 13, 39, 7.8, 118),
  (20000, 2300, 12, 38, 7.7, 113),
  (20000, 2300, 13, 42, 8.4, 126),
  (20000, 2450, 12, 40, 8.3, 122),
  (20000, 2450, 13, 44, 9, 133),
]
# Indices into each tuple
ALT = 0
RPM = 1
MP = 2
PCTPWR = 3
GPH = 4
TASMPH = 5


# Two things we want to be able to solve:
# 1. Given altitude and power setting, compute the % pwr, fuel burn, and airspeed
# 2. Given altitude, MP, and desired % pwr, compute the RPM needed to meet that % pwr.
# As an extension to (1), want to also know the maximum MP available at an altitude. 
# 
alt = float(input("Input altitude (feet MSL): "))
rpm = float(input("Input RPM: "))
mp = float(input("Input manifold pressure (inches Hg): "))
print()

# Note: If inputs are too low or too high, we won't find anything to interpolate from.  Notify user.

# Find the data points that bound our criteria in terms of Altitude and RPM.
def findLowerAndUpperBounds(tuples, cmpIndex, cmpValue):
  #loAlt = max([tup[ALT] for tup in data if tup[ALT] <= alt])
  #hiAlt = min([tup[ALT] for tup in data if tup[ALT] >= alt])
  #loAltData = list(filter(lambda tup: tup[ALT] == loAlt, data))
  #hiAltData = list(filter(lambda tup: tup[ALT] == hiAlt, data))
  loVals = [tup[cmpIndex] for tup in tuples if tup[cmpIndex] <= cmpValue]
  hiVals = [tup[cmpIndex] for tup in tuples if tup[cmpIndex] >= cmpValue]
  loVal = max(loVals) if loVals else None
  hiVal = min(hiVals) if hiVals else None
  loData = list(filter(lambda tup: tup[cmpIndex] == loVal, tuples))
  hiData = list(filter(lambda tup: tup[cmpIndex] == hiVal, tuples))
  return loData, hiData

loAltData, hiAltData = findLowerAndUpperBounds(data, ALT, alt)

loAltLoRpm, loAltHiRpm = findLowerAndUpperBounds(loAltData, RPM, rpm)
hiAltLoRpm, hiAltHiRpm = findLowerAndUpperBounds(hiAltData, RPM, rpm)

loAltLoRpmLoMp, loAltLoRpmHiMp = findLowerAndUpperBounds(loAltLoRpm, MP, mp)
loAltHiRpmLoMp, loAltHiRpmHiMp = findLowerAndUpperBounds(loAltHiRpm, MP, mp)
hiAltLoRpmLoMp, hiAltLoRpmHiMp = findLowerAndUpperBounds(hiAltLoRpm, MP, mp)
hiAltHiRpmLoMp, hiAltHiRpmHiMp = findLowerAndUpperBounds(hiAltHiRpm, MP, mp)

# Remove duplicate points
boundingPts = sorted(set(loAltLoRpmLoMp + loAltLoRpmHiMp + loAltHiRpmLoMp + loAltHiRpmHiMp + hiAltLoRpmLoMp + hiAltLoRpmHiMp + hiAltHiRpmLoMp + hiAltHiRpmHiMp))

print ("Found %d points" % len(boundingPts))
for pt in boundingPts:
  print(pt)

# Rename vars for easier use
x0 = loAltData
x1 = hiAltData
x0y0, x0y1 = loAltLoRpm, loAltHiRpm
x1y0, x1y1 = hiAltLoRpm, hiAltHiRpm
x0y0z0, x0y0z1 = loAltLoRpmLoMp, loAltLoRpmHiMp
x0y1z0, x0y1z1 = loAltHiRpmLoMp, loAltHiRpmHiMp
x1y0z0, x1y0z1 = hiAltLoRpmLoMp, hiAltLoRpmHiMp
x1y1z0, x1y1z1 = hiAltHiRpmLoMp, hiAltHiRpmHiMp

# Get fractions in each coordinate
def getFraction(v, v0, v1):
  if v0 == v1:
    return 1.0
  else:
    return float(v-v0) / float(v1-v0)

x0 = loAltData[0][ALT]
x1 = hiAltData[0][ALT]
xf = getFraction(alt, x0, x1)

y0 = loAltLoRpm[0][RPM]
y1 = loAltHiRpm[0][RPM]
yf = getFraction(rpm, y0, y1)

z0 = loAltLoRpmLoMp[0][MP]
z1 = loAltLoRpmHiMp[0][MP]
zf = getFraction(mp, z0, z1)

print("X fraction in ALT is: %.3f" % xf)
print("Y fraction in RPM is: %.3f" % yf)
print("Z fraction in MP  is: %.3f" % zf)
print()

def interp1(f, v0, v1):
  return v0 + f*(v1-v0)

def interp3(cornerPts, xf, yf, zf, dim):
  # Interpolate along the 4 edges of the X direction
  # but this only works inside a cube
  a = interp1(xf, cornerPts[0][dim], cornerPts[4][dim])
  b = interp1(xf, cornerPts[1][dim], cornerPts[5][dim])
  c = interp1(xf, cornerPts[2][dim], cornerPts[6][dim])
  d = interp1(xf, cornerPts[3][dim], cornerPts[7][dim])

  # Then along the Y direction between these two pairs of edges
  e = interp1(yf, a, b)
  f = interp1(yf, c, d)

  # Then along the Z direction between the pair of Y-edges
  g = interp1(zf, e, f)
  return g

print("pct pwr:   %.1f" % interp3(boundingPts, xf, yf, zf, PCTPWR))
print("fuel rate: %.2f" % interp3(boundingPts, xf, yf, zf, GPH))
tasmph = interp3(boundingPts, xf, yf, zf, TASMPH)
print("TAS mph:   %.1f    (%.1f kt)" % (tasmph, tasmph / 1.15))

