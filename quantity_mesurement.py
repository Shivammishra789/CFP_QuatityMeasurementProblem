'''
@author: Shivam Mishra
@date: 29-12-21 12:06 PM
'''
from quantity_custom_execption import QuantityCustomException


class Measurement:
    """
    Takes two parameter length and unit; methods converting length to make in same unit, equals method is being overridden
    """

    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    @staticmethod
    def convert_inch_to_feet_and_compare(length_in_feet, length_in_inch):
        '''
        Making lengths in same unit
        :param length_in_feet: length in feet
        :param length_in_inch: length in inch
        :return: True
        '''
        inch_in_feet = length_in_inch/12
        if length_in_feet == inch_in_feet:
            return True

    @staticmethod
    def convert_yard_to_feet_and_compare(length_in_feet, length_in_yard):
        '''
        Making lengths in same unit
        :param length_in_feet: length in feet
        :param length_in_yard: length in yard
        :return: True
        '''
        yard_in_feet = length_in_yard*3
        if length_in_feet == yard_in_feet:
            return True

    @staticmethod
    def convert_yard_to_inch_and_compare(length_in_inch, length_in_yard):
        '''
        Making lengths in same unit
        :param length_in_inch: length in feet
        :param length_in_yard: length in yard
        :return: True
        '''
        yard_in_inch = length_in_yard*36
        if length_in_inch == yard_in_inch:
            return True

    def __eq__(self, other):

        if self.unit == "feet" and other.unit == "inch":
            return self.convert_inch_to_feet_and_compare(self.length, other.length)
        if self.unit == "inch" and other.unit == "feet":
            return self.convert_inch_to_feet_and_compare(other.length, self.length)
        if self.unit == "feet" and other.unit == "yard":
            return self.convert_yard_to_feet_and_compare(self.length, other.length)
        if self.unit == "yard" and other.unit == "feet":
            return self.convert_yard_to_feet_and_compare(other.length, self.length)
        if self.unit == "inch" and other.unit == "yard":
            return self.convert_yard_to_inch_and_compare(self.length, other.length)
        if self.unit == "yard" and other.unit == "inch":
            return self.convert_yard_to_inch_and_compare(other.length, self.length)
        if self.length == 0.0 and other.length == 0.0:
            return True
        if other.length is None:
            raise QuantityCustomException("Value can't be none")
        if id(self.length) != id(other.length):
            raise QuantityCustomException("Reference are different")
        if isinstance(other.length, float):
            return True
        if self.length == other.length:
            return True
