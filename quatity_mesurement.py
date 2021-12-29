'''
@author: Shivam Mishra
@date: 29-12-21 12:06 PM

'''
from quatity_custom_execption import QuatityCustomException


class Measurement:

    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    def __eq__(self, other):

        if self.length == 0.0 and other.length == 0.0:
            return True
        elif other.length is None:
            raise QuatityCustomException("Value can't be none")
        elif id(self.length) != id(other.length):
            raise QuatityCustomException("Reference are different")
        elif isinstance(other.length, float):
            return True
        elif self.length == other.length:
            return True

