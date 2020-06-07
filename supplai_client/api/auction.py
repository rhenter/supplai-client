"""
Auction endpoints
"""


class Auction:
    """Class holding auction functions.
    Auction
        Docs: https://api.supplai.com.br/doc/auction/
    """
    endpoint_base = 'auction'

    def __init__(self, api):
        self._api = api

    def get_auctions(self, **kwargs):
        """Get a list of all Auctions.

        Args:
            This function takes no arguments.

        Returns:
            dict: All auctions.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/auctions/'
        return self._api.search(endpoint, **kwargs)

    def create_auction(self, data):
        """Update a single Auction Text.

        Args:
            data (dict, list of tuples): Data to send in the body of the request.

        Returns:
            dict: Data retrieved for specified endpoint.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/auctions/'
        return self._api.create(endpoint, data)

    def get_auction(self, code):
        """Get the full details for a single Auction.

        Args:
            code (str): Auction Code.

        Returns:
            dict: Full auction details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/auctions/{code}/'
        return self._api.search(endpoint)

    def update_auction(self, code, data, partial=False):
        """Update a single Auction Text.

        Args:
            code (str): Auction Code.
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
        endpoint = f'{self.endpoint_base}/auctions/{code}/'
        return self._api.update(endpoint, data, partial)
