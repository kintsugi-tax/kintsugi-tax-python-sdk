"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .countrycodeenum import CountryCodeEnum
from .transactionstatusenum import TransactionStatusEnum
from kintsugi_tax_platform_sdk.types import BaseModel
from kintsugi_tax_platform_sdk.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetTransactionsV1TransactionsGetRequestTypedDict(TypedDict):
    state_code: NotRequired[str]
    r"""Filter transactions by state code."""
    transaction_type: NotRequired[str]
    r"""Filter by transaction type (e.g., SALE, FULL_CREDIT_NOTE,
    PARTIAL_CREDIT_NOTE, ARCHIVE etc.).
    """
    transaction_source: NotRequired[str]
    r"""Filter transactions based on the source."""
    search_query: NotRequired[str]
    r"""Search for transactions using a general query
    (e.g., order ID, customer name).
    """
    country: NotRequired[List[CountryCodeEnum]]
    r"""Filter transactions by country code
    (ISO 3166-1 alpha-2 format, e.g., US).
    """
    state: NotRequired[str]
    r"""Filter by full state name (e.g., California)."""
    address_status_in: NotRequired[str]
    r"""Filter by address status (e.g., UNVERIFIED, INVALID,
    PARTIALLY_VERIFIED, VERIFIED, UNVERIFIABLE).
    """
    status: NotRequired[TransactionStatusEnum]
    r"""Filter by transaction status (e.g., PENDING, COMMITTED,
    CANCELLED, FULLY_REFUNDED, PARTIALLY_REFUNDED, ARCHIVED).
    """
    filing_id: NotRequired[str]
    r"""Retrieve transactions linked to a specific filing ID."""
    order_by: NotRequired[str]
    r"""Sort results based on specified fields.
    Prefix with - for descending order (e.g., -date for newest first).
    """
    date_gte: NotRequired[str]
    r"""Retrieve transactions with a date
    greater than or equal to (YYYY-MM-DD).
    """
    date_lte: NotRequired[str]
    r"""Retrieve transactions with a date
    less than or equal to (YYYY-MM-DD).
    """
    processing_status_in: NotRequired[str]
    r"""Filter transactions based on processing status.
    Multiple values can be passed as a comma-separated list.
    """
    marketplace: NotRequired[bool]
    r"""Filter transactions by marketplace (e.g., AMAZON, EBAY)."""
    exempt_in: NotRequired[str]
    r"""Filter transactions by exemption status.
    Multiple values can be passed as a comma-separated list (e.g., EXEMPT,TAXABLE).
    """
    page: NotRequired[int]
    r"""Page number"""
    size: NotRequired[int]
    r"""Page size"""


class GetTransactionsV1TransactionsGetRequest(BaseModel):
    state_code: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter transactions by state code."""

    transaction_type: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by transaction type (e.g., SALE, FULL_CREDIT_NOTE,
    PARTIAL_CREDIT_NOTE, ARCHIVE etc.).
    """

    transaction_source: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter transactions based on the source."""

    search_query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Search for transactions using a general query
    (e.g., order ID, customer name).
    """

    country: Annotated[
        Optional[List[CountryCodeEnum]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter transactions by country code
    (ISO 3166-1 alpha-2 format, e.g., US).
    """

    state: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by full state name (e.g., California)."""

    address_status_in: Annotated[
        Optional[str],
        pydantic.Field(alias="address_status__in"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "UNVERIFIED,INVALID,PARTIALLY_VERIFIED,VERIFIED,UNVERIFIABLE"
    r"""Filter by address status (e.g., UNVERIFIED, INVALID,
    PARTIALLY_VERIFIED, VERIFIED, UNVERIFIABLE).
    """

    status: Annotated[
        Optional[TransactionStatusEnum],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by transaction status (e.g., PENDING, COMMITTED,
    CANCELLED, FULLY_REFUNDED, PARTIALLY_REFUNDED, ARCHIVED).
    """

    filing_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Retrieve transactions linked to a specific filing ID."""

    order_by: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "date,state,customer_name,status"
    r"""Sort results based on specified fields.
    Prefix with - for descending order (e.g., -date for newest first).
    """

    date_gte: Annotated[
        Optional[str],
        pydantic.Field(alias="date__gte"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Retrieve transactions with a date
    greater than or equal to (YYYY-MM-DD).
    """

    date_lte: Annotated[
        Optional[str],
        pydantic.Field(alias="date__lte"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Retrieve transactions with a date
    less than or equal to (YYYY-MM-DD).
    """

    processing_status_in: Annotated[
        Optional[str],
        pydantic.Field(alias="processing_status__in"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter transactions based on processing status.
    Multiple values can be passed as a comma-separated list.
    """

    marketplace: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter transactions by marketplace (e.g., AMAZON, EBAY)."""

    exempt_in: Annotated[
        Optional[str],
        pydantic.Field(alias="exempt__in"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter transactions by exemption status.
    Multiple values can be passed as a comma-separated list (e.g., EXEMPT,TAXABLE).
    """

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
