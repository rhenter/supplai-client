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

    def get_messages(self, **kwargs):
        """Get a list of all Message.

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
        return self._api.search(endpoint, **kwargs)

    def get_message(self, code):
        """Get the full details for a single Message.

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

    def update_message(self, code, data, partial=False):
        """Update a single Message.

        Args:
            code (str): Contact Code.
            data (dict): Payload data.
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
        endpoint = f'{self.endpoint_base}/messages/{code}/'
        return self._api.update(endpoint, data, partial)
