"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .countrycodeenum import CountryCodeEnum
from kintsugi_tax_platform_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AddressBaseTypedDict(TypedDict):
    phone: NotRequired[str]
    r"""Phone number associated with the address."""
    street_1: NotRequired[str]
    r"""Primary street address."""
    street_2: NotRequired[str]
    r"""Additional street address details, such as an apartment or suite number."""
    city: NotRequired[str]
    r"""City where the customer resides."""
    county: NotRequired[str]
    r"""County or district of the customer."""
    state: NotRequired[str]
    r"""State or province of the customer."""
    postal_code: NotRequired[str]
    r"""ZIP or Postal code of the customer."""
    country: NotRequired[CountryCodeEnum]
    full_address: NotRequired[str]
    r"""Complete address string of the customer, which can be used as an alternative to individual fields."""


class AddressBase(BaseModel):
    phone: Optional[str] = None
    r"""Phone number associated with the address."""

    street_1: Optional[str] = None
    r"""Primary street address."""

    street_2: Optional[str] = None
    r"""Additional street address details, such as an apartment or suite number."""

    city: Optional[str] = None
    r"""City where the customer resides."""

    county: Optional[str] = None
    r"""County or district of the customer."""

    state: Optional[str] = None
    r"""State or province of the customer."""

    postal_code: Optional[str] = None
    r"""ZIP or Postal code of the customer."""

    country: Optional[CountryCodeEnum] = None

    full_address: Optional[str] = None
    r"""Complete address string of the customer, which can be used as an alternative to individual fields."""
