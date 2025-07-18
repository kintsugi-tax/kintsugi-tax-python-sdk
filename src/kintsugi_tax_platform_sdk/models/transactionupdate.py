"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .address_input import AddressInput, AddressInputTypedDict
from .addressstatus import AddressStatus
from .countrycodeenum import CountryCodeEnum
from .currencyenum import CurrencyEnum
from .customerupdate import CustomerUpdate, CustomerUpdateTypedDict
from .exemption import Exemption, ExemptionTypedDict
from .exemptionrequired import ExemptionRequired, ExemptionRequiredTypedDict
from .processingstatusenum import ProcessingStatusEnum
from .sourceenum import SourceEnum
from .taxliabilitysourceenum import TaxLiabilitySourceEnum
from .transactionaddressbuilder import (
    TransactionAddressBuilder,
    TransactionAddressBuilderTypedDict,
)
from .transactionexemptstatusenum import TransactionExemptStatusEnum
from .transactionitemcreateupdate import (
    TransactionItemCreateUpdate,
    TransactionItemCreateUpdateTypedDict,
)
from .transactionrefundstatus import TransactionRefundStatus
from .transactionstatusenum import TransactionStatusEnum
from datetime import date, datetime
from kintsugi_tax_platform_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


TransactionUpdateTotalAmountTypedDict = TypeAliasType(
    "TransactionUpdateTotalAmountTypedDict", Union[float, str]
)
r"""Total amount of the transaction."""


TransactionUpdateTotalAmount = TypeAliasType(
    "TransactionUpdateTotalAmount", Union[float, str]
)
r"""Total amount of the transaction."""


TransactionUpdateTotalTaxAmountImportedTypedDict = TypeAliasType(
    "TransactionUpdateTotalTaxAmountImportedTypedDict", Union[float, str]
)
r"""Imported tax amount."""


TransactionUpdateTotalTaxAmountImported = TypeAliasType(
    "TransactionUpdateTotalTaxAmountImported", Union[float, str]
)
r"""Imported tax amount."""


TransactionUpdateTaxRateImportedTypedDict = TypeAliasType(
    "TransactionUpdateTaxRateImportedTypedDict", Union[float, str]
)
r"""Imported tax rate."""


TransactionUpdateTaxRateImported = TypeAliasType(
    "TransactionUpdateTaxRateImported", Union[float, str]
)
r"""Imported tax rate."""


TransactionUpdateTotalTaxAmountCalculatedTypedDict = TypeAliasType(
    "TransactionUpdateTotalTaxAmountCalculatedTypedDict", Union[float, str]
)
r"""Calculated tax amount."""


TransactionUpdateTotalTaxAmountCalculated = TypeAliasType(
    "TransactionUpdateTotalTaxAmountCalculated", Union[float, str]
)
r"""Calculated tax amount."""


TransactionUpdateTaxRateCalculatedTypedDict = TypeAliasType(
    "TransactionUpdateTaxRateCalculatedTypedDict", Union[float, str]
)
r"""Calculated tax rate."""


TransactionUpdateTaxRateCalculated = TypeAliasType(
    "TransactionUpdateTaxRateCalculated", Union[float, str]
)
r"""Calculated tax rate."""


TransactionUpdateTotalTaxLiabilityAmountTypedDict = TypeAliasType(
    "TransactionUpdateTotalTaxLiabilityAmountTypedDict", Union[float, str]
)
r"""Total tax liability amount."""


TransactionUpdateTotalTaxLiabilityAmount = TypeAliasType(
    "TransactionUpdateTotalTaxLiabilityAmount", Union[float, str]
)
r"""Total tax liability amount."""


TransactionUpdateTaxableAmountTypedDict = TypeAliasType(
    "TransactionUpdateTaxableAmountTypedDict", Union[float, str]
)
r"""Taxable amount."""


TransactionUpdateTaxableAmount = TypeAliasType(
    "TransactionUpdateTaxableAmount", Union[float, str]
)
r"""Taxable amount."""


TransactionUpdateConvertedTotalAmountTypedDict = TypeAliasType(
    "TransactionUpdateConvertedTotalAmountTypedDict", Union[float, str]
)
r"""Converted total amount."""


TransactionUpdateConvertedTotalAmount = TypeAliasType(
    "TransactionUpdateConvertedTotalAmount", Union[float, str]
)
r"""Converted total amount."""


TransactionUpdateConvertedTotalTaxAmountImportedTypedDict = TypeAliasType(
    "TransactionUpdateConvertedTotalTaxAmountImportedTypedDict", Union[float, str]
)
r"""Converted imported tax amount."""


TransactionUpdateConvertedTotalTaxAmountImported = TypeAliasType(
    "TransactionUpdateConvertedTotalTaxAmountImported", Union[float, str]
)
r"""Converted imported tax amount."""


TransactionUpdateConvertedTotalTaxAmountCalculatedTypedDict = TypeAliasType(
    "TransactionUpdateConvertedTotalTaxAmountCalculatedTypedDict", Union[float, str]
)
r"""Converted calculated tax amount."""


TransactionUpdateConvertedTotalTaxAmountCalculated = TypeAliasType(
    "TransactionUpdateConvertedTotalTaxAmountCalculated", Union[float, str]
)
r"""Converted calculated tax amount."""


TransactionUpdateConversionRateTypedDict = TypeAliasType(
    "TransactionUpdateConversionRateTypedDict", Union[float, str]
)
r"""Currency conversion rate."""


TransactionUpdateConversionRate = TypeAliasType(
    "TransactionUpdateConversionRate", Union[float, str]
)
r"""Currency conversion rate."""


TransactionUpdateConvertedTaxableAmountTypedDict = TypeAliasType(
    "TransactionUpdateConvertedTaxableAmountTypedDict", Union[float, str]
)
r"""Converted taxable amount."""


TransactionUpdateConvertedTaxableAmount = TypeAliasType(
    "TransactionUpdateConvertedTaxableAmount", Union[float, str]
)
r"""Converted taxable amount."""


TransactionUpdateConvertedTotalDiscountTypedDict = TypeAliasType(
    "TransactionUpdateConvertedTotalDiscountTypedDict", Union[float, str]
)
r"""Converted total discount amount."""


TransactionUpdateConvertedTotalDiscount = TypeAliasType(
    "TransactionUpdateConvertedTotalDiscount", Union[float, str]
)
r"""Converted total discount amount."""


TransactionUpdateConvertedSubtotalTypedDict = TypeAliasType(
    "TransactionUpdateConvertedSubtotalTypedDict", Union[float, str]
)
r"""Converted subtotal amount."""


TransactionUpdateConvertedSubtotal = TypeAliasType(
    "TransactionUpdateConvertedSubtotal", Union[float, str]
)
r"""Converted subtotal amount."""


TransactionUpdateConvertedTotalTaxLiabilityAmountTypedDict = TypeAliasType(
    "TransactionUpdateConvertedTotalTaxLiabilityAmountTypedDict", Union[float, str]
)
r"""Converted total tax liability amount."""


TransactionUpdateConvertedTotalTaxLiabilityAmount = TypeAliasType(
    "TransactionUpdateConvertedTotalTaxLiabilityAmount", Union[float, str]
)
r"""Converted total tax liability amount."""


TransactionUpdateAddressesTypedDict = TypeAliasType(
    "TransactionUpdateAddressesTypedDict",
    Union[List[TransactionAddressBuilderTypedDict], List[AddressInputTypedDict]],
)


TransactionUpdateAddresses = TypeAliasType(
    "TransactionUpdateAddresses",
    Union[List[TransactionAddressBuilder], List[AddressInput]],
)


class TransactionUpdateTypedDict(TypedDict):
    organization_id: str
    r"""Unique identifier of the organization."""
    external_id: str
    r"""External identifier of the transaction."""
    date_: datetime
    r"""Transaction date and time"""
    addresses: TransactionUpdateAddressesTypedDict
    transaction_items: List[TransactionItemCreateUpdateTypedDict]
    customer: CustomerUpdateTypedDict
    requires_exemption: NotRequired[Nullable[ExemptionRequiredTypedDict]]
    r"""Indicates if transaction requires tax exemption."""
    shop_date: NotRequired[Nullable[date]]
    r"""Transaction date in the shop's local timezone"""
    shop_date_tz: NotRequired[Nullable[str]]
    r"""Timezone of the shop"""
    status: NotRequired[TransactionStatusEnum]
    description: NotRequired[Nullable[str]]
    r"""Description of the transaction."""
    refund_status: NotRequired[Nullable[TransactionRefundStatus]]
    r"""Status of refund, if applicable"""
    total_amount: NotRequired[TransactionUpdateTotalAmountTypedDict]
    r"""Total amount of the transaction."""
    customer_id: NotRequired[Nullable[str]]
    r"""Unique identifier of the customer."""
    marketplace: NotRequired[Nullable[bool]]
    r"""Indicates if transaction is marketplace-based."""
    exempt: NotRequired[Nullable[TransactionExemptStatusEnum]]
    r"""Exemption status (e.g., NOT_EXEMPT)"""
    exemptions: NotRequired[Nullable[List[ExemptionTypedDict]]]
    r"""List of exemptions applied (if any)."""
    related_to: NotRequired[Nullable[str]]
    r"""Related transaction identifier."""
    secondary_external_id: NotRequired[Nullable[str]]
    r"""Secondary External Identifier."""
    secondary_source: NotRequired[Nullable[str]]
    r"""Secondary source information"""
    external_friendly_id: NotRequired[Nullable[str]]
    r"""Friendly identifier of the original item."""
    total_tax_amount_imported: NotRequired[
        TransactionUpdateTotalTaxAmountImportedTypedDict
    ]
    r"""Imported tax amount."""
    tax_rate_imported: NotRequired[TransactionUpdateTaxRateImportedTypedDict]
    r"""Imported tax rate."""
    total_tax_amount_calculated: NotRequired[
        TransactionUpdateTotalTaxAmountCalculatedTypedDict
    ]
    r"""Calculated tax amount."""
    tax_rate_calculated: NotRequired[TransactionUpdateTaxRateCalculatedTypedDict]
    r"""Calculated tax rate."""
    total_tax_liability_amount: NotRequired[
        TransactionUpdateTotalTaxLiabilityAmountTypedDict
    ]
    r"""Total tax liability amount."""
    tax_liability_source: NotRequired[Nullable[TaxLiabilitySourceEnum]]
    r"""Source of tax liability."""
    taxable_amount: NotRequired[TransactionUpdateTaxableAmountTypedDict]
    r"""Taxable amount."""
    currency: NotRequired[CurrencyEnum]
    locked: NotRequired[bool]
    r"""Transaction lock status."""
    source: NotRequired[SourceEnum]
    connection_id: NotRequired[Nullable[str]]
    r"""Connection Identifier"""
    filing_id: NotRequired[Nullable[str]]
    r"""Filing identifier."""
    city: NotRequired[Nullable[str]]
    r"""City of the transaction address."""
    county: NotRequired[Nullable[str]]
    r"""County of the transaction address."""
    state: NotRequired[Nullable[str]]
    r"""State of the transaction address."""
    country: NotRequired[Nullable[CountryCodeEnum]]
    r"""Country code (ISO Alpha-2)."""
    postal_code: NotRequired[Nullable[str]]
    r"""Postal code of the transaction."""
    tax_id: NotRequired[Nullable[str]]
    r"""Tax ID associated with the transaction"""
    address_status: NotRequired[AddressStatus]
    processing_status: NotRequired[ProcessingStatusEnum]
    r"""Our transaction state, used to determine when/if a transaction needs additional
    processing.
    """
    destination_currency: NotRequired[Nullable[CurrencyEnum]]
    r"""Destination currency code (ISO 4217, e.g., USD)"""
    converted_total_amount: NotRequired[
        Nullable[TransactionUpdateConvertedTotalAmountTypedDict]
    ]
    r"""Converted total amount."""
    converted_total_tax_amount_imported: NotRequired[
        Nullable[TransactionUpdateConvertedTotalTaxAmountImportedTypedDict]
    ]
    r"""Converted imported tax amount."""
    converted_total_tax_amount_calculated: NotRequired[
        Nullable[TransactionUpdateConvertedTotalTaxAmountCalculatedTypedDict]
    ]
    r"""Converted calculated tax amount."""
    conversion_rate: NotRequired[Nullable[TransactionUpdateConversionRateTypedDict]]
    r"""Currency conversion rate."""
    converted_taxable_amount: NotRequired[
        Nullable[TransactionUpdateConvertedTaxableAmountTypedDict]
    ]
    r"""Converted taxable amount."""
    converted_total_discount: NotRequired[
        Nullable[TransactionUpdateConvertedTotalDiscountTypedDict]
    ]
    r"""Converted total discount amount."""
    converted_subtotal: NotRequired[
        Nullable[TransactionUpdateConvertedSubtotalTypedDict]
    ]
    r"""Converted subtotal amount."""
    converted_total_tax_liability_amount: NotRequired[
        Nullable[TransactionUpdateConvertedTotalTaxLiabilityAmountTypedDict]
    ]
    r"""Converted total tax liability amount."""


class TransactionUpdate(BaseModel):
    organization_id: str
    r"""Unique identifier of the organization."""

    external_id: str
    r"""External identifier of the transaction."""

    date_: Annotated[datetime, pydantic.Field(alias="date")]
    r"""Transaction date and time"""

    addresses: TransactionUpdateAddresses

    transaction_items: List[TransactionItemCreateUpdate]

    customer: CustomerUpdate

    requires_exemption: OptionalNullable[ExemptionRequired] = UNSET
    r"""Indicates if transaction requires tax exemption."""

    shop_date: OptionalNullable[date] = UNSET
    r"""Transaction date in the shop's local timezone"""

    shop_date_tz: OptionalNullable[str] = UNSET
    r"""Timezone of the shop"""

    status: Optional[TransactionStatusEnum] = None

    description: OptionalNullable[str] = UNSET
    r"""Description of the transaction."""

    refund_status: OptionalNullable[TransactionRefundStatus] = UNSET
    r"""Status of refund, if applicable"""

    total_amount: Optional[TransactionUpdateTotalAmount] = None
    r"""Total amount of the transaction."""

    customer_id: OptionalNullable[str] = UNSET
    r"""Unique identifier of the customer."""

    marketplace: OptionalNullable[bool] = UNSET
    r"""Indicates if transaction is marketplace-based."""

    exempt: OptionalNullable[TransactionExemptStatusEnum] = UNSET
    r"""Exemption status (e.g., NOT_EXEMPT)"""

    exemptions: OptionalNullable[List[Exemption]] = UNSET
    r"""List of exemptions applied (if any)."""

    related_to: OptionalNullable[str] = UNSET
    r"""Related transaction identifier."""

    secondary_external_id: OptionalNullable[str] = UNSET
    r"""Secondary External Identifier."""

    secondary_source: OptionalNullable[str] = UNSET
    r"""Secondary source information"""

    external_friendly_id: OptionalNullable[str] = UNSET
    r"""Friendly identifier of the original item."""

    total_tax_amount_imported: Optional[TransactionUpdateTotalTaxAmountImported] = None
    r"""Imported tax amount."""

    tax_rate_imported: Optional[TransactionUpdateTaxRateImported] = None
    r"""Imported tax rate."""

    total_tax_amount_calculated: Optional[TransactionUpdateTotalTaxAmountCalculated] = (
        None
    )
    r"""Calculated tax amount."""

    tax_rate_calculated: Optional[TransactionUpdateTaxRateCalculated] = None
    r"""Calculated tax rate."""

    total_tax_liability_amount: Optional[TransactionUpdateTotalTaxLiabilityAmount] = (
        None
    )
    r"""Total tax liability amount."""

    tax_liability_source: OptionalNullable[TaxLiabilitySourceEnum] = UNSET
    r"""Source of tax liability."""

    taxable_amount: Optional[TransactionUpdateTaxableAmount] = None
    r"""Taxable amount."""

    currency: Optional[CurrencyEnum] = None

    locked: Optional[bool] = False
    r"""Transaction lock status."""

    source: Optional[SourceEnum] = None

    connection_id: OptionalNullable[str] = UNSET
    r"""Connection Identifier"""

    filing_id: OptionalNullable[str] = UNSET
    r"""Filing identifier."""

    city: OptionalNullable[str] = UNSET
    r"""City of the transaction address."""

    county: OptionalNullable[str] = UNSET
    r"""County of the transaction address."""

    state: OptionalNullable[str] = UNSET
    r"""State of the transaction address."""

    country: OptionalNullable[CountryCodeEnum] = UNSET
    r"""Country code (ISO Alpha-2)."""

    postal_code: OptionalNullable[str] = UNSET
    r"""Postal code of the transaction."""

    tax_id: OptionalNullable[str] = UNSET
    r"""Tax ID associated with the transaction"""

    address_status: Optional[AddressStatus] = None

    processing_status: Optional[ProcessingStatusEnum] = None
    r"""Our transaction state, used to determine when/if a transaction needs additional
    processing.
    """

    destination_currency: OptionalNullable[CurrencyEnum] = UNSET
    r"""Destination currency code (ISO 4217, e.g., USD)"""

    converted_total_amount: OptionalNullable[TransactionUpdateConvertedTotalAmount] = (
        UNSET
    )
    r"""Converted total amount."""

    converted_total_tax_amount_imported: OptionalNullable[
        TransactionUpdateConvertedTotalTaxAmountImported
    ] = UNSET
    r"""Converted imported tax amount."""

    converted_total_tax_amount_calculated: OptionalNullable[
        TransactionUpdateConvertedTotalTaxAmountCalculated
    ] = UNSET
    r"""Converted calculated tax amount."""

    conversion_rate: OptionalNullable[TransactionUpdateConversionRate] = UNSET
    r"""Currency conversion rate."""

    converted_taxable_amount: OptionalNullable[
        TransactionUpdateConvertedTaxableAmount
    ] = UNSET
    r"""Converted taxable amount."""

    converted_total_discount: OptionalNullable[
        TransactionUpdateConvertedTotalDiscount
    ] = UNSET
    r"""Converted total discount amount."""

    converted_subtotal: OptionalNullable[TransactionUpdateConvertedSubtotal] = UNSET
    r"""Converted subtotal amount."""

    converted_total_tax_liability_amount: OptionalNullable[
        TransactionUpdateConvertedTotalTaxLiabilityAmount
    ] = UNSET
    r"""Converted total tax liability amount."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "requires_exemption",
            "shop_date",
            "shop_date_tz",
            "status",
            "description",
            "refund_status",
            "total_amount",
            "customer_id",
            "marketplace",
            "exempt",
            "exemptions",
            "related_to",
            "secondary_external_id",
            "secondary_source",
            "external_friendly_id",
            "total_tax_amount_imported",
            "tax_rate_imported",
            "total_tax_amount_calculated",
            "tax_rate_calculated",
            "total_tax_liability_amount",
            "tax_liability_source",
            "taxable_amount",
            "currency",
            "locked",
            "source",
            "connection_id",
            "filing_id",
            "city",
            "county",
            "state",
            "country",
            "postal_code",
            "tax_id",
            "address_status",
            "processing_status",
            "destination_currency",
            "converted_total_amount",
            "converted_total_tax_amount_imported",
            "converted_total_tax_amount_calculated",
            "conversion_rate",
            "converted_taxable_amount",
            "converted_total_discount",
            "converted_subtotal",
            "converted_total_tax_liability_amount",
        ]
        nullable_fields = [
            "requires_exemption",
            "shop_date",
            "shop_date_tz",
            "description",
            "refund_status",
            "customer_id",
            "marketplace",
            "exempt",
            "exemptions",
            "related_to",
            "secondary_external_id",
            "secondary_source",
            "external_friendly_id",
            "tax_liability_source",
            "connection_id",
            "filing_id",
            "city",
            "county",
            "state",
            "country",
            "postal_code",
            "tax_id",
            "destination_currency",
            "converted_total_amount",
            "converted_total_tax_amount_imported",
            "converted_total_tax_amount_calculated",
            "conversion_rate",
            "converted_taxable_amount",
            "converted_total_discount",
            "converted_subtotal",
            "converted_total_tax_liability_amount",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
