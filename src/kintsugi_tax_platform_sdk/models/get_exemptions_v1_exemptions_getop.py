"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .countrycodeenum import CountryCodeEnum
from kintsugi_tax_platform_sdk.types import BaseModel
from kintsugi_tax_platform_sdk.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetExemptionsV1ExemptionsGetRequestTypedDict(TypedDict):
    search_query: NotRequired[str]
    r"""Search term to filter exemptions by exemption ID, customer name, or customer email"""
    status_in: NotRequired[str]
    r"""Filter exemptions by their status"""
    country_code: NotRequired[List[CountryCodeEnum]]
    r"""Country code in ISO 3166-1 alpha-2 format"""
    jurisdiction: NotRequired[str]
    r"""Jurisdiction identifier"""
    start_date: NotRequired[str]
    r"""Start date for filtering exemptions"""
    end_date: NotRequired[str]
    r"""End date for filtering exemptions"""
    customer_id: NotRequired[str]
    r"""Customer ID to filter exemptions"""
    transaction_id: NotRequired[str]
    r"""Transaction ID to filter exemptions"""
    order_by: NotRequired[str]
    r"""Fields to sort by (comma-separated)"""
    page: NotRequired[int]
    r"""Page number"""
    size: NotRequired[int]
    r"""Page size"""


class GetExemptionsV1ExemptionsGetRequest(BaseModel):
    search_query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Search term to filter exemptions by exemption ID, customer name, or customer email"""

    status_in: Annotated[
        Optional[str],
        pydantic.Field(alias="status__in"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "ACTIVE,INACTIVE,EXPIRED"
    r"""Filter exemptions by their status"""

    country_code: Annotated[
        Optional[List[CountryCodeEnum]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Country code in ISO 3166-1 alpha-2 format"""

    jurisdiction: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Jurisdiction identifier"""

    start_date: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Start date for filtering exemptions"""

    end_date: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""End date for filtering exemptions"""

    customer_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Customer ID to filter exemptions"""

    transaction_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Transaction ID to filter exemptions"""

    order_by: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "end_date,FEIN,sales_tax_id,status"
    r"""Fields to sort by (comma-separated)"""

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
