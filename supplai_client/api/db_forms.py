"""
DynamicForm endpoints
"""


class DynamicForm:
    """Class holding contact functions.
    DynamicForm
        Docs: http://localhost:8001/doc/#tag/form
    """
    endpoint_base = 'form'

    def __init__(self, api):
        self._api = api

    def get_forms(self, **kwargs):
        """Get a list of all Forms.

        Args:
            This function takes no arguments.

        Returns:
            dict: All forms.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/dynamic-forms/'
        return self._api.search(endpoint, **kwargs)

    def get_form(self, form_id):
        """Get the full details for a single Form.

        Args:
            form_id (str/uuid): DynamicForm Id.

        Returns:
            dict: Full message details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/dynamic-forms/{form_id}/'
        return self._api.search(endpoint)

    def update_form(self, form_id, data, partial=False):
        """Update a single Form.

        Args:
            form_id (str/uuid): DynamicForm id.
            data (dict): Payload data.
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
        endpoint = f'{self.endpoint_base}/dynamic-forms/{form_id}/'
        return self._api.update(endpoint, data, partial)

    def get_subsections(self, **kwargs):
        """Get a list of all SubSections.

        Args:
            This function takes no arguments.

        Returns:
            dict: All subsections.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/form-subsections/'
        return self._api.search(endpoint, **kwargs)

    def get_subsection(self, subsection_id):
        """Get the full details for a single SubSection.

        Args:
            subsection_id (str/uuid): instance Id.

        Returns:
            dict: Full message details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/form-subsections/{subsection_id}/'
        return self._api.search(endpoint)

    def update_subsection(self, subsection_id, data, partial=False):
        """Update a single SubSection.

        Args:
            subsection_id (str/uuid): instance id.
            data (dict): Payload data.
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
        endpoint = f'{self.endpoint_base}/form-subsections/{subsection_id}/'
        return self._api.update(endpoint, data, partial)

    def get_fields(self, **kwargs):
        """Get a list of all Fields.

        Args:
            This function takes no arguments.

        Returns:
            dict: All fields.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/dynamic-fields/'
        return self._api.search(endpoint, **kwargs)

    def get_field(self, field_id):
        """Get the full details for a single Field.

        Args:
            field_id (str/uuid): DynamicField Id.

        Returns:
            dict: Full message details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/dynamic-fields/{field_id}/'
        return self._api.search(endpoint)

    def update_field(self, field_id, data, partial=False):
        """Update a single Field.

        Args:
            field_id (str/uuid): DynamicField id.
            data (dict): Payload data.
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
        endpoint = f'{self.endpoint_base}/dynamic-fields/{field_id}/'
        return self._api.update(endpoint, data, partial)
