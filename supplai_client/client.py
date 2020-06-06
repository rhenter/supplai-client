from .api import BaseAPI, Auction, Condo, Core, Contact, Faq, Financial, Order, Supplier, User


class API(BaseAPI):
    """Supplai REST API v1.0 Class

    This class instantiates all endpoint classes

    """

    def __init__(
            self,
            environment="staging",
            access_token=None,
            timeout=3,
            api_port=443,
            locale='pt-br',
    ):
        """APIv20 object to communicate with Supplai REST API.

        Args:
            environment (str, optional): Provides the environment for
                Supplai's API. Defaults to 'practice'.
            access_token (str): Specifies the access token.

        """
        super().__init__(environment, access_token, timeout, api_port=api_port, locale=locale)

        self.auction = Auction(self)
        self.condo = Condo(self)
        self.core = Core(self)
        self.contact = Contact(self)
        self.faq = Faq(self)
        self.financial = Financial(self)
        self.order = Order(self)
        self.supplier = Supplier(self)
        self.user = User(self)
