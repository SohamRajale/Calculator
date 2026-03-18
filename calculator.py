import math

# Trigonometry functions

def sin_deg(angle):
    """Calculate sine of an angle given in degrees."""
    return math.sin(math.radians(angle))

def cos_deg(angle):
    """Calculate cosine of an angle given in degrees."""
    return math.cos(math.radians(angle))


def tan_deg(angle):
    """Calculate tangent of an angle given in degrees."""
    return math.tan(math.radians(angle))


def asin_rad(value):
    """Calculate arcsine of a value and return the angle in radians."""
    return math.asin(value)


def acos_rad(value):
    """Calculate arccosine of a value and return the angle in radians."""
    return math.acos(value)


def atan_rad(value):
    """Calculate arctangent of a value and return the angle in radians."""
    return math.atan(value)


def degrees(rad):
    """Convert radians to degrees."""
    return math.degrees(rad)


def radians(deg):
    """Convert degrees to radians."""
    return math.radians(deg)