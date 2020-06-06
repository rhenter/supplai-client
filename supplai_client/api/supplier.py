"""
Supplier endpoints
"""


class Supplier:
    """Class holding supplier functions.
    Supplier
        Docs: https://api.supplai.com.br/doc/supplier/
    """
    endpoint_base = 'supplier'

    def __init__(self, api):
        self._api = api

    def get_suppliers(self):
        """Get a list of all Suppliers.

        Args:
            This function takes no arguments.

        Returns:
            dict: All suppliers.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/suppliers/'
        return self._api.search(endpoint)

    def get_supplier(self, code):
        """Get the full details for a single Supplier.

        Args:
            code (str): Supplier Code.

        Returns:
            dict: Full supplier details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/suppliers/{code}/'
        return self._api.search(endpoint)

    def get_supplier_documents(self, supplier_code):
        """Get a list of all Documents of a Supplier.

        Args:
            This function takes no arguments.

        Returns:
            dict: All Documents of a Supplier.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.
        """

        endpoint = f'{self.endpoint_base}/suppliers-documents/?supplier__code={supplier_code}'
        return self._api.search(endpoint)

    def get_supplier(self, supplier_document_code):
        """Get the full details for a single Supplier.

        Args:
            supplier_document_code (str): Supplier document Code.

        Returns:
            dict: Full supplier document details.

        Raises:
            RequestException: An error thrown by Requests library.
            ValueError: An error thrown by json parser, if JSON decoding fails.
            SupplaiError: An error occurred while requesting the Supplai API.

        """
        endpoint = f'{self.endpoint_base}/suppliers-documents/{supplier_document_code}/'
        return self._api.search(endpoint)
