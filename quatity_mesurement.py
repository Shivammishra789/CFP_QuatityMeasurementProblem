'''
@author: Shivam Mishra
@date: 29-12-21 12:06 PM
'''
from quatity_custom_execption import QuatityCustomException


class Measurement:
    """
    Takes two parameter length and unit, equals method is been overrided
    """

    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    def __eq__(self, other):

        if self.unit == "feet" and other.unit == "inch":
            other.length = other.length/12      # making units same to feet
            if self.length == other.length:
                return True
        elif self.unit == "inch" and other.unit == "feet":
            self.length = self.length*12        # making units same to feet
            if self.length == other.length:
                return True
        elif self.length == 0.0 and other.length == 0.0:
            return True
        elif other.length is None:
            raise QuatityCustomException("Value can't be none")
        elif id(self.length) != id(other.length):
            raise QuatityCustomException("Reference are different")
        elif isinstance(other.length, float):
            return True
        elif self.length == other.length:
            return True

