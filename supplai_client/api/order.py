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

    def get_orders(self):
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
        return self._api.search(endpoint)

    def get_order(self, order_code):
        """Get the full details for a single Order.

        Args:
            order_code (str): Order Code.

        Returns:
            dict: Full order details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/orders/{order_code}/'
        return self._api.search(endpoint)
