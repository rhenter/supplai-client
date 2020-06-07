"""
Condo endpoints
"""


class Condo:
    """Class holding condo functions.
    Condo
        Docs: https://api.supplai.com.br/doc/condo/
    """
    endpoint_base = 'condo'

    def __init__(self, api):
        self._api = api

    def get_condos(self, **kwargs):
        """Get a list of all Condos.

        Args:
            This function takes no arguments.

        Returns:
            dict: All condos.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/condos/'
        return self._api.search(endpoint, **kwargs)

    def get_condo(self, code):
        """Get the full details for a single Condo.

        Args:
            code (str): Condo Code.

        Returns:
            dict: Full condominium details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/condos/{code}/'
        return self._api.search(endpoint)
