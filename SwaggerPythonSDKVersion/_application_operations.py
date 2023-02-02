# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    *,
    max_results: int = 1000,
    timeout: int = 30,
    client_request_id: Optional[str] = None,
    return_client_request_id: bool = False,
    ocp_date: Optional[datetime.datetime] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-01-01.15.0"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/applications")

    # Construct parameters
    if max_results is not None:
        _params["maxresults"] = _SERIALIZER.query("max_results", max_results, "int", maximum=1000, minimum=1)
    if timeout is not None:
        _params["timeout"] = _SERIALIZER.query("timeout", timeout, "int")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if client_request_id is not None:
        _headers["client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    if return_client_request_id is not None:
        _headers["return-client-request-id"] = _SERIALIZER.header(
            "return_client_request_id", return_client_request_id, "bool"
        )
    if ocp_date is not None:
        _headers["ocp-date"] = _SERIALIZER.header("ocp_date", ocp_date, "rfc-1123")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    application_id: str,
    *,
    timeout: int = 30,
    client_request_id: Optional[str] = None,
    return_client_request_id: bool = False,
    ocp_date: Optional[datetime.datetime] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-01-01.15.0"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/applications/{applicationId}")
    path_format_arguments = {
        "applicationId": _SERIALIZER.url("application_id", application_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if timeout is not None:
        _params["timeout"] = _SERIALIZER.query("timeout", timeout, "int")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if client_request_id is not None:
        _headers["client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    if return_client_request_id is not None:
        _headers["return-client-request-id"] = _SERIALIZER.header(
            "return_client_request_id", return_client_request_id, "bool"
        )
    if ocp_date is not None:
        _headers["ocp-date"] = _SERIALIZER.header("ocp_date", ocp_date, "rfc-1123")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class ApplicationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure-batch.BatchServiceClient`'s
        :attr:`application` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self, application_list_options: Optional[_models.ApplicationListOptions] = None, **kwargs: Any
    ) -> Iterable["_models.Application"]:
        """Lists all of the applications available in the specified Account.

        This operation returns only Applications and versions that are available for use on Compute
        Nodes; that is, that can be used in an Package reference. For administrator information about
        applications and versions that are not yet available to Compute Nodes, use the Azure portal or
        the Azure Resource Manager API.

        :param application_list_options: Parameter group. Default value is None.
        :type application_list_options: ~azure-batch.models.ApplicationListOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Application or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure-batch.models.Application]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ApplicationListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:
                _max_results = None
                _timeout = None
                _client_request_id = None
                _return_client_request_id = None
                _ocp_date = None
                if application_list_options is not None:
                    _client_request_id = application_list_options.client_request_id
                    _max_results = application_list_options.max_results
                    _ocp_date = application_list_options.ocp_date
                    _return_client_request_id = application_list_options.return_client_request_id
                    _timeout = application_list_options.timeout

                request = build_list_request(
                    max_results=_max_results,
                    timeout=_timeout,
                    client_request_id=_client_request_id,
                    return_client_request_id=_return_client_request_id,
                    ocp_date=_ocp_date,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "batchUrl": self._serialize.url(
                        "self._config.batch_url", self._config.batch_url, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "batchUrl": self._serialize.url(
                        "self._config.batch_url", self._config.batch_url, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ApplicationListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.BatchError, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {"url": "/applications"}  # type: ignore

    @distributed_trace
    def get(
        self,
        application_id: str,
        application_get_options: Optional[_models.ApplicationGetOptions] = None,
        **kwargs: Any
    ) -> _models.Application:
        """Gets information about the specified Application.

        This operation returns only Applications and versions that are available for use on Compute
        Nodes; that is, that can be used in an Package reference. For administrator information about
        Applications and versions that are not yet available to Compute Nodes, use the Azure portal or
        the Azure Resource Manager API.

        :param application_id: The ID of the Application. Required.
        :type application_id: str
        :param application_get_options: Parameter group. Default value is None.
        :type application_get_options: ~azure-batch.models.ApplicationGetOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Application or the result of cls(response)
        :rtype: ~azure-batch.models.Application
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
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Application]

        _timeout = None
        _client_request_id = None
        _return_client_request_id = None
        _ocp_date = None
        if application_get_options is not None:
            _client_request_id = application_get_options.client_request_id
            _ocp_date = application_get_options.ocp_date
            _return_client_request_id = application_get_options.return_client_request_id
            _timeout = application_get_options.timeout

        request = build_get_request(
            application_id=application_id,
            timeout=_timeout,
            client_request_id=_client_request_id,
            return_client_request_id=_return_client_request_id,
            ocp_date=_ocp_date,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "batchUrl": self._serialize.url("self._config.batch_url", self._config.batch_url, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.BatchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["client-request-id"] = self._deserialize("str", response.headers.get("client-request-id"))
        response_headers["request-id"] = self._deserialize("str", response.headers.get("request-id"))
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))
        response_headers["Last-Modified"] = self._deserialize("rfc-1123", response.headers.get("Last-Modified"))

        deserialized = self._deserialize("Application", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get.metadata = {"url": "/applications/{applicationId}"}  # type: ignore
