"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .addressresponsedata import AddressResponseData, AddressResponseDataTypedDict
from .addresssubmittedresponse import (
    AddressSubmittedResponse,
    AddressSubmittedResponseTypedDict,
)
from kintsugi_tax_platform_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class AddressSearchResponseTypedDict(TypedDict):
    address_submitted: AddressSubmittedResponseTypedDict
    response_address: AddressResponseDataTypedDict
    verification_status: str
    r"""Indicates if the address was VERIFIED, PARTIALLY_VERIFIED, INVALID, UNVERIFIABLE, BLANK"""
    enrich_fields: List[str]
    r"""List of additional fields added to enrich the address"""


class AddressSearchResponse(BaseModel):
    address_submitted: AddressSubmittedResponse

    response_address: AddressResponseData

    verification_status: str
    r"""Indicates if the address was VERIFIED, PARTIALLY_VERIFIED, INVALID, UNVERIFIABLE, BLANK"""

    enrich_fields: List[str]
    r"""List of additional fields added to enrich the address"""
