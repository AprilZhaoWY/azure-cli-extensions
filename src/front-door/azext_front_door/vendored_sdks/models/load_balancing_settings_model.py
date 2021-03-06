# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class LoadBalancingSettingsModel(SubResource):
    """Load balancing settings for a backend pool.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param sample_size: The number of samples to consider for load balancing
     decisions
    :type sample_size: int
    :param successful_samples_required: The number of samples within the
     sample period that must succeed
    :type successful_samples_required: int
    :param additional_latency_milliseconds: The additional latency in
     milliseconds for probes to fall into the lowest latency bucket
    :type additional_latency_milliseconds: int
    :param resource_state: Resource status. Possible values include:
     'Creating', 'Enabling', 'Enabled', 'Disabling', 'Disabled', 'Deleting'
    :type resource_state: str or
     ~azure.mgmt.frontdoor.models.FrontDoorResourceState
    :param name: Resource name.
    :type name: str
    :ivar type: Resource type.
    :vartype type: str
    """

    _validation = {
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'sample_size': {'key': 'properties.sampleSize', 'type': 'int'},
        'successful_samples_required': {'key': 'properties.successfulSamplesRequired', 'type': 'int'},
        'additional_latency_milliseconds': {'key': 'properties.additionalLatencyMilliseconds', 'type': 'int'},
        'resource_state': {'key': 'properties.resourceState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LoadBalancingSettingsModel, self).__init__(**kwargs)
        self.sample_size = kwargs.get('sample_size', None)
        self.successful_samples_required = kwargs.get('successful_samples_required', None)
        self.additional_latency_milliseconds = kwargs.get('additional_latency_milliseconds', None)
        self.resource_state = kwargs.get('resource_state', None)
        self.name = kwargs.get('name', None)
        self.type = None
