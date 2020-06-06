class SupplaiError(Exception):
    """Supplai Error Exception Class"""

    def __init__(self, status_code='', resp_content=''):
        """SupplaiError Exception raised when server returns error.
        Args:
            status_code (str): Status code retrieved from the server.
            resp_content (dict): Response's body with more detailed info about
                                 the problem that has occurred.

        """
        if resp_content:
            message = "Supplai server returned [{}] status code".format(
                status_code)

            if "errorCode" in resp_content:
                message += ", and API returned [{}] error code".format(
                    resp_content["errorCode"])

            if "errorMessage" in resp_content:
                message += ", with message: ({})".format(
                    resp_content["errorMessage"])

        else:
            message = "Supplai server returned a internal server error"

        super().__init__(message)


class EnvironmentNotFound(Exception):
    pass


class AuthError(SupplaiError):
    pass


class NotFound(SupplaiError):
    pass


class ServerError(SupplaiError):
    """ServerError"""
    pass
