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
from datetime import datetime
from kintsugi_tax_platform_sdk.types import BaseModel
import pydantic
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
    requires_exemption: NotRequired[ExemptionRequiredTypedDict]
    shop_date: NotRequired[str]
    r"""Transaction date in the shop's local timezone"""
    shop_date_tz: NotRequired[str]
    r"""Timezone of the shop"""
    status: NotRequired[TransactionStatusEnum]
    description: NotRequired[str]
    r"""Description of the transaction."""
    refund_status: NotRequired[TransactionRefundStatus]
    r"""Shopify has 2 order statuses for refund case: refunded and partially_refunded
    If the given order has different status from these 2, we will set the
    transaction's refund_status to PARTIALLY_REFUNDED by default.
    """
    total_amount: NotRequired[str]
    r"""Total amount of the transaction."""
    customer_id: NotRequired[str]
    r"""Unique identifier of the customer."""
    marketplace: NotRequired[bool]
    r"""Indicates if transaction is marketplace-based."""
    exempt: NotRequired[TransactionExemptStatusEnum]
    r"""Based on transaction item exempt status.
    NOT EXEMPT: None of the items are NOT EXEMPT
    PARTIALLY EXEMPT: At least some of the items are NOT EXEMPT
    FULLY_EXEMPT: All items sold in the transaction are EXEMPT
    """
    exemptions: NotRequired[List[ExemptionTypedDict]]
    r"""List of exemptions applied (if any)."""
    related_to: NotRequired[str]
    r"""Related transaction identifier."""
    secondary_external_id: NotRequired[str]
    r"""Secondary External Identifier."""
    secondary_source: NotRequired[str]
    r"""Secondary source information"""
    external_friendly_id: NotRequired[str]
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
    tax_liability_source: NotRequired[TaxLiabilitySourceEnum]
    taxable_amount: NotRequired[str]
    r"""Taxable amount."""
    currency: NotRequired[CurrencyEnum]
    locked: NotRequired[bool]
    r"""Transaction lock status."""
    source: NotRequired[SourceEnum]
    connection_id: NotRequired[str]
    r"""Connection Identifier"""
    filing_id: NotRequired[str]
    r"""Filing identifier."""
    city: NotRequired[str]
    r"""City of the transaction address."""
    county: NotRequired[str]
    r"""County of the transaction address."""
    state: NotRequired[str]
    r"""State of the transaction address."""
    country: NotRequired[CountryCodeEnum]
    postal_code: NotRequired[str]
    r"""Postal code of the transaction."""
    tax_id: NotRequired[str]
    r"""Tax ID associated with the transaction"""
    address_status: NotRequired[AddressStatus]
    processing_status: NotRequired[ProcessingStatusEnum]
    r"""Our transaction state, used to determine when/if a transaction needs additional
    processing.
    """
    destination_currency: NotRequired[CurrencyEnum]
    converted_total_amount: NotRequired[str]
    r"""Converted total amount."""
    converted_total_tax_amount_imported: NotRequired[str]
    r"""Converted imported tax amount."""
    converted_total_tax_amount_calculated: NotRequired[str]
    r"""Converted calculated tax amount."""
    conversion_rate: NotRequired[str]
    r"""Currency conversion rate."""
    converted_taxable_amount: NotRequired[str]
    r"""Converted taxable amount."""
    converted_total_discount: NotRequired[str]
    r"""Converted total discount amount."""
    converted_subtotal: NotRequired[str]
    r"""Converted subtotal amount."""
    converted_total_tax_liability_amount: NotRequired[str]
    r"""Converted total tax liability amount."""
    customer: NotRequired[CustomerReadTypedDict]
    total_discount: NotRequired[str]
    r"""Total amount of all discounts applied to the transaction."""
    subtotal: NotRequired[str]
    r"""Subtotal amount before any discounts are applied."""
    final_total_amount: NotRequired[str]
    r"""Final total amount including tax liability."""
    converted_final_total_amount: NotRequired[str]
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

    requires_exemption: Optional[ExemptionRequired] = None

    shop_date: Optional[str] = None
    r"""Transaction date in the shop's local timezone"""

    shop_date_tz: Optional[str] = None
    r"""Timezone of the shop"""

    status: Optional[TransactionStatusEnum] = None

    description: Optional[str] = None
    r"""Description of the transaction."""

    refund_status: Optional[TransactionRefundStatus] = None
    r"""Shopify has 2 order statuses for refund case: refunded and partially_refunded
    If the given order has different status from these 2, we will set the
    transaction's refund_status to PARTIALLY_REFUNDED by default.
    """

    total_amount: Optional[str] = "0.00"
    r"""Total amount of the transaction."""

    customer_id: Optional[str] = None
    r"""Unique identifier of the customer."""

    marketplace: Optional[bool] = False
    r"""Indicates if transaction is marketplace-based."""

    exempt: Optional[TransactionExemptStatusEnum] = None
    r"""Based on transaction item exempt status.
    NOT EXEMPT: None of the items are NOT EXEMPT
    PARTIALLY EXEMPT: At least some of the items are NOT EXEMPT
    FULLY_EXEMPT: All items sold in the transaction are EXEMPT
    """

    exemptions: Optional[List[Exemption]] = None
    r"""List of exemptions applied (if any)."""

    related_to: Optional[str] = None
    r"""Related transaction identifier."""

    secondary_external_id: Optional[str] = None
    r"""Secondary External Identifier."""

    secondary_source: Optional[str] = None
    r"""Secondary source information"""

    external_friendly_id: Optional[str] = None
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

    tax_liability_source: Optional[TaxLiabilitySourceEnum] = None

    taxable_amount: Optional[str] = "0.00"
    r"""Taxable amount."""

    currency: Optional[CurrencyEnum] = None

    locked: Optional[bool] = False
    r"""Transaction lock status."""

    source: Optional[SourceEnum] = None

    connection_id: Optional[str] = None
    r"""Connection Identifier"""

    filing_id: Optional[str] = None
    r"""Filing identifier."""

    city: Optional[str] = None
    r"""City of the transaction address."""

    county: Optional[str] = None
    r"""County of the transaction address."""

    state: Optional[str] = None
    r"""State of the transaction address."""

    country: Optional[CountryCodeEnum] = None

    postal_code: Optional[str] = None
    r"""Postal code of the transaction."""

    tax_id: Optional[str] = None
    r"""Tax ID associated with the transaction"""

    address_status: Optional[AddressStatus] = None

    processing_status: Optional[ProcessingStatusEnum] = None
    r"""Our transaction state, used to determine when/if a transaction needs additional
    processing.
    """

    destination_currency: Optional[CurrencyEnum] = None

    converted_total_amount: Optional[str] = None
    r"""Converted total amount."""

    converted_total_tax_amount_imported: Optional[str] = None
    r"""Converted imported tax amount."""

    converted_total_tax_amount_calculated: Optional[str] = None
    r"""Converted calculated tax amount."""

    conversion_rate: Optional[str] = None
    r"""Currency conversion rate."""

    converted_taxable_amount: Optional[str] = None
    r"""Converted taxable amount."""

    converted_total_discount: Optional[str] = None
    r"""Converted total discount amount."""

    converted_subtotal: Optional[str] = None
    r"""Converted subtotal amount."""

    converted_total_tax_liability_amount: Optional[str] = None
    r"""Converted total tax liability amount."""

    customer: Optional[CustomerRead] = None

    total_discount: Optional[str] = None
    r"""Total amount of all discounts applied to the transaction."""

    subtotal: Optional[str] = None
    r"""Subtotal amount before any discounts are applied."""

    final_total_amount: Optional[str] = None
    r"""Final total amount including tax liability."""

    converted_final_total_amount: Optional[str] = None
    r"""Converted final total amount including tax liability."""
