"""
Feat 7. There is the following class for reading information from the input stream:

        
import sys


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines())) # read a list of strings from the input stream
        sd = StreamData()
        res = sd.create(self.FIELDS,
lst_in)
        return sd, res
Which can then be used as follows:

sr = StreamReader()
data, result = sr.readlines()
Before the StreamReader class, it is necessary to declare another StreamData class with a method:

def create(self, fields, lst_values): ...
which would receive as input a tuple FIELDS from the names of local attributes (passed to the fields attribute) and a list of lst_in strings (passed to the lst_values ​​attribute) and would form local properties in an object of the StreamData class with field names from fields and corresponding values ​​from lst_values.

If the creation of local properties is successful,
then the create() method returns True, otherwise it returns False. If the number of fields and the number of rows do not match, then the create() method returns False and there is no need to create local attributes.

P.S. The program only needs to additionally declare the StreamData class. You don't need to do anything else.


Sample Input:

10
Python - the basics of mastery
512
"""

import sys

# здесь объявляется класс StreamData
class StreamData:
    def create(self, fields, lst_values):        
        if len(fields) != len(lst_values):
            return False
        
        for index, value in enumerate(fields):
            setattr(self, value, lst_values[index])
        
        return True

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
