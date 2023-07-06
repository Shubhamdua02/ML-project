import sys
# import logging
from src.logger import logging

def error_message_detail(error, error_detail:sys):

    exc_type, exc_value, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = "Error occurred in file [{0}], line number [{1}] with an Error Message [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message


class customException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        """
        The error_message argument passed in the function below is the error messsage we get from the Exception class.
        Using the super() function, we get the original error message
        """
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
# if __name__ == "__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise customException(e, sys)