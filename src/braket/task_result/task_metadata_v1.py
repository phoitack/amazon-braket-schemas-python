# Copyright 2019-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License

from typing import Any, Dict, Optional

from pydantic import Field, conint, constr

from braket.schema_common import BraketSchemaBase, BraketSchemaHeader


class TaskMetadata(BraketSchemaBase):
    """
    The task metadata schema.

    Attributes:
        braketSchemaHeader (BraketSchemaHeader): Schema header. Users do not need
            to set this value. Only default is allowed.
        id (str): The ID of the task. For AWS tasks, this is the task ARN.
        shots (str): The number of shots for the task
        deviceId (str): The ID of the device on which the task ran.
            For AWS devices, this is the device ARN.
        deviceParameters (Dict[str, Any]): The device parameters of the task. Default is None.
            # TODO: replace with device schema
        createdAt (str): The timestamp of creation;
            the format must be in ISO-8601/RFC3339 string format YYYY-MM-DDTHH:mm:ss.sssZ.
            Default is None.
        endedAt (str): The timestamp of when the task ended;
            the format must be in ISO-8601/RFC3339 string format YYYY-MM-DDTHH:mm:ss.sssZ.
            Default is None.
        status (str): The status of the task. Default is None.
        failureReason (str): The failure reason of the task. Default is None.

    Examples:
        >>> TaskMetadata(id="task_id", shots=100, deviceId="device_id")

    """

    _TASK_METADATA_HEADER = BraketSchemaHeader(name="braket.task_result.task_metadata", version="1")

    braketSchemaHeader: BraketSchemaHeader = Field(
        default=_TASK_METADATA_HEADER, const=_TASK_METADATA_HEADER
    )
    id: constr(min_length=1)
    shots: conint(ge=0)
    deviceId: constr(min_length=1)
    deviceParameters: Optional[Dict[str, Any]]  # TODO: replace with device schema
    createdAt: Optional[constr(min_length=1, max_length=24)]
    endedAt: Optional[constr(min_length=1, max_length=24)]
    status: Optional[constr(min_length=1, max_length=20)]
    failureReason: Optional[constr(min_length=1)]