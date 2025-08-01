"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .countrycodeenum import CountryCodeEnum
from kintsugi_tax_platform_sdk.types import BaseModel
from kintsugi_tax_platform_sdk.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetCustomersV1RequestTypedDict(TypedDict):
    search_query: NotRequired[str]
    r"""Search term to filter customers by name or other details"""
    country: NotRequired[List[CountryCodeEnum]]
    r"""Country code in ISO 3166-1 alpha-2 format (e.g., 'US')"""
    state: NotRequired[str]
    r"""State or province code to filter customers"""
    source_in: NotRequired[str]
    r"""Filter customers by source (comma-separated)"""
    order_by: NotRequired[str]
    r"""Comma-separated list of fields to sort results by."""
    page: NotRequired[int]
    r"""Page number"""
    size: NotRequired[int]
    r"""Page size"""


class GetCustomersV1Request(BaseModel):
    search_query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Search term to filter customers by name or other details"""

    country: Annotated[
        Optional[List[CountryCodeEnum]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Country code in ISO 3166-1 alpha-2 format (e.g., 'US')"""

    state: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""State or province code to filter customers"""

    source_in: Annotated[
        Optional[str],
        pydantic.Field(alias="source__in"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter customers by source (comma-separated)"""

    order_by: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Comma-separated list of fields to sort results by."""

    page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1
    r"""Page number"""

    size: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 50
    r"""Page size"""
