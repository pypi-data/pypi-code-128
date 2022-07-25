# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Ptsv2paymentsidrefundsOrderInformationLineItems(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'product_code': 'str',
        'product_name': 'str',
        'product_sku': 'str',
        'quantity': 'int',
        'unit_price': 'str',
        'unit_of_measure': 'str',
        'total_amount': 'str',
        'tax_amount': 'str',
        'tax_rate': 'str',
        'tax_applied_after_discount': 'str',
        'tax_status_indicator': 'str',
        'tax_type_code': 'str',
        'amount_includes_tax': 'bool',
        'type_of_supply': 'str',
        'commodity_code': 'str',
        'discount_amount': 'str',
        'discount_applied': 'bool',
        'discount_rate': 'str',
        'invoice_number': 'str',
        'tax_details': 'list[Ptsv2paymentsOrderInformationAmountDetailsTaxDetails]'
    }

    attribute_map = {
        'product_code': 'productCode',
        'product_name': 'productName',
        'product_sku': 'productSku',
        'quantity': 'quantity',
        'unit_price': 'unitPrice',
        'unit_of_measure': 'unitOfMeasure',
        'total_amount': 'totalAmount',
        'tax_amount': 'taxAmount',
        'tax_rate': 'taxRate',
        'tax_applied_after_discount': 'taxAppliedAfterDiscount',
        'tax_status_indicator': 'taxStatusIndicator',
        'tax_type_code': 'taxTypeCode',
        'amount_includes_tax': 'amountIncludesTax',
        'type_of_supply': 'typeOfSupply',
        'commodity_code': 'commodityCode',
        'discount_amount': 'discountAmount',
        'discount_applied': 'discountApplied',
        'discount_rate': 'discountRate',
        'invoice_number': 'invoiceNumber',
        'tax_details': 'taxDetails'
    }

    def __init__(self, product_code=None, product_name=None, product_sku=None, quantity=None, unit_price=None, unit_of_measure=None, total_amount=None, tax_amount=None, tax_rate=None, tax_applied_after_discount=None, tax_status_indicator=None, tax_type_code=None, amount_includes_tax=None, type_of_supply=None, commodity_code=None, discount_amount=None, discount_applied=None, discount_rate=None, invoice_number=None, tax_details=None):
        """
        Ptsv2paymentsidrefundsOrderInformationLineItems - a model defined in Swagger
        """

        self._product_code = None
        self._product_name = None
        self._product_sku = None
        self._quantity = None
        self._unit_price = None
        self._unit_of_measure = None
        self._total_amount = None
        self._tax_amount = None
        self._tax_rate = None
        self._tax_applied_after_discount = None
        self._tax_status_indicator = None
        self._tax_type_code = None
        self._amount_includes_tax = None
        self._type_of_supply = None
        self._commodity_code = None
        self._discount_amount = None
        self._discount_applied = None
        self._discount_rate = None
        self._invoice_number = None
        self._tax_details = None

        if product_code is not None:
          self.product_code = product_code
        if product_name is not None:
          self.product_name = product_name
        if product_sku is not None:
          self.product_sku = product_sku
        if quantity is not None:
          self.quantity = quantity
        if unit_price is not None:
          self.unit_price = unit_price
        if unit_of_measure is not None:
          self.unit_of_measure = unit_of_measure
        if total_amount is not None:
          self.total_amount = total_amount
        if tax_amount is not None:
          self.tax_amount = tax_amount
        if tax_rate is not None:
          self.tax_rate = tax_rate
        if tax_applied_after_discount is not None:
          self.tax_applied_after_discount = tax_applied_after_discount
        if tax_status_indicator is not None:
          self.tax_status_indicator = tax_status_indicator
        if tax_type_code is not None:
          self.tax_type_code = tax_type_code
        if amount_includes_tax is not None:
          self.amount_includes_tax = amount_includes_tax
        if type_of_supply is not None:
          self.type_of_supply = type_of_supply
        if commodity_code is not None:
          self.commodity_code = commodity_code
        if discount_amount is not None:
          self.discount_amount = discount_amount
        if discount_applied is not None:
          self.discount_applied = discount_applied
        if discount_rate is not None:
          self.discount_rate = discount_rate
        if invoice_number is not None:
          self.invoice_number = invoice_number
        if tax_details is not None:
          self.tax_details = tax_details

    @property
    def product_code(self):
        """
        Gets the product_code of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Type of product. The value for this field is used to identify the product category (electronic, handling, physical, service, or shipping). The default value is `default`.  If you are performing an authorization transaction (`processingOptions.capture` is set to `false`), and you set this field to a value other than `default` or one of the values related to shipping and/or handling, then `orderInformation.lineItems[].quantity`, `orderInformation.lineItems[].productName`, and `orderInformation.lineItems[].productSku` fields are required.  Optional field.  For details, see the `product_code` field description in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/).  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes.  To use the tax calculation service, use values listed in the Tax Product Code Guide. For information about this document, contact customer support. See \"Product Codes,\" page 14, for more information. 

        :return: The product_code of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """
        Sets the product_code of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Type of product. The value for this field is used to identify the product category (electronic, handling, physical, service, or shipping). The default value is `default`.  If you are performing an authorization transaction (`processingOptions.capture` is set to `false`), and you set this field to a value other than `default` or one of the values related to shipping and/or handling, then `orderInformation.lineItems[].quantity`, `orderInformation.lineItems[].productName`, and `orderInformation.lineItems[].productSku` fields are required.  Optional field.  For details, see the `product_code` field description in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/).  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes.  To use the tax calculation service, use values listed in the Tax Product Code Guide. For information about this document, contact customer support. See \"Product Codes,\" page 14, for more information. 

        :param product_code: The product_code of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._product_code = product_code

    @property
    def product_name(self):
        """
        Gets the product_name of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        For an authorization or capture transaction (`processingOptions.capture` is `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the other values that are related to shipping and/or handling.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. 

        :return: The product_name of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        For an authorization or capture transaction (`processingOptions.capture` is `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the other values that are related to shipping and/or handling.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. 

        :param product_name: The product_name of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._product_name = product_name

    @property
    def product_sku(self):
        """
        Gets the product_sku of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Product identifier code. Also known as the Stock Keeping Unit (SKU) code for the product.  For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not set to **default** or one of the other values that are related to shipping and/or handling.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the values related to shipping and/or handling. 

        :return: The product_sku of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._product_sku

    @product_sku.setter
    def product_sku(self, product_sku):
        """
        Sets the product_sku of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Product identifier code. Also known as the Stock Keeping Unit (SKU) code for the product.  For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not set to **default** or one of the other values that are related to shipping and/or handling.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the values related to shipping and/or handling. 

        :param product_sku: The product_sku of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._product_sku = product_sku

    @property
    def quantity(self):
        """
        Gets the quantity of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Number of units for this order. Must be a non-negative integer.  The default is `1`. For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the other values related to shipping and/or handling.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. 

        :return: The quantity of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Number of units for this order. Must be a non-negative integer.  The default is `1`. For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the other values related to shipping and/or handling.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. 

        :param quantity: The quantity of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: int
        """
        if quantity is not None and quantity > 999999999:
            raise ValueError("Invalid value for `quantity`, must be a value less than or equal to `999999999`")
        if quantity is not None and quantity < 1:
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `1`")

        self._quantity = quantity

    @property
    def unit_price(self):
        """
        Gets the unit_price of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Per-item price of the product. This value for this field cannot be negative.  You must include either this field or the request-level field `orderInformation.amountDetails.totalAmount` in your request.  You can include a decimal point (.), but you cannot include any other special characters. The value is truncated to the correct number of decimal places.  #### DCC with a Third-Party Provider Set this field to the converted amount that was returned by the DCC provider. You must include either the 1st line item in the order and this field, or the request-level field `orderInformation.amountDetails.totalAmount` in your request.  #### FDMS South If you accept IDR or CLP currencies, see the entry for FDMS South in the [Merchant Descriptors Using the SCMP API Guide.] (https://apps.cybersource.com/library/documentation/dev_guides/Merchant_Descriptors_SCMP_API/html/)  #### Tax Calculation Required field for U.S., Canadian, international and value added taxes.  #### Zero Amount Authorizations If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen.  #### Maximum Field Lengths For GPN and JCN Gateway: Decimal (10) All other processors: Decimal (15) 

        :return: The unit_price of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """
        Sets the unit_price of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Per-item price of the product. This value for this field cannot be negative.  You must include either this field or the request-level field `orderInformation.amountDetails.totalAmount` in your request.  You can include a decimal point (.), but you cannot include any other special characters. The value is truncated to the correct number of decimal places.  #### DCC with a Third-Party Provider Set this field to the converted amount that was returned by the DCC provider. You must include either the 1st line item in the order and this field, or the request-level field `orderInformation.amountDetails.totalAmount` in your request.  #### FDMS South If you accept IDR or CLP currencies, see the entry for FDMS South in the [Merchant Descriptors Using the SCMP API Guide.] (https://apps.cybersource.com/library/documentation/dev_guides/Merchant_Descriptors_SCMP_API/html/)  #### Tax Calculation Required field for U.S., Canadian, international and value added taxes.  #### Zero Amount Authorizations If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen.  #### Maximum Field Lengths For GPN and JCN Gateway: Decimal (10) All other processors: Decimal (15) 

        :param unit_price: The unit_price of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._unit_price = unit_price

    @property
    def unit_of_measure(self):
        """
        Gets the unit_of_measure of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Unit of measure, or unit of measure code, for the item. 

        :return: The unit_of_measure of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """
        Sets the unit_of_measure of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Unit of measure, or unit of measure code, for the item. 

        :param unit_of_measure: The unit_of_measure of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._unit_of_measure = unit_of_measure

    @property
    def total_amount(self):
        """
        Gets the total_amount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Total amount for the item. Normally calculated as the unit price times quantity.  When `orderInformation.lineItems[].productCode` is \"gift_card\", this is the purchase amount total for prepaid gift cards in major units.  Example: 123.45 USD = 123 

        :return: The total_amount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """
        Sets the total_amount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Total amount for the item. Normally calculated as the unit price times quantity.  When `orderInformation.lineItems[].productCode` is \"gift_card\", this is the purchase amount total for prepaid gift cards in major units.  Example: 123.45 USD = 123 

        :param total_amount: The total_amount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._total_amount = total_amount

    @property
    def tax_amount(self):
        """
        Gets the tax_amount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Total tax to apply to the product. This value cannot be negative. The tax amount and the offer amount must be in the same currency. The tax amount field is additive.  The following example uses a two-exponent currency such as USD:   1. You include each line item in your request.  ..- 1st line item has amount=10.00, quantity=1, and taxAmount=0.80  ..- 2nd line item has amount=20.00, quantity=1, and taxAmount=1.60  2. The total amount authorized will be 32.40, not 30.00 with 2.40 of tax included.  Optional field.  #### Airlines processing Tax portion of the order amount. This value cannot exceed 99999999999999 (fourteen 9s). Format: English characters only. Optional request field for a line item.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes.  Note if you send this field in your tax request, the value in the field will override the tax engine 

        :return: The tax_amount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """
        Sets the tax_amount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Total tax to apply to the product. This value cannot be negative. The tax amount and the offer amount must be in the same currency. The tax amount field is additive.  The following example uses a two-exponent currency such as USD:   1. You include each line item in your request.  ..- 1st line item has amount=10.00, quantity=1, and taxAmount=0.80  ..- 2nd line item has amount=20.00, quantity=1, and taxAmount=1.60  2. The total amount authorized will be 32.40, not 30.00 with 2.40 of tax included.  Optional field.  #### Airlines processing Tax portion of the order amount. This value cannot exceed 99999999999999 (fourteen 9s). Format: English characters only. Optional request field for a line item.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes.  Note if you send this field in your tax request, the value in the field will override the tax engine 

        :param tax_amount: The tax_amount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._tax_amount = tax_amount

    @property
    def tax_rate(self):
        """
        Gets the tax_rate of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Tax rate applied to the item.  For details, see `tax_rate` field description in the [Level II and Level III Processing Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html/)  **Visa**: Valid range is 0.01 to 0.99 (1% to 99%, with only whole percentage values accepted; values with additional decimal places will be truncated).  **Mastercard**: Valid range is 0.00001 to 0.99999 (0.001% to 99.999%). 

        :return: The tax_rate of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """
        Sets the tax_rate of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Tax rate applied to the item.  For details, see `tax_rate` field description in the [Level II and Level III Processing Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html/)  **Visa**: Valid range is 0.01 to 0.99 (1% to 99%, with only whole percentage values accepted; values with additional decimal places will be truncated).  **Mastercard**: Valid range is 0.00001 to 0.99999 (0.001% to 99.999%). 

        :param tax_rate: The tax_rate of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._tax_rate = tax_rate

    @property
    def tax_applied_after_discount(self):
        """
        Gets the tax_applied_after_discount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Flag to indicate how you handle discount at the line item level.   - 0: no line level discount provided  - 1: tax was calculated on the post-discount line item total  - 2: tax was calculated on the pre-discount line item total  `Note` Visa will inset 0 (zero) if an invalid value is included in this field.  This field relates to the value in the _lineItems[].discountAmount_ field. 

        :return: The tax_applied_after_discount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._tax_applied_after_discount

    @tax_applied_after_discount.setter
    def tax_applied_after_discount(self, tax_applied_after_discount):
        """
        Sets the tax_applied_after_discount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Flag to indicate how you handle discount at the line item level.   - 0: no line level discount provided  - 1: tax was calculated on the post-discount line item total  - 2: tax was calculated on the pre-discount line item total  `Note` Visa will inset 0 (zero) if an invalid value is included in this field.  This field relates to the value in the _lineItems[].discountAmount_ field. 

        :param tax_applied_after_discount: The tax_applied_after_discount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._tax_applied_after_discount = tax_applied_after_discount

    @property
    def tax_status_indicator(self):
        """
        Gets the tax_status_indicator of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Flag to indicate whether tax is exempted or not included.   - 0: tax not included  - 1: tax included  - 2: transaction is not subject to tax 

        :return: The tax_status_indicator of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._tax_status_indicator

    @tax_status_indicator.setter
    def tax_status_indicator(self, tax_status_indicator):
        """
        Sets the tax_status_indicator of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Flag to indicate whether tax is exempted or not included.   - 0: tax not included  - 1: tax included  - 2: transaction is not subject to tax 

        :param tax_status_indicator: The tax_status_indicator of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._tax_status_indicator = tax_status_indicator

    @property
    def tax_type_code(self):
        """
        Gets the tax_type_code of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Type of tax being applied to the item.  For possible values, see the processor-specific field descriptions in [Level II and Level III Processing Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html/):  #### FDC Nashville Global - `alternate_tax_type_applied` - `alternate_tax_type_identifier`  #### Worldpay VAP - `alternate_tax_type_identifier`  #### RBS WorldPay Atlanta - `tax_type_applied`  #### TSYS Acquiring Solutions - `tax_type_applied` - `local_tax_indicator`  #### Chase Paymentech Solutions - `tax_type_applied`  #### Elavon Americas - `local_tax_indicator`  #### FDC Compass - `tax_type_applied`  #### OmniPay Direct - `local_tax_indicator` 

        :return: The tax_type_code of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._tax_type_code

    @tax_type_code.setter
    def tax_type_code(self, tax_type_code):
        """
        Sets the tax_type_code of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Type of tax being applied to the item.  For possible values, see the processor-specific field descriptions in [Level II and Level III Processing Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html/):  #### FDC Nashville Global - `alternate_tax_type_applied` - `alternate_tax_type_identifier`  #### Worldpay VAP - `alternate_tax_type_identifier`  #### RBS WorldPay Atlanta - `tax_type_applied`  #### TSYS Acquiring Solutions - `tax_type_applied` - `local_tax_indicator`  #### Chase Paymentech Solutions - `tax_type_applied`  #### Elavon Americas - `local_tax_indicator`  #### FDC Compass - `tax_type_applied`  #### OmniPay Direct - `local_tax_indicator` 

        :param tax_type_code: The tax_type_code of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._tax_type_code = tax_type_code

    @property
    def amount_includes_tax(self):
        """
        Gets the amount_includes_tax of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Flag that indicates whether the tax amount is included in the Line Item Total.  Possible values:  - **true**  - **false** 

        :return: The amount_includes_tax of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: bool
        """
        return self._amount_includes_tax

    @amount_includes_tax.setter
    def amount_includes_tax(self, amount_includes_tax):
        """
        Sets the amount_includes_tax of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Flag that indicates whether the tax amount is included in the Line Item Total.  Possible values:  - **true**  - **false** 

        :param amount_includes_tax: The amount_includes_tax of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: bool
        """

        self._amount_includes_tax = amount_includes_tax

    @property
    def type_of_supply(self):
        """
        Gets the type_of_supply of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Flag to indicate whether the purchase is categorized as goods or services. Possible values:   - 00: goods  - 01: services 

        :return: The type_of_supply of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._type_of_supply

    @type_of_supply.setter
    def type_of_supply(self, type_of_supply):
        """
        Sets the type_of_supply of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Flag to indicate whether the purchase is categorized as goods or services. Possible values:   - 00: goods  - 01: services 

        :param type_of_supply: The type_of_supply of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._type_of_supply = type_of_supply

    @property
    def commodity_code(self):
        """
        Gets the commodity_code of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Commodity code or International description code used to classify the item. Contact your acquirer for a list of codes. 

        :return: The commodity_code of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._commodity_code

    @commodity_code.setter
    def commodity_code(self, commodity_code):
        """
        Sets the commodity_code of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Commodity code or International description code used to classify the item. Contact your acquirer for a list of codes. 

        :param commodity_code: The commodity_code of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._commodity_code = commodity_code

    @property
    def discount_amount(self):
        """
        Gets the discount_amount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Discount applied to the item.

        :return: The discount_amount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """
        Sets the discount_amount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Discount applied to the item.

        :param discount_amount: The discount_amount of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._discount_amount = discount_amount

    @property
    def discount_applied(self):
        """
        Gets the discount_applied of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Flag that indicates whether the amount is discounted.  If you do not provide a value but you set Discount Amount to a value greater than zero, then CyberSource sets this field to **true**.  Possible values:  - **true**  - **false** 

        :return: The discount_applied of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: bool
        """
        return self._discount_applied

    @discount_applied.setter
    def discount_applied(self, discount_applied):
        """
        Sets the discount_applied of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Flag that indicates whether the amount is discounted.  If you do not provide a value but you set Discount Amount to a value greater than zero, then CyberSource sets this field to **true**.  Possible values:  - **true**  - **false** 

        :param discount_applied: The discount_applied of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: bool
        """

        self._discount_applied = discount_applied

    @property
    def discount_rate(self):
        """
        Gets the discount_rate of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Rate the item is discounted. Maximum of 2 decimal places.  Example 5.25 (=5.25%) 

        :return: The discount_rate of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, discount_rate):
        """
        Sets the discount_rate of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Rate the item is discounted. Maximum of 2 decimal places.  Example 5.25 (=5.25%) 

        :param discount_rate: The discount_rate of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._discount_rate = discount_rate

    @property
    def invoice_number(self):
        """
        Gets the invoice_number of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Field to support an invoice number for a transaction. You must specify the number of line items that will include an invoice number. By default, the first line item will include an invoice number field. The invoice number field can be included for up to 10 line items. 

        :return: The invoice_number of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """
        Sets the invoice_number of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        Field to support an invoice number for a transaction. You must specify the number of line items that will include an invoice number. By default, the first line item will include an invoice number field. The invoice number field can be included for up to 10 line items. 

        :param invoice_number: The invoice_number of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def tax_details(self):
        """
        Gets the tax_details of this Ptsv2paymentsidrefundsOrderInformationLineItems.

        :return: The tax_details of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :rtype: list[Ptsv2paymentsOrderInformationAmountDetailsTaxDetails]
        """
        return self._tax_details

    @tax_details.setter
    def tax_details(self, tax_details):
        """
        Sets the tax_details of this Ptsv2paymentsidrefundsOrderInformationLineItems.

        :param tax_details: The tax_details of this Ptsv2paymentsidrefundsOrderInformationLineItems.
        :type: list[Ptsv2paymentsOrderInformationAmountDetailsTaxDetails]
        """

        self._tax_details = tax_details

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Ptsv2paymentsidrefundsOrderInformationLineItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
