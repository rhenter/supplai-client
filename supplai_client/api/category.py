"""
Category endpoints
"""


class Category:
    """Class holding category functions.
    Category
        Docs: https://api.supplai.com.br/doc/category/
    """
    endpoint_base = 'category'

    def __init__(self, api):
        self._api = api

    def get_categories(self, **kwargs):
        """Get a list of all Condos.

        Args:
            This function takes no arguments.

        Returns:
            dict: All categories.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/categories/'
        return self._api.search(endpoint, **kwargs)

    def create_category(self, data):
        """Update a single Category Text.

        Args:
            data (dict, list of tuples): Data to send in the body of the request.

        Returns:
            dict: Data retrieved for specified endpoint.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/categories/'
        return self._api.create(endpoint, data)

    def get_category(self, code):
        """Get the full details for a single Category.

        Args:
            code (str): Category Code.

        Returns:
            dict: Full category details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/categories/{code}/'
        return self._api.search(endpoint)

    def update_category(self, code, data, partial=False):
        """Update a single Category Text.

        Args:
            code (str): Category Code.
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
        endpoint = f'{self.endpoint_base}/categories/{code}/'
        return self._api.update(endpoint, data, partial)

