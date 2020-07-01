from .api import Auction, BaseAPI, Category, Condo, Contact, Core, DynamicForm, Faq, Financial, Notification, Order, Supplier, User


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
        self.category = Category(self)
        self.condo = Condo(self)
        self.core = Core(self)
        self.contact = Contact(self)
        self.db_forms = DynamicForm(self)
        self.faq = Faq(self)
        self.financial = Financial(self)
        self.notification = Notification(self)
        self.order = Order(self)
        self.supplier = Supplier(self)
        self.user = User(self)
