"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .taxexemptionenum import TaxExemptionEnum
from .taxitembuilder import TaxItemBuilder, TaxItemBuilderTypedDict
from datetime import datetime
from kintsugi_tax_platform_sdk.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreditNoteItemCreateUpdateTypedDict(TypedDict):
    external_id: str
    r"""Unique identifier for the credit note item in the external system."""
    date_: datetime
    r"""Date when the credit note item was issued or created."""
    external_product_id: str
    r"""Unique identifier for the associated product in the external system."""
    description: NotRequired[str]
    r"""Brief explanation or details about the credit note item."""
    quantity: NotRequired[float]
    r"""Number of units or amount of the product being credited."""
    amount: NotRequired[float]
    r"""Total monetary value of the credit note item before taxes."""
    tax_amount_imported: NotRequired[float]
    r"""Pre-calculated tax amount for the item, if provided by the external system."""
    tax_rate_imported: NotRequired[float]
    r"""Pre-calculated tax rate for the item, if provided by the external system."""
    taxable_amount: NotRequired[float]
    r"""Portion of the item amount subject to taxation."""
    tax_exemption: NotRequired[TaxExemptionEnum]
    r"""This enum is used to determine if a transaction is exempt from tax."""
    tax_items: NotRequired[List[TaxItemBuilderTypedDict]]
    r"""Detailed breakdown of individual tax components applied to this item."""


class CreditNoteItemCreateUpdate(BaseModel):
    external_id: str
    r"""Unique identifier for the credit note item in the external system."""

    date_: Annotated[datetime, pydantic.Field(alias="date")]
    r"""Date when the credit note item was issued or created."""

    external_product_id: str
    r"""Unique identifier for the associated product in the external system."""

    description: Optional[str] = None
    r"""Brief explanation or details about the credit note item."""

    quantity: Optional[float] = 1.0
    r"""Number of units or amount of the product being credited."""

    amount: Optional[float] = 0.00
    r"""Total monetary value of the credit note item before taxes."""

    tax_amount_imported: Optional[float] = None
    r"""Pre-calculated tax amount for the item, if provided by the external system."""

    tax_rate_imported: Optional[float] = None
    r"""Pre-calculated tax rate for the item, if provided by the external system."""

    taxable_amount: Optional[float] = None
    r"""Portion of the item amount subject to taxation."""

    tax_exemption: Optional[TaxExemptionEnum] = None
    r"""This enum is used to determine if a transaction is exempt from tax."""

    tax_items: Optional[List[TaxItemBuilder]] = None
    r"""Detailed breakdown of individual tax components applied to this item."""
