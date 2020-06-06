"""
Contact endpoints
"""


class Contact:
    """Class holding contact functions.
    Contact
        Docs: https://api.supplai.com.br/doc/contact/
    """
    endpoint_base = 'contact'

    def __init__(self, api):
        self._api = api

    def get_messages(self):
        """Get a list of all Contacts.

        Args:
            This function takes no arguments.

        Returns:
            dict: All messages.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/messages/'
        return self._api.search(endpoint)

    def get_message(self, code):
        """Get the full details for a single Contact.

        Args:
            code (str): Contact Code.

        Returns:
            dict: Full message details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/messages/{code}/'
        return self._api.search(endpoint)
