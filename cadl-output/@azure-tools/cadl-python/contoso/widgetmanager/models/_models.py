# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Application(_model_base.Model):
    """Contains information about an application in an Azure Batch Account.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: A string that uniquely identifies the application within the Account. Required.
    :vartype id: str
    :ivar display_name: The display name for the application. Required.
    :vartype display_name: str
    :ivar versions: The list of available versions of the application. Required.
    :vartype versions: list[str]
    """

    id: str = rest_field(readonly=True)
    """A string that uniquely identifies the application within the Account. Required. """
    display_name: str = rest_field(name="displayName")
    """The display name for the application. Required. """
    versions: List[str] = rest_field()
    """The list of available versions of the application. Required. """

    @overload
    def __init__(
        self,
        *,
        display_name: str,
        versions: List[str],
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Application2(_model_base.Model):
    """Contains information about an application in an Azure Batch Account.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: A string that uniquely identifies the application within the Account. Required.
    :vartype id: str
    :ivar display_name: The display name for the application. Required.
    :vartype display_name: str
    :ivar versions: The list of available versions of the application. Required.
    :vartype versions: list[str]
    """

    id: str = rest_field(readonly=True)
    """A string that uniquely identifies the application within the Account. Required. """
    display_name: str = rest_field(name="displayName")
    """The display name for the application. Required. """
    versions: List[str] = rest_field()
    """The list of available versions of the application. Required. """

    @overload
    def __init__(
        self,
        *,
        display_name: str,
        versions: List[str],
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ApplicationListResult(_model_base.Model):
    """ApplicationListResult.

    :ivar value: The list of applications available in the Account.
    :vartype value: list[~contoso.widgetmanager.models.Application]
    :ivar odata_next_link: The URL to get the next set of results.
    :vartype odata_next_link: str
    """

    value: Optional[List["_models.Application"]] = rest_field()
    """The list of applications available in the Account. """
    odata_next_link: Optional[str] = rest_field(name="odata.nextLink")
    """The URL to get the next set of results. """

    @overload
    def __init__(
        self,
        *,
        value: Optional[List["_models.Application"]] = None,
        odata_next_link: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CustomPageApplication2(_model_base.Model):
    """Paged collection of Application2 items.

    All required parameters must be populated in order to send to Azure.

    :ivar value: The Application2 items on this page. Required.
    :vartype value: list[~contoso.widgetmanager.models.Application2]
    :ivar next_link: The link to the next page of items.
    :vartype next_link: str
    """

    value: List["_models.Application2"] = rest_field()
    """The Application2 items on this page. Required. """
    next_link: Optional[str] = rest_field(name="nextLink")
    """The link to the next page of items. """
