from dataclasses import dataclass, field
import datetime

@dataclass
class Orders:
    """Orders Class, fields taken from Sales.OrderLines"""
    OrderLineID: int
    OrderID: int
    StockItemID: int
    Description: str
    PackageTypeID: int
    Quantity: int
    UnitPrice: float = field(metatdata={"units":"$"})
    TaxRate: float = field(metadata={"units":"%"})
    PickedQuantity: int
    PickingCompletedWhen: datetime
    LastEditedBy: int
    LastEditedWhen: datetime
    def __gt__(self,other):
        return self.__quantity*self.__UnitPrice*(1+self.__TaxRate/100)>other.__quantity*other.__UnitPrice*(1+other.__TaxRate/100)

    def __ge__(self,other):
        return self.__quantity*self.__UnitPrice*(1+self.__TaxRate/100)>=other.__quantity*other.__UnitPrice*(1+other.__TaxRate/100)

@dataclass
class Invoices:
    """Invoices class, fields taken from Sales.InvoiceLines"""
    InvoiceLineID: int
    InvoiceID: int
    StockItemID: int
    Description: str
    PackageTypeID: int
    Quantity: int
    UnitPrice: float = field(metadata={"units":"$"})
    TaxRate: float = field(metadata={"units":"%"})
    TaxAmount: float = field(metadata={"units":"$"})
    LineProfit: float = field(metadata={"units":"$"})
    ExtendedPrice: float = field(metadata={"units":"$"})
    LastEditedBy: int
    LastEditedWhen: datetime
    def __gt__(self,other):
        self.__ExtendedPrice>other.__ExtendedPrice

    def __ge__(self,other):
        self.__ExtendedPrice>=other.__ExtendedPrice

@dataclass
class Customers:
    """Customers class, fields taken from Sales.Customers"""
    CustomerID: int
    CustomerName: str
    BillToCustomerID: int
    CustomerCategoryID: int
    BuyingGroupID: int
    PrimaryContactPersonID: int
    AlternateContactPersonID: int
    DeliveryMethodID: int
    DeliveryCityID: int
    PostalCityID: int
    CreditLimit: float = field(metadata={"units":"$"})
    AccountOpenedDate: str
    StandardDiscountPercentage: float = field(metadata={"units":"%"})
    IsStatementSent: bool
    IsOnCreditHold: bool
    PaymentDays: int
    PhoneNumber: str
    FaxNumber: str
    DeliveryRun: str
    RunPosition: str
    WebsiteURL: str
    DeliveryAddressLine1: str
    DeliveryAddressLine2: str
    DeliveryPostalCode: str
    DeliveryLocation: str
    PostalAddressLine1: str
    PostalAddressLine2: str
    PostalPostalCode: str
    LastEditedBy: int
    ValidFrom: datetime
    ValidTo: datetime