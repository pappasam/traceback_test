import testmod
from config import error_handler

def add_one(n):
    pass
    return testmod.div_by_zero(n) + 1


@error_handler
def main_module():
    print "Hello"
    print "World"
    print add_one(2)
    print "The one above me is an error"
