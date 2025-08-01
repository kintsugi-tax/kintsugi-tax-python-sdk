"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from kintsugi_tax_platform_sdk.types import BaseModel
from typing import Any, Dict, List
from typing_extensions import TypedDict


class BackendSrcAddressValidationResponsesValidationErrorItemTypedDict(TypedDict):
    type: str
    r"""Type of validation error"""
    loc: List[str]
    r"""Location of error"""
    msg: str
    r"""Error message"""
    input: Any
    r"""Invalid input value"""
    ctx: Dict[str, Any]
    r"""Additional context"""


class BackendSrcAddressValidationResponsesValidationErrorItem(BaseModel):
    type: str
    r"""Type of validation error"""

    loc: List[str]
    r"""Location of error"""

    msg: str
    r"""Error message"""

    input: Any
    r"""Invalid input value"""

    ctx: Dict[str, Any]
    r"""Additional context"""
