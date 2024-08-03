import math

def calculate_angles(x, y, z, cosDeltaGamma, sinDeltaGamma, cosDeltaPhi, sinDeltaPhi, k):
    angle1 = math.atan2(y * cosDeltaGamma - k * sinDeltaGamma, x * cosDeltaPhi - z * sinDeltaPhi)
    angle2 = math.asin(k * cosDeltaGamma + y * sinDeltaGamma)
    return [angle1, angle2]
