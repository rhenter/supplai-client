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

    def get_faqs(self):
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
        return self._api.search(endpoint)

    def get_faq(self, faq_code):
        """Get the full details for a single Faq.

        Args:
            faq_code (str): Faq Code.

        Returns:
            dict: Full faq details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/faqs/{faq_code}/'
        return self._api.search(endpoint)
