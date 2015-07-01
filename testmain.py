import testmod
from errorcatch import pager_duty_test

def add_one(n):
    pass
    return testmod.div_by_zero(n) + 1

@pager_duty_test("Error during fun process")
def main_module():
    print "Hello"
    print "World"
    print add_one(2)
    print "The one above me is an error"
