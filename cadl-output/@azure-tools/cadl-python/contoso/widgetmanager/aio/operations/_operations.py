# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._model_base import _deserialize
from ...operations._operations import (
    build_list_as_acore_resource_list_core_resource_list_request,
    build_list_as_afoundation_operation_foundations_operation_list_request,
    build_list_as_afoundation_resource_list_foundations_resource_list_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ListAsAFoundationOperationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~contoso.widgetmanager.aio.WidgetManagerClient`'s
        :attr:`list_as_afoundation_operation` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def foundations_operation_list(
        self,
        *,
        maxresults: Optional[int] = None,
        time_out: Optional[int] = None,
        client_request_id: Optional[str] = None,
        return_client_request_id: Optional[bool] = None,
        ocp_date: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ApplicationListResult:
        """Lists all of the applications available in the specified Account.

        This operation returns only Applications and versions that are available for
        use on Compute Nodes; that is, that can be used in an Package reference. For
        administrator information about applications and versions that are not yet
        available to Compute Nodes, use the Azure portal or the Azure Resource Manager
        API.

        :keyword maxresults: The maximum number of items to return in the response. A maximum of 1000
         applications can be returned. Default value is None.
        :paramtype maxresults: int
        :keyword time_out: The maximum number of items to return in the response. A maximum of 1000
         applications can be returned. Default value is None.
        :paramtype time_out: int
        :keyword client_request_id: The caller-generated request identity, in the form of a GUID with
         no decoration
         such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. Default value is None.
        :paramtype client_request_id: str
        :keyword return_client_request_id: Whether the server should return the client-request-id in
         the response. Default value is None.
        :paramtype return_client_request_id: bool
        :keyword ocp_date: The time the request was issued. Client libraries typically set this to the
         current system clock time; set it explicitly if you are calling the REST API
         directly. Default value is None.
        :paramtype ocp_date: str
        :return: ApplicationListResult. The ApplicationListResult is compatible with MutableMapping
        :rtype: ~contoso.widgetmanager.models.ApplicationListResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.ApplicationListResult] = kwargs.pop("cls", None)

        request = build_list_as_afoundation_operation_foundations_operation_list_request(
            api_version=self._config.api_version,
            maxresults=maxresults,
            time_out=time_out,
            client_request_id=client_request_id,
            return_client_request_id=return_client_request_id,
            ocp_date=ocp_date,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["etag"] = self._deserialize("str", response.headers.get("etag"))
        response_headers["last-modified"] = self._deserialize("str", response.headers.get("last-modified"))
        response_headers["client-request-id"] = self._deserialize("str", response.headers.get("client-request-id"))
        response_headers["request-id"] = self._deserialize("str", response.headers.get("request-id"))

        deserialized = _deserialize(_models.ApplicationListResult, response.json())

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore


class ListAsAFoundationResourceListOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~contoso.widgetmanager.aio.WidgetManagerClient`'s
        :attr:`list_as_afoundation_resource_list` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def foundations_resource_list(
        self,
        *,
        maxresults: Optional[int] = None,
        time_out: Optional[int] = None,
        client_request_id: Optional[str] = None,
        return_client_request_id: Optional[bool] = None,
        ocp_date: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ApplicationListResult:
        """Lists all of the applications available in the specified Account.

        This operation returns only Applications and versions that are available for
        use on Compute Nodes; that is, that can be used in an Package reference. For
        administrator information about applications and versions that are not yet
        available to Compute Nodes, use the Azure portal or the Azure Resource Manager
        API.

        :keyword maxresults: The maximum number of items to return in the response. A maximum of 1000
         applications can be returned. Default value is None.
        :paramtype maxresults: int
        :keyword time_out: The maximum number of items to return in the response. A maximum of 1000
         applications can be returned. Default value is None.
        :paramtype time_out: int
        :keyword client_request_id: The caller-generated request identity, in the form of a GUID with
         no decoration
         such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. Default value is None.
        :paramtype client_request_id: str
        :keyword return_client_request_id: Whether the server should return the client-request-id in
         the response. Default value is None.
        :paramtype return_client_request_id: bool
        :keyword ocp_date: The time the request was issued. Client libraries typically set this to the
         current system clock time; set it explicitly if you are calling the REST API
         directly. Default value is None.
        :paramtype ocp_date: str
        :return: ApplicationListResult. The ApplicationListResult is compatible with MutableMapping
        :rtype: ~contoso.widgetmanager.models.ApplicationListResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.ApplicationListResult] = kwargs.pop("cls", None)

        request = build_list_as_afoundation_resource_list_foundations_resource_list_request(
            api_version=self._config.api_version,
            maxresults=maxresults,
            time_out=time_out,
            client_request_id=client_request_id,
            return_client_request_id=return_client_request_id,
            ocp_date=ocp_date,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["etag"] = self._deserialize("str", response.headers.get("etag"))
        response_headers["last-modified"] = self._deserialize("str", response.headers.get("last-modified"))
        response_headers["client-request-id"] = self._deserialize("str", response.headers.get("client-request-id"))
        response_headers["request-id"] = self._deserialize("str", response.headers.get("request-id"))

        deserialized = _deserialize(_models.ApplicationListResult, response.json())

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore


class ListAsACoreResourceListOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~contoso.widgetmanager.aio.WidgetManagerClient`'s
        :attr:`list_as_acore_resource_list` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def core_resource_list(self, **kwargs: Any) -> AsyncIterable["_models.Application2"]:
        """Lists all of the applications available in the specified Account.

        This operation returns only Applications and versions that are available for
        use on Compute Nodes; that is, that can be used in an Package reference. For
        administrator information about applications and versions that are not yet
        available to Compute Nodes, use the Azure portal or the Azure Resource Manager
        API.

        :return: An iterator like instance of Application2. The Application2 is compatible with
         MutableMapping
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~contoso.widgetmanager.models.Application2]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models._models.CustomPageApplication2] = kwargs.pop(
            "cls", None
        )  # pylint: disable=protected-access

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_as_acore_resource_list_core_resource_list_request(
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                request.url = self._client.format_url(request.url)

            else:
                request = HttpRequest("GET", next_link)
                request.url = self._client.format_url(request.url)

            return request

        async def extract_data(pipeline_response):
            deserialized: _models._models.CustomPageApplication2 = _deserialize(  # pylint: disable=protected-access
                _models._models.CustomPageApplication2, pipeline_response  # pylint: disable=protected-access
            )
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)
