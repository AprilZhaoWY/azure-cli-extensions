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

from msrest.serialization import Model


class NsRecord(Model):
    """An NS record.

    :param nsdname: The name server name for this NS record.
    :type nsdname: str
    """

    _attribute_map = {
        'nsdname': {'key': 'nsdname', 'type': 'str'},
    }

    def __init__(self, nsdname=None):
        super(NsRecord, self).__init__()
        self.nsdname = nsdname
