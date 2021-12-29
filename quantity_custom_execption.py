'''
@author: Shivam Mishra
@date: 29-12-21 12:21 PM
@desc: Custom Quantity Exception
'''


class QuantityCustomException(Exception):

    def __init__(self,message):
        self.message = message

    def __str__(self):
        return self.message
