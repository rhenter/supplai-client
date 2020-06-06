"""
Core endpoints
"""


class Core:
    """Class holding core functions.
    Core
        Docs: https://api.supplai.com.br/doc/core/
    """
    endpoint_base = 'core'

    def __init__(self, api):
        self._api = api

    def get_privacy_policies(self):
        """Get a list of all Privacy Policies Texts.

        Args:
            This function takes no arguments.

        Returns:
            dict: All cores.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/privacy-policy/'
        return self._api.search(endpoint)

    def get_privacy_policy(self, code):
        """Get the full details for a single Privacy Policy Text.

        Args:
            code (str): Privacy Policy Code.

        Returns:
            dict: Full privacy policy details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/privacy-policy/{code}/'
        return self._api.search(endpoint)

    def get_terms_of_services(self):
        """Get a list of all Terms of Services.

        Args:
            This function takes no arguments.

        Returns:
            dict: All terms of service texts.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/terms-of-service/'
        return self._api.search(endpoint)

    def get_terms_of_service(self, code):
        """Get the full details for a single Privacy Policy.

        Args:
            code (str): Privacy Policy Code.

        Returns:
            dict: Full terms of service details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/terms-of-service/{code}/'
        return self._api.search(endpoint)
