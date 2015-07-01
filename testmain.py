import testmod
from errorcatch import error_handle_test

def add_one(n):
    pass
    return testmod.div_by_zero(n) + 1

@error_handle_test("Error during fun process")
def main_module():
    print "Hello"
    print "World"
    print add_one(2)
    print "The one above me is an error"
