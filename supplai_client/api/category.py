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

    def get_categories(self):
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
        return self._api.search(endpoint)

    def get_category(self, id):
        """Get the full details for a single Category.

        Args:
            id (uuid): Category Id.

        Returns:
            dict: Full category details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/categories/{id}/'
        return self._api.search(endpoint)
