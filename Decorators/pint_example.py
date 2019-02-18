import math
import pint


def set_unit(unit):
    """Register a unit on a function"""
    def decorator_set_unit(func):
        func.unit = unit
        return func
    return decorator_set_unit


@set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius**2 * height


ureg = pint.UnitRegistry()
vol = volume(3, 5) * ureg(volume.unit)
print(volume.unit)
print(vol)
print(vol.to("cubic inches"))
print(vol.to("gallons").m)   # Magnitude
