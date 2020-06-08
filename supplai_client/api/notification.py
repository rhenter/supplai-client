"""
Notification endpoints
"""


class Notification:
    """Class holding notification functions.
    Notification
        Docs: https://api.supplai.com.br/doc/notification/
    """
    endpoint_base = 'notification'

    def __init__(self, api):
        self._api = api

    def get_notifications(self, **kwargs):
        """Get a list of all Condos.

        Args:
            This function takes no arguments.

        Returns:
            dict: All notifications.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/notifications/'
        return self._api.search(endpoint, **kwargs)

    def create_notification(self, data):
        """Update a single Notification Text.

        Args:
            data (dict, list of tuples): Data to send in the body of the request.

        Returns:
            dict: Data retrieved for specified endpoint.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/notifications/'
        return self._api.create(endpoint, data)

    def get_notification(self, code):
        """Get the full details for a single Notification.

        Args:
            code (str): Notification Code.

        Returns:
            dict: Full notification details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/notifications/{code}/'
        return self._api.search(endpoint)

    def update_notification(self, code, data, partial=False):
        """Update a single Notification Text.

        Args:
            code (str): Notification Code.
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
        endpoint = f'{self.endpoint_base}/notifications/{code}/'
        return self._api.update(endpoint, data, partial)

    def get_notification_templates(self, **kwargs):
        """Get a list of all Condos.

        Args:
            This function takes no arguments.

        Returns:
            dict: All Notification Templates.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/notification-templates/'
        return self._api.search(endpoint, **kwargs)

    def create_notification_template(self, data):
        """Update a single Notification Template Text.

        Args:
            data (dict, list of tuples): Data to send in the body of the request.

        Returns:
            dict: Data retrieved for specified endpoint.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/notification-templates/'
        return self._api.create(endpoint, data)

    def get_notification_template(self, code):
        """Get the full details for a single Notification Template.

        Args:
            code (str): Notification Template Code.

        Returns:
            dict: Full notification template details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/notification-templates/{code}/'
        return self._api.search(endpoint)

    def update_notification_template(self, code, data, partial=False):
        """Update a single Notification Template Text.

        Args:
            code (str): Notification Code.
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
        endpoint = f'{self.endpoint_base}/notification-templates/{code}/'
        return self._api.update(endpoint, data, partial)
