'''
@author: Shivam Mishra
@date: 29-12-21 12:06 PM
'''
from quantity_custom_execption import QuantityCustomException


class Measurement:
    """
    Takes two parameter length and unit, equals method is been overrided
    """

    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    def __eq__(self, other):

        if self.unit == "feet" and other.unit == "inch":
            other.length = other.length/12      # making units same
            if self.length == other.length:
                return True
        elif self.unit == "inch" and other.unit == "feet":
            self.length = self.length/12      # making units same to feet
            if self.length == other.length:
                return True
        elif self.unit == "feet" and other.unit == "yard":
            other.length = other.length*3      # making units same to feet
            if self.length == other.length:
                return True
        elif self.unit == "yard" and other.unit == "feet":
            self.length = self.length*3       # making units same to feet
            if self.length == other.length:
                return True
        elif self.unit == "inch" and other.unit == "yard":
            other.length = other.length*36       # making units same to inch
            if self.length == other.length:
                return True
        elif self.unit == "yard" and other.unit == "inch":
            self.length = self.length*36       # making units same to inch
            if self.length == other.length:
                return True
        elif self.length == 0.0 and other.length == 0.0:
            return True
        elif other.length is None:
            raise QuantityCustomException("Value can't be none")
        elif id(self.length) != id(other.length):
            raise QuantityCustomException("Reference are different")
        elif isinstance(other.length, float):
            return True
        elif self.length == other.length:
            return True

