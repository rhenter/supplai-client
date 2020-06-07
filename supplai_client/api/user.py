"""
User endpoints
"""


class User:
    """Class holding user functions.
    User
        Docs: https://api.supplai.com.br/doc/user/
    """
    endpoint_base = 'user'

    def __init__(self, api):
        self._api = api

    def get_users(self, **kwargs):
        """Get a list of all Accounts authorized for the provided token.

        Args:
            This function takes no arguments.

        Returns:
            dict: All users.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/users/'
        return self._api.search(endpoint, **kwargs)

    def get_user(self, user_id):
        """Get the full details for a single User.

        Args:
            user_id (str): User ID.

        Returns:
            dict: Full user details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/users/{user_id}'
        return self._api.search(endpoint)
