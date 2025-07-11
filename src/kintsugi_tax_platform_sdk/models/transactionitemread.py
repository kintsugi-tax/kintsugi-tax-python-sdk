"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .currencyenum import CurrencyEnum
from .taxexemptionenum import TaxExemptionEnum
from .taxitemread import TaxItemRead, TaxItemReadTypedDict
from datetime import datetime
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


class TransactionItemReadTypedDict(TypedDict):
    organization_id: Nullable[str]
    r"""Organization identifier."""
    date_: datetime
    r"""Date/time of item."""
    external_product_id: str
    r"""External product identifier."""
    id: str
    r"""The unique transaction item identifier."""
    tax_items: List[TaxItemReadTypedDict]
    r"""List of tax items associated with the transaction item."""
    external_id: NotRequired[Nullable[str]]
    r"""External item identifier."""
    description: NotRequired[Nullable[str]]
    r"""Item description"""
    product: NotRequired[Nullable[str]]
    r"""Product name"""
    product_id: NotRequired[Nullable[str]]
    r"""Product identifier."""
    product_name: NotRequired[Nullable[str]]
    r"""Product name (detailed)"""
    product_description: NotRequired[Nullable[str]]
    r"""Product description"""
    quantity: NotRequired[str]
    r"""Quantity of item."""
    amount: NotRequired[str]
    r"""Item amount."""
    tax_amount_imported: NotRequired[str]
    r"""Imported tax amount for the item."""
    tax_rate_imported: NotRequired[str]
    r"""Imported tax rate."""
    tax_amount_calculated: NotRequired[str]
    r"""Calculated tax amount for the item."""
    tax_rate_calculated: NotRequired[str]
    r"""Calculated tax rate."""
    original_currency: NotRequired[Nullable[CurrencyEnum]]
    r"""Original currency code."""
    destination_currency: NotRequired[Nullable[CurrencyEnum]]
    r"""Destination currency code."""
    converted_amount: NotRequired[Nullable[str]]
    r"""Converted item amount."""
    converted_taxable_amount: NotRequired[Nullable[str]]
    r"""Converted taxable amount."""
    converted_tax_amount_imported: NotRequired[Nullable[str]]
    r"""Converted imported tax amount."""
    converted_tax_amount_calculated: NotRequired[Nullable[str]]
    r"""Converted calculated tax amount"""
    converted_total_discount: NotRequired[Nullable[str]]
    r"""Converted total discount amount."""
    converted_subtotal: NotRequired[Nullable[str]]
    r"""Converted subtotal amount."""
    taxable_amount: NotRequired[str]
    r"""Taxable amount for the item."""
    tax_exemption: NotRequired[Nullable[TaxExemptionEnum]]
    r"""Tax exemption status."""
    exempt: NotRequired[bool]
    r"""Indicates if the item is exempt."""
    total_discount: NotRequired[Nullable[str]]
    r"""Total discount amount applied to this transaction item."""
    subtotal: NotRequired[Nullable[str]]
    r"""Subtotal amount before any discount is applied."""


class TransactionItemRead(BaseModel):
    organization_id: Nullable[str]
    r"""Organization identifier."""

    date_: Annotated[datetime, pydantic.Field(alias="date")]
    r"""Date/time of item."""

    external_product_id: str
    r"""External product identifier."""

    id: str
    r"""The unique transaction item identifier."""

    tax_items: List[TaxItemRead]
    r"""List of tax items associated with the transaction item."""

    external_id: OptionalNullable[str] = UNSET
    r"""External item identifier."""

    description: OptionalNullable[str] = UNSET
    r"""Item description"""

    product: OptionalNullable[str] = UNSET
    r"""Product name"""

    product_id: OptionalNullable[str] = UNSET
    r"""Product identifier."""

    product_name: OptionalNullable[str] = UNSET
    r"""Product name (detailed)"""

    product_description: OptionalNullable[str] = UNSET
    r"""Product description"""

    quantity: Optional[str] = "1.0"
    r"""Quantity of item."""

    amount: Optional[str] = "0.00"
    r"""Item amount."""

    tax_amount_imported: Optional[str] = "0.00"
    r"""Imported tax amount for the item."""

    tax_rate_imported: Optional[str] = "0.00"
    r"""Imported tax rate."""

    tax_amount_calculated: Optional[str] = "0.00"
    r"""Calculated tax amount for the item."""

    tax_rate_calculated: Optional[str] = "0.00"
    r"""Calculated tax rate."""

    original_currency: OptionalNullable[CurrencyEnum] = UNSET
    r"""Original currency code."""

    destination_currency: OptionalNullable[CurrencyEnum] = UNSET
    r"""Destination currency code."""

    converted_amount: OptionalNullable[str] = UNSET
    r"""Converted item amount."""

    converted_taxable_amount: OptionalNullable[str] = UNSET
    r"""Converted taxable amount."""

    converted_tax_amount_imported: OptionalNullable[str] = UNSET
    r"""Converted imported tax amount."""

    converted_tax_amount_calculated: OptionalNullable[str] = UNSET
    r"""Converted calculated tax amount"""

    converted_total_discount: OptionalNullable[str] = UNSET
    r"""Converted total discount amount."""

    converted_subtotal: OptionalNullable[str] = UNSET
    r"""Converted subtotal amount."""

    taxable_amount: Optional[str] = "0.00"
    r"""Taxable amount for the item."""

    tax_exemption: OptionalNullable[TaxExemptionEnum] = UNSET
    r"""Tax exemption status."""

    exempt: Optional[bool] = False
    r"""Indicates if the item is exempt."""

    total_discount: OptionalNullable[str] = UNSET
    r"""Total discount amount applied to this transaction item."""

    subtotal: OptionalNullable[str] = UNSET
    r"""Subtotal amount before any discount is applied."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "external_id",
            "description",
            "product",
            "product_id",
            "product_name",
            "product_description",
            "quantity",
            "amount",
            "tax_amount_imported",
            "tax_rate_imported",
            "tax_amount_calculated",
            "tax_rate_calculated",
            "original_currency",
            "destination_currency",
            "converted_amount",
            "converted_taxable_amount",
            "converted_tax_amount_imported",
            "converted_tax_amount_calculated",
            "converted_total_discount",
            "converted_subtotal",
            "taxable_amount",
            "tax_exemption",
            "exempt",
            "total_discount",
            "subtotal",
        ]
        nullable_fields = [
            "external_id",
            "organization_id",
            "description",
            "product",
            "product_id",
            "product_name",
            "product_description",
            "original_currency",
            "destination_currency",
            "converted_amount",
            "converted_taxable_amount",
            "converted_tax_amount_imported",
            "converted_tax_amount_calculated",
            "converted_total_discount",
            "converted_subtotal",
            "tax_exemption",
            "total_discount",
            "subtotal",
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
