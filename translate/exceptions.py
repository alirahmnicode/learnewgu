class BaseError(Exception):
    """
    base error class
    """

    def __init__(self, val, message):
        self.val = val
        self.message = message
        super().__init__()

    def __str__(self):
        return "{} --> {}".format(self.val, self.message)


class LanguageNotSupportedException(BaseError):
    """
    exception thrown if the user uses a language that is not supported by the deep_translator
    """
    
    def __init__(self, val, message="There is no support for the chosen language"):
        super().__init__(val, message)



class TranslationNotFound(BaseError):
    """
    exception thrown if no translation was found for the text provided by the use
    """

    def __init__(self, val, message="No translation was found using the current translator."):
        super().__init__(val, message)


class RequestError(Exception):
    """
    exception thrown if an error occurred during the request call, e.g a connection problem.
    """

    def __init__(self, message="Request exception can happen due to an api connection error. "
        "Please check your connection and try again"):
        self.message = message

    def __str__(self):
        return self.message


class TooManyRequests(Exception):
    """
    exception thrown if an error occurred during the request call, e.g a connection problem.
    """

    def __init__(
        self,
        message="Server Error: You made too many requests to the server. According to google, you are allowed to make 5 requests per second and up to 200k requests per day." 
        "You can wait and try again later or you can try the translate_batch function",):
        self.message = message

    def __str__(self):
        return self.message