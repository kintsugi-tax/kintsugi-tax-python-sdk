"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .productcategoryenum import ProductCategoryEnum
from .productsubcategoryenum import ProductSubCategoryEnum
from .sourceenum import SourceEnum
from datetime import datetime
from kintsugi_tax_platform_sdk.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TransactionItemEstimateBaseTypedDict(TypedDict):
    date_: datetime
    r"""The date of the transaction item."""
    amount: float
    r"""The total amount of the item."""
    external_id: NotRequired[str]
    r"""A unique identifier for the transaction item."""
    description: NotRequired[str]
    r"""A description of the item."""
    external_product_id: NotRequired[str]
    r"""External product identifier. If not found and product_subcategory
    and product_category are not provided, an error occurs.
    """
    product_name: NotRequired[str]
    r"""Name of the product. Used if creating a new product."""
    product_description: NotRequired[str]
    r"""Description of the product. Used if creating a new product."""
    product_source: NotRequired[SourceEnum]
    product_subcategory: NotRequired[ProductSubCategoryEnum]
    product_category: NotRequired[ProductCategoryEnum]
    quantity: NotRequired[float]
    r"""Defaults to 1.0. The quantity of the item."""
    exempt: NotRequired[bool]
    r"""Defaults to false. Indicates whether the item is exempt from tax."""


class TransactionItemEstimateBase(BaseModel):
    date_: Annotated[datetime, pydantic.Field(alias="date")]
    r"""The date of the transaction item."""

    amount: float
    r"""The total amount of the item."""

    external_id: Optional[str] = None
    r"""A unique identifier for the transaction item."""

    description: Optional[str] = None
    r"""A description of the item."""

    external_product_id: Optional[str] = None
    r"""External product identifier. If not found and product_subcategory
    and product_category are not provided, an error occurs.
    """

    product_name: Optional[str] = None
    r"""Name of the product. Used if creating a new product."""

    product_description: Optional[str] = None
    r"""Description of the product. Used if creating a new product."""

    product_source: Optional[SourceEnum] = None

    product_subcategory: Optional[ProductSubCategoryEnum] = None

    product_category: Optional[ProductCategoryEnum] = None

    quantity: Optional[float] = 1.0
    r"""Defaults to 1.0. The quantity of the item."""

    exempt: Optional[bool] = False
    r"""Defaults to false. Indicates whether the item is exempt from tax."""
