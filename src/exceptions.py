import os  # Importing os module for file path manipulations

def error_message_func(error, error_details):  # Function to format the error message
    _, _, exc_tb = error_details.exc_info()  # Extract traceback information
    filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)[0]  # Get the filename
    error_message = "Error occurred at [{0}] on line [{1}] and error message is [{2}]".format(
        filename, exc_tb.tb_lineno, str(error)  # Format the error message with details
    )

    return error_message  # Return the formatted error message

class customExceptions(Exception):  # Custom exception class inheriting from Exception
    def __init__(self, error_message, error_details):  # Constructor to initialize error message and details
        super().__init__(self, error_message)  # Call the parent constructor
        self.error_message = error_message_func(error=error_message, error_details=error_details)  # Set formatted error message

    def __str__(self):  # String representation of the exception
        return self.error_message  # Return the formatted error message

# Testing customException class
# import sys  # Uncomment to import sys for traceback details
# try:
#     a = 5/0  # Example operation that will raise an exception
#     print(a)  # This line won't execute due to the exception

# except Exception as e:  # Catching any exception
#     print(customExceptions(str(e), sys))  # Print custom exception with error details
        
# print('Hello World!')  # Example output to demonstrate continuation of code
