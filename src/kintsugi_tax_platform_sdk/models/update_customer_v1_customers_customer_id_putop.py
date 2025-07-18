"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customerupdate import CustomerUpdate, CustomerUpdateTypedDict
from kintsugi_tax_platform_sdk.types import BaseModel, Nullable, UNSET_SENTINEL
from kintsugi_tax_platform_sdk.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
    SecurityMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateCustomerV1CustomersCustomerIDPutSecurityTypedDict(TypedDict):
    api_key_header: NotRequired[str]
    http_bearer: NotRequired[str]


class UpdateCustomerV1CustomersCustomerIDPutSecurity(BaseModel):
    api_key_header: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="apiKey",
                sub_type="header",
                field_name="X-API-KEY",
            )
        ),
    ] = None

    http_bearer: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="http",
                sub_type="bearer",
                field_name="Authorization",
            )
        ),
    ] = None


class UpdateCustomerV1CustomersCustomerIDPutRequestTypedDict(TypedDict):
    customer_id: str
    r"""Unique identifier of the customer to be retrieved."""
    x_organization_id: Nullable[str]
    r"""The unique identifier for the organization making the request"""
    customer_update: CustomerUpdateTypedDict


class UpdateCustomerV1CustomersCustomerIDPutRequest(BaseModel):
    customer_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Unique identifier of the customer to be retrieved."""

    x_organization_id: Annotated[
        Nullable[str],
        pydantic.Field(alias="x-organization-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""The unique identifier for the organization making the request"""

    customer_update: Annotated[
        CustomerUpdate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["x-organization-id"]
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
