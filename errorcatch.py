import sys
import traceback

class pager_duty_test(object):

    def __init__(self, begin_message, depth=1):
        self.depth = depth
        self.begin_message = begin_message

    def _print_header(self, header):
        line = "-" * 79
        print line
        print header
        print line

    def __call__(self, f):
        def inner(*args, **kwargs):
            try:
                f(*args, **kwargs)
            except:
                exc_type, exc_value, exc_tb = sys.exc_info()
                list_of_traceback_tuples = traceback.extract_tb(exc_tb)

                self._print_header( "Full Traceback list of tuples")
                print list_of_traceback_tuples

                self._print_header("Formatted error position")
                relevant_info = list_of_traceback_tuples[self.depth]
                print relevant_info

                self._print_header("Possible formatted message")

                error_template = "File '{0}', line {1}, function '{2}', call '{3}'"
                error_position_format = error_template.format(*relevant_info)
                
                error_final_list = traceback.format_exception_only(
                        exc_type, 
                        exc_value
                        )
                error_final = ''.join(error_final_list).replace('\n', '')

                final_msg = "{0}: {1}. Error Type -> {2}"
                print final_msg.format(
                        self.begin_message,
                        error_position_format,
                        error_final
                        ) 
                self._print_header("Now raising actual error")
                raise
        return inner
