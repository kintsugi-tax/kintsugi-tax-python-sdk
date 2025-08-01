"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import io
from kintsugi_tax_platform_sdk.types import BaseModel
from kintsugi_tax_platform_sdk.utils import FieldMetadata, MultipartFormMetadata
import pydantic
from typing import IO, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class FileTypedDict(TypedDict):
    file_name: str
    content: Union[bytes, IO[bytes], io.BufferedReader]
    content_type: NotRequired[str]


class File(BaseModel):
    file_name: Annotated[
        str, pydantic.Field(alias="fileName"), FieldMetadata(multipart=True)
    ]

    content: Annotated[
        Union[bytes, IO[bytes], io.BufferedReader],
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(content=True)),
    ]

    content_type: Annotated[
        Optional[str],
        pydantic.Field(alias="Content-Type"),
        FieldMetadata(multipart=True),
    ] = None


class BodyUploadExemptionCertificateV1ExemptionsExemptionIDAttachmentsPostTypedDict(
    TypedDict
):
    file: FileTypedDict
    r"""The file to be uploaded. Supported format: PDF. Max size: 10 MB."""


class BodyUploadExemptionCertificateV1ExemptionsExemptionIDAttachmentsPost(BaseModel):
    file: Annotated[File, FieldMetadata(multipart=MultipartFormMetadata(file=True))]
    r"""The file to be uploaded. Supported format: PDF. Max size: 10 MB."""
