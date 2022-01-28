# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._restorable_table_resources_operations import build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class RestorableTableResourcesOperations:
    """RestorableTableResourcesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.cosmosdb.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def list(
        self,
        location: str,
        instance_id: str,
        restore_location: Optional[str] = None,
        restore_timestamp_in_utc: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.RestorableTableResourcesGetResult":
        """Return a list of tables that exist on the account at the given timestamp and location. This
        helps in scenarios to validate what resources exist at given timestamp and location. This API
        requires 'Microsoft.DocumentDB/locations/restorableDatabaseAccounts/.../read' permission.

        :param location: Cosmos DB region, with spaces between words and each word capitalized.
        :type location: str
        :param instance_id: The instanceId GUID of a restorable database account.
        :type instance_id: str
        :param restore_location: The location where the restorable resources are located.
        :type restore_location: str
        :param restore_timestamp_in_utc: The timestamp when the restorable resources existed.
        :type restore_timestamp_in_utc: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RestorableTableResourcesGetResult, or the result of cls(response)
        :rtype: ~azure.mgmt.cosmosdb.models.RestorableTableResourcesGetResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RestorableTableResourcesGetResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_list_request(
            subscription_id=self._config.subscription_id,
            location=location,
            instance_id=instance_id,
            restore_location=restore_location,
            restore_timestamp_in_utc=restore_timestamp_in_utc,
            template_url=self.list.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('RestorableTableResourcesGetResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DocumentDB/locations/{location}/restorableDatabaseAccounts/{instanceId}/restorableTableResources'}  # type: ignore

