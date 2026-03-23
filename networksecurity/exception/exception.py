import sys


class NetworkSecurityException(Exception):

    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)

        _, _, exc_tb = error_details.exc_info()

        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.line_number = exc_tb.tb_lineno
        self.error_message = error_message

    def __str__(self):
        return (
            f"Error occurred in script [{self.file_name}] "
            f"line [{self.line_number}] "
            f"message [{self.error_message}]"
        )