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

    def get_auctions(self):
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
        return self._api.search(endpoint)

    def get_auction(self, auction_code):
        """Get the full details for a single Auction.

        Args:
            auction_code (str): Auction Code.

        Returns:
            dict: Full auction details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/auctions/{auction_code}/'
        return self._api.search(endpoint)
