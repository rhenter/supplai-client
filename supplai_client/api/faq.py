"""
Faq endpoints
"""


class Faq:
    """Class holding faq functions.
    Faq
        Docs: https://api.supplai.com.br/doc/faq/
    """
    endpoint_base = 'faq'

    def __init__(self, api):
        self._api = api

    def get_faqs(self, **kwargs):
        """Get a list of all Faqs.

        Args:
            This function takes no arguments.

        Returns:
            dict: All faqs.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/faqs/'
        return self._api.search(endpoint, **kwargs)

    def create_faq(self, data):
        """Update a single Faq Text.

        Args:
            data (dict, list of tuples): Data to send in the body of the request.

        Returns:
            dict: Data retrieved for specified endpoint.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/faqs/'
        return self._api.create(endpoint, data)

    def get_faq(self, code):
        """Get the full details for a single Faq.

        Args:
            code (str): Faq Code.

        Returns:
            dict: Full faq details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/faqs/{code}/'
        return self._api.search(endpoint)

    def update_faq(self, code, data, partial=False):
        """Update a single Faq Text.

        Args:
            code (str): Faq Code.
            data (dict, list of tuples): Data to send in the body of the request.
            partial (bool): To specify whether the update will change everything
                            or just a few attributes. Default is False

        Returns:
            dict: Data retrieved for specified endpoint.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/faqs/{code}/'
        return self._api.update(endpoint, data, partial)

