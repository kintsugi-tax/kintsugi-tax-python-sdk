"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class TransactionExemptStatusEnum(str, Enum):
    r"""Based on transaction item exempt status.
    NOT EXEMPT: None of the items are NOT EXEMPT
    PARTIALLY EXEMPT: At least some of the items are NOT EXEMPT
    FULLY_EXEMPT: All items sold in the transaction are EXEMPT
    """

    NOT_EXEMPT = "NOT_EXEMPT"
    PARTIALLY_EXEMPT = "PARTIALLY_EXEMPT"
    FULLY_EXEMPT = "FULLY_EXEMPT"
