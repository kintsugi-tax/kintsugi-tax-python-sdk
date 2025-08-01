"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .relatedentitytype import RelatedEntityType
from kintsugi_tax_platform_sdk.types import BaseModel
from typing_extensions import TypedDict


class AttachmentReadTypedDict(TypedDict):
    related_entity_id: str
    r"""The unique identifier of the exemption associated
    with the attachment.
    """
    related_entity_type: RelatedEntityType
    id: str
    r"""The unique identifier of the uploaded attachment (attachment ID)."""


class AttachmentRead(BaseModel):
    related_entity_id: str
    r"""The unique identifier of the exemption associated
    with the attachment.
    """

    related_entity_type: RelatedEntityType

    id: str
    r"""The unique identifier of the uploaded attachment (attachment ID)."""
