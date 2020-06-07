"""
Financial endpoints
"""


class Financial:
    """Class holding payment functions.
    payment
        Docs: https://api.supplai.com.br/doc/payment/
    """
    endpoint_base = 'payment'

    def __init__(self, api):
        self._api = api

    def get_payments(self, **kwargs):
        """Get a list of all payments.

        Args:
            This function takes no arguments.

        Returns:
            dict: All payments.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/payments/'
        return self._api.search(endpoint, **kwargs)

    def get_payment(self, code):
        """Get the full details for a single Financial.

        Args:
            code (str): Financial Code.

        Returns:
            dict: Full payment details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/payments/{code}/'
        return self._api.search(endpoint)
