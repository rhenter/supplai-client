import json

import requests
from requests.exceptions import Timeout, ReadTimeout, ConnectionError as RequestsConnectionError

from ..exceptions import EnvironmentNotFound, ServerError
from ..validators import validate_status_code
from ..factories import ResponseFactory


class RequestsTransport:
    def __init__(self, headers):
        self.session = requests.Session()
        self.session.headers.update(headers)

    def make_request(self, method_name, endpoint, **kwargs):
        method = getattr(self.session, method_name.lower())
        return method(endpoint, **kwargs)


class BaseAPI:
    """
    BaseAPI Abstract object.
    Attributes:
        url_bases: URLs from Supplai environments
        api_version: Supplai's API base Version
        timeout: Request timeout
        token: Supplai's API Access token
        transport: Transport class to able to use Requests or AioHTTP(AsyncIO)
    """
    api_version = 'v1'

    base_urls = {
        'production': 'https://api.supplai.com.br',
        'staging': 'https://api.staging.supplai.com.br',
        'localhost': 'http://localhost',
    }
    locale = 'pt-br'

    def __init__(
            self,
            environment,
            access_token,
            timeout=3,
            **kwargs):
        """
        Args:
            environment (str): Provides the environment for Supplai's API.
            access_token (str): Specifies the access token.
            optional_api_port (int): Set the base_url port. Default is 443 (HTTPS)
            locale (str): Set the locale language. Default is pt-br
            timeout (int): Set the request timeout. Default is 3
        """
        self.access_token = access_token
        self.environment = environment

        api_port = kwargs.get('api_port', 443)
        locale = kwargs.get('locale', self.locale)
        headers = self.get_default_headers(accept_language=locale)

        self.base_url = self._get_base_url(environment, api_port)
        self.transport = RequestsTransport(headers=headers)
        self.timeout = timeout

    def _get_base_url(self, environment, api_port):
        """
        Get URL BASE of Supplai's API
        Args:
            environment (str):
            api_port (int):
        Returns:
             supplai's API URL
        """
        base_url = self.base_urls.get(environment)
        if api_port != 443:
            base_url = f'{base_url}:{api_port}'

        if not base_url:
            raise EnvironmentNotFound(
                "Environment '{0}' does not exist!".format(environment))
        return f"{base_url}/{self.api_version}"

    def get_default_headers(self, access_token_type='Token', accept_language="pt-br"):
        """Get the required headers to access the API
        Optional:
            access_token_type (str): Specifies the access_token_type to be used on the request. E.g: Token or Bearer
            accept_language: Specifies the Accept-Language to be receive the response i18n.
        Returns:
             dict: Authorization and Content Type
        """
        return {
            'Authorization': f'{access_token_type} {self.access_token}',
            'Content-Type': 'application/json',
            "Accept-Language": accept_language
        }

    def make_request(self, method_name, endpoint, **kwargs):
        """Requests data from Supplai API.
        Args:
            endpoint (str): URL for Supplai API endpoint.
            method_name (str): Specifies the method to be used on the request.
        Optional:
            params (dict, optional): Specifies parameters to be sent with the
            request.

        Returns:
            response: Requests response object.
        """

        full_url = f"{self.base_url}/{endpoint}"
        try:
            response = self.transport.make_request(
                method_name, full_url, timeout=self.timeout, **kwargs
            )
        except (Timeout, ReadTimeout, RequestsConnectionError) as exc:
            raise ServerError() from exc

        is_valid, exception_class = validate_status_code(
            response.status_code, response.json()
        )
        if not is_valid:
            raise exception_class

        return response

    def create(self, endpoint, data):
        """Do a POST without need to pass all arguments to make a request
        Args:
            endpoint (str): URL for Supplai API endpoint.
            data (dict, list of tuples): Data to send in the body of the request.

        Returns:
            dict: Data retrieved for specified endpoint.
        """
        response = self.make_request('POST', endpoint, data=json.dumps(data))
        return ResponseFactory(response, endpoint)

    def update(self, endpoint, data, partial=False):
        """Do a update (PUT/PATCH) without need to pass all arguments to make a request
        Args:
            endpoint (str): URL for Supplai API endpoint.
            data (dict, list of tuples): Data to send in the body of the request.
            partial (bool): To specify whether the update will change everything
                            or just a few attributes. Default is False

        Returns:
            dict: Data retrieved for specified endpoint.
        """
        method = 'PATCH' if partial else 'PUT'
        response = self.make_request(method, endpoint, data=json.dumps(data))
        return ResponseFactory(response, endpoint)

    def search(self, endpoint, **kwargs):
        """Do a GET to make a search without need
           to pass all arguments to make a request.
        Args:
            endpoint (str): URL for Supplai API endpoint.
        Kwargs(Optional):
            params (dict): Specifies parameters to be sent with the request.

        Returns:
            dict: Data retrieved for specified endpoint.
        """
        params = kwargs.pop('params', {})
        response = self.make_request('GET', endpoint, params=params)
        return ResponseFactory(response, endpoint)

    class Meta:
        abstract = True
