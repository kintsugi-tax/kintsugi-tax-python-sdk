"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .countrycodeenum import CountryCodeEnum
from .exemptionstatus import ExemptionStatus
from .exemptiontype import ExemptionType
from datetime import date
from kintsugi_tax_platform_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ExemptionCreateTypedDict(TypedDict):
    exemption_type: ExemptionType
    start_date: date
    r"""Start date for the exemption validity period (YYYY-MM-DD format)"""
    customer_id: str
    r"""Unique identifier for the customer associated with the exemption"""
    fein: str
    r"""Federal Employer Identification Number"""
    sales_tax_id: str
    r"""Sales tax ID for the exemption"""
    status: ExemptionStatus
    jurisdiction: NotRequired[Nullable[str]]
    r"""The jurisdiction identifier for the exemption"""
    country_code: NotRequired[Nullable[CountryCodeEnum]]
    r"""Country code in ISO 3166-1 alpha-2 format (e.g., 'US')"""
    end_date: NotRequired[Nullable[date]]
    r"""End date for the exemption validity period (YYYY-MM-DD format)"""
    transaction_id: NotRequired[Nullable[str]]
    r"""Unique identifier for the transaction, if applicable"""
    reseller: NotRequired[bool]
    r"""Indicates whether the exemption is for a reseller"""


class ExemptionCreate(BaseModel):
    exemption_type: ExemptionType

    start_date: date
    r"""Start date for the exemption validity period (YYYY-MM-DD format)"""

    customer_id: str
    r"""Unique identifier for the customer associated with the exemption"""

    fein: Annotated[str, pydantic.Field(alias="FEIN")]
    r"""Federal Employer Identification Number"""

    sales_tax_id: str
    r"""Sales tax ID for the exemption"""

    status: ExemptionStatus

    jurisdiction: OptionalNullable[str] = UNSET
    r"""The jurisdiction identifier for the exemption"""

    country_code: OptionalNullable[CountryCodeEnum] = UNSET
    r"""Country code in ISO 3166-1 alpha-2 format (e.g., 'US')"""

    end_date: OptionalNullable[date] = UNSET
    r"""End date for the exemption validity period (YYYY-MM-DD format)"""

    transaction_id: OptionalNullable[str] = UNSET
    r"""Unique identifier for the transaction, if applicable"""

    reseller: Optional[bool] = False
    r"""Indicates whether the exemption is for a reseller"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "jurisdiction",
            "country_code",
            "end_date",
            "transaction_id",
            "reseller",
        ]
        nullable_fields = ["jurisdiction", "country_code", "end_date", "transaction_id"]
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
