
# remember error handling

# try:
# except:
# except Exception as e
#   print(str(e))

# SyntaxError
# ZeroDivisionError
# NameError
# TypeError
# ValueError
# RuntimeError
# OSError
# BaseException

# example
# import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except BaseException as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise


# winter 2018 - Q2 Part B 10 marks
'''
class Light:

    def __init__(self, state=True, wattage=100):

        if not isinstance(state, bool):
            raise TypeError("state is not bool")

        if not isinstance(wattage, (int,float)):
            raise TypeError("wattage is not a form of number")

        if wattage > 300 or wattage < 40:
            raise LightWattageRangeError("wattage has an illegal range value")

        self.__state =state
        self.__wattage =wattage

        self.__all_worked = True

class LightWattageRangeError(Exception):
    pass
'''

# check for exception pass through
# add tutorial for normal try/except


# Light(True, 100)
# Light("a", 100)
# Light(True, 39)


# update code 
import logging
log = logging.getLogger(__name__)

class Light:

    __all_worked = False

    def __init__(self, state=True, wattage=100):

        print("oh no, this won't work!!!")

        if not isinstance(state, bool):
            log.info("state is not bool")
            raise TypeError("state is not bool")

        if not isinstance(wattage, (int, float)):
            log.info("wattage is not a form of number")
            raise TypeError("wattage is not a form of number")

        if wattage > 300 or wattage < 40:
            log.info("wattage has an illegal range value")
            raise LightWattageRangeError("wattage has an illegal range value")

        self.__state = state
        self.__wattage = wattage

        self.__all_worked = True
        log.info("all worked")

    def __eq__(self, other):
        log.info("Am I called? with the __all_worked value of " + str(self.__all_worked))
        return self.__all_worked
    def easy_eq(self,other):
        self.__eq__(other)
        print(other)

class LightWattageRangeError(Exception):
    log.info("wattage has an illegal range value")
    # pass

light0 = Light(True, 190)
light0.easy_eq('hi')



# import unittest

'''
class TestClassMethods(unittest.TestCase):

    def setUp(self):
        # Changing log level to DEBUG
        loglevel = logging.DEBUG
        logging.basicConfig(level=loglevel)

    def test_values(self):
        self.assertTrue(Light(True, 100) == True)
        self.assertFalse(Light(False, 100) == False)

    def test_this_other_values(self):
        self.assertTrue(Light("a", 100) == True)

    def test_other_values(self):
        self.assertTrue(Light(True, 10) == True)


if __name__ == '__main__':
    unittest.main()

'''