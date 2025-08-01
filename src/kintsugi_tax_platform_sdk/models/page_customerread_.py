"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customerread import CustomerRead, CustomerReadTypedDict
from kintsugi_tax_platform_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PageCustomerReadTypedDict(TypedDict):
    items: List[CustomerReadTypedDict]
    total: int
    page: int
    size: int
    pages: NotRequired[int]


class PageCustomerRead(BaseModel):
    items: List[CustomerRead]

    total: int

    page: int

    size: int

    pages: Optional[int] = None
