import os

def error_message_detail(error, error_detail):
    # Extracts the traceback details from the exception
    _, _, exc_tb = error_detail.exc_info()
    # Retrieves the filename from where the exception occurred
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    # Formats the error message with the filename, line number, and error message
    error_message = "Error occurred in script [{0}], line number [{1}], error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        # Initializes the base Exception class with the error message
        super().__init__(error_message)
        # Creates a detailed error message using the error_message_detail function
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        # Returns the detailed error message when the exception is printed
        return self.error_message
