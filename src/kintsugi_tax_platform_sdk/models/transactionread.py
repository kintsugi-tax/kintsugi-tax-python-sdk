"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .addressstatus import AddressStatus
from .countrycodeenum import CountryCodeEnum
from .currencyenum import CurrencyEnum
from .customerread import CustomerRead, CustomerReadTypedDict
from .exemption import Exemption, ExemptionTypedDict
from .exemptionrequired import ExemptionRequired, ExemptionRequiredTypedDict
from .processingstatusenum import ProcessingStatusEnum
from .sourceenum import SourceEnum
from .taxliabilitysourceenum import TaxLiabilitySourceEnum
from .transactionaddressread_output import (
    TransactionAddressReadOutput,
    TransactionAddressReadOutputTypedDict,
)
from .transactionexemptstatusenum import TransactionExemptStatusEnum
from .transactionitemread import TransactionItemRead, TransactionItemReadTypedDict
from .transactionrefundstatus import TransactionRefundStatus
from .transactionstatusenum import TransactionStatusEnum
from .transactiontypeenum import TransactionTypeEnum
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
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TransactionReadTypedDict(TypedDict):
    organization_id: str
    r"""Unique identifier of the organization."""
    external_id: str
    r"""External identifier of the transaction."""
    date_: datetime
    r"""Transaction date and time"""
    id: str
    r"""The unique transaction identifier."""
    addresses: List[TransactionAddressReadOutputTypedDict]
    r"""List of addresses associated."""
    transaction_items: List[TransactionItemReadTypedDict]
    r"""List of items in the transaction."""
    type: TransactionTypeEnum
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
    total_amount: NotRequired[str]
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
    total_tax_amount_imported: NotRequired[str]
    r"""Imported tax amount."""
    tax_rate_imported: NotRequired[str]
    r"""Imported tax rate."""
    total_tax_amount_calculated: NotRequired[str]
    r"""Calculated tax amount."""
    tax_rate_calculated: NotRequired[str]
    r"""Calculated tax rate."""
    total_tax_liability_amount: NotRequired[str]
    r"""Total tax liability amount."""
    tax_liability_source: NotRequired[Nullable[TaxLiabilitySourceEnum]]
    r"""Source of tax liability."""
    taxable_amount: NotRequired[str]
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
    converted_total_amount: NotRequired[Nullable[str]]
    r"""Converted total amount."""
    converted_total_tax_amount_imported: NotRequired[Nullable[str]]
    r"""Converted imported tax amount."""
    converted_total_tax_amount_calculated: NotRequired[Nullable[str]]
    r"""Converted calculated tax amount."""
    conversion_rate: NotRequired[Nullable[str]]
    r"""Currency conversion rate."""
    converted_taxable_amount: NotRequired[Nullable[str]]
    r"""Converted taxable amount."""
    converted_total_discount: NotRequired[Nullable[str]]
    r"""Converted total discount amount."""
    converted_subtotal: NotRequired[Nullable[str]]
    r"""Converted subtotal amount."""
    converted_total_tax_liability_amount: NotRequired[Nullable[str]]
    r"""Converted total tax liability amount."""
    customer: NotRequired[Nullable[CustomerReadTypedDict]]
    r"""Customer information associated with the transaction."""
    total_discount: NotRequired[Nullable[str]]
    r"""Total amount of all discounts applied to the transaction."""
    subtotal: NotRequired[Nullable[str]]
    r"""Subtotal amount before any discounts are applied."""
    final_total_amount: NotRequired[Nullable[str]]
    r"""Final total amount including tax liability."""
    converted_final_total_amount: NotRequired[Nullable[str]]
    r"""Converted final total amount including tax liability."""


class TransactionRead(BaseModel):
    organization_id: str
    r"""Unique identifier of the organization."""

    external_id: str
    r"""External identifier of the transaction."""

    date_: Annotated[datetime, pydantic.Field(alias="date")]
    r"""Transaction date and time"""

    id: str
    r"""The unique transaction identifier."""

    addresses: List[TransactionAddressReadOutput]
    r"""List of addresses associated."""

    transaction_items: List[TransactionItemRead]
    r"""List of items in the transaction."""

    type: TransactionTypeEnum

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

    total_amount: Optional[str] = "0.00"
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

    total_tax_amount_imported: Optional[str] = "0.00"
    r"""Imported tax amount."""

    tax_rate_imported: Optional[str] = "0.00"
    r"""Imported tax rate."""

    total_tax_amount_calculated: Optional[str] = "0.00"
    r"""Calculated tax amount."""

    tax_rate_calculated: Optional[str] = "0.00"
    r"""Calculated tax rate."""

    total_tax_liability_amount: Optional[str] = "0.00"
    r"""Total tax liability amount."""

    tax_liability_source: OptionalNullable[TaxLiabilitySourceEnum] = UNSET
    r"""Source of tax liability."""

    taxable_amount: Optional[str] = "0.00"
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

    converted_total_amount: OptionalNullable[str] = UNSET
    r"""Converted total amount."""

    converted_total_tax_amount_imported: OptionalNullable[str] = UNSET
    r"""Converted imported tax amount."""

    converted_total_tax_amount_calculated: OptionalNullable[str] = UNSET
    r"""Converted calculated tax amount."""

    conversion_rate: OptionalNullable[str] = UNSET
    r"""Currency conversion rate."""

    converted_taxable_amount: OptionalNullable[str] = UNSET
    r"""Converted taxable amount."""

    converted_total_discount: OptionalNullable[str] = UNSET
    r"""Converted total discount amount."""

    converted_subtotal: OptionalNullable[str] = UNSET
    r"""Converted subtotal amount."""

    converted_total_tax_liability_amount: OptionalNullable[str] = UNSET
    r"""Converted total tax liability amount."""

    customer: OptionalNullable[CustomerRead] = UNSET
    r"""Customer information associated with the transaction."""

    total_discount: OptionalNullable[str] = UNSET
    r"""Total amount of all discounts applied to the transaction."""

    subtotal: OptionalNullable[str] = UNSET
    r"""Subtotal amount before any discounts are applied."""

    final_total_amount: OptionalNullable[str] = UNSET
    r"""Final total amount including tax liability."""

    converted_final_total_amount: OptionalNullable[str] = UNSET
    r"""Converted final total amount including tax liability."""

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
            "customer",
            "total_discount",
            "subtotal",
            "final_total_amount",
            "converted_final_total_amount",
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
            "customer",
            "total_discount",
            "subtotal",
            "final_total_amount",
            "converted_final_total_amount",
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
