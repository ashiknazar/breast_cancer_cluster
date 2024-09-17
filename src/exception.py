import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    fname = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error in script name [{0}] line no [{1}] error message [{2}]".format(fname, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)  # Pass the error object (e), not just the message
    
    def __str__(self):
        return self.error_message

