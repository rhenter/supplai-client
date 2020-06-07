"""
Order endpoints
"""


class Order:
    """Class holding order functions.
    Order
        Docs: https://api.supplai.com.br/doc/order/
    """
    endpoint_base = 'order'

    def __init__(self, api):
        self._api = api

    def get_orders(self, **kwargs):
        """Get a list of all Orders.

        Args:
            This function takes no arguments.

        Returns:
            dict: All orders.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/orders/'
        return self._api.search(endpoint, **kwargs)

    def get_order(self, code):
        """Get the full details for a single Order.

        Args:
            code (str): Order Code.

        Returns:
            dict: Full order details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/orders/{code}/'
        return self._api.search(endpoint)
