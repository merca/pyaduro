"""
Test fixtures for the models tests.
"""
import json

import pytest  # noqa E402 # pylint: disable=import-error


@pytest.fixture(name="connection_obj", scope="module")
def get_connection_obj():
    """Connection fixture"""
    return json.loads(
        """
        {
            "timestamp": "2022-10-14T16:06:22.021852Z",
            "online": false
        }
        """
    )


@pytest.fixture(name="meta_obj", scope="module")
def get_meta_obj():
    """Meta fixture"""
    return json.loads(
        """
        {
            "id": "373371fe-9735-4069-25d6-44a93531a982",
            "type": "device",
            "version": "2.1",
            "owner": "a4e0a961-b3f5-4571-8a68-30cbb140d204",
            "manufacturer": "d510770c-e8cc-4b9f-8863-6044b96bb799",
            "created": "2022-09-14T18:39:45.340401Z",
            "updated": "2022-10-14T09:47:25.969650Z",
            "tag": [],
            "tag_by_user": [],
            "name_by_user": "Stove",
            "iot": true,
            "connection": {
                "timestamp": "2022-10-14T16:06:22.021852Z",
                "online": false
            },
            "stable_connection": {
                "timestamp": "2022-10-14T16:06:22.021852Z",
                "online": false
            }
        }
        """
    )


@pytest.fixture(name="device_obj", scope="module")
def get_device_obj():
    """Device fixture"""
    return json.loads(
        """
        {
            "status": [],
            "value": [
                "309c0f56-280f-4e8d-8fe9-4dc8af8cbdbb",
                "a4e7a139-eb90-4c09-a8d0-760181f504dd"
            ],
            "name": "Stove",
            "manufacturer": "Aduro",
            "product": "P1 [4EFA]",
            "version": "1.2.9",
            "serial": "1879",
            "description": "Aduro Stove on Seluxit Echidna",
            "protocol": "JSONRPC over SSL",
            "communication": "WIFI",
            "meta":
            {
                "id": "373371fe-9735-4069-25d6-44a93531a982",
                "type": "device",
                "version": "2.1",
                "owner": "a4e0a961-b3f5-4571-8a68-30cbb140d204",
                "manufacturer": "d510770c-e8cc-4b9f-8863-6044b96bb799",
                "created": "2022-09-14T18:39:45.340401Z",
                "updated": "2022-10-14T09:47:25.969650Z",
                "tag": [],
                "tag_by_user": [],
                "name_by_user": "Stove",
                "iot": true,
                "connection": {
                    "timestamp": "2022-10-14T16:06:22.021852Z",
                    "online": false
                },
                "stable_connection": {
                    "timestamp": "2022-10-14T16:06:22.021852Z",
                    "online": false
                }
            }
        }
        """
    )


@pytest.fixture(name="number_obj", scope="module")
def get_number_obj():
    """Number fixture"""
    return json.loads(
        """
        {
            "min": 0.0,
            "max": 1.0,
            "step": 1.0,
            "unit": ""
        }
        """
    )


@pytest.fixture(name="entity_number_obj", scope="module")
def get_entity_obj():
    """Entity number fixture"""
    return json.loads(
        """
        {
            "state": [
                "69d1f4fa-b664-46f2-321e-db6a7dc12776"
            ],
            "eventlog": [],
            "name": "On/Off",
            "type": "boolean",
            "period": "0",
            "delta": "0.000000",
            "permission": "w",
            "number": {
                "min": 0.0,
                "max": 1.0,
                "step": 1.0,
                "unit": ""
            },
            "meta": {
                "id": "309c0f56-280f-4e8d-8fe9-4dc8af8cbdbb",
                "type": "value",
                "version": "2.1",
                "owner": "a4e0a961-b3f5-4571-8a68-30cbb140d204",
                "manufacturer": "d510770c-e8cc-4b9f-8863-6044b96bb799",
                "created": "2022-09-14T18:39:45.340401Z",
                "updated": "2022-10-05T16:51:42.810914Z",
                "tag": [],
                "tag_by_user": [],
                "name_by_user": "On/Off"
            }
        }
        """
    )


@pytest.fixture(name="entity_string_obj", scope="module")
def get_entity_string_obj():
    """Entity string fixture"""
    return json.loads(
        """
        {
            "state": [
                "a517d519-e326-4690-076e-115f6c632da6"
            ],
            "eventlog": [],
            "name": "Status",
            "type": "aduro_state",
            "period": "0",
            "delta": "0.000000",
            "permission": "r",
            "string": {
                "encoding": "",
                "max": 10
            },
            "meta": {
                "id": "a4e7a139-eb90-4c09-a8d0-760181f504dd",
                "type": "value",
                "version": "2.1",
                "owner": "a4e0a961-b3f5-4571-8a68-30cbb140d204",
                "manufacturer": "d510770c-e8cc-4b9f-8863-6044b96bb799",
                "created": "2022-09-14T18:39:45.340401Z",
                "updated": "2022-10-05T16:51:42.810914Z",
                "tag": [],
                "tag_by_user": [],
                "name_by_user": "Status"
            }
        }
        """
    )


@pytest.fixture(name="state_string_obj", scope="module")
def get_state_string_obj():
    """State string fixture"""
    return json.loads(
        """
        {
            "timestamp": "2022-10-15T16:29:17.023096Z",
            "data": "WORK PHASE",
            "status_payment": "owned",
            "type": "Report",
            "meta": {
                "id": "a517d519-e326-4690-076e-115f6c632da6",
                "type": "state",
                "version": "2.1",
                "owner": "a4e0a961-b3f5-4571-8a68-30cbb140d204",
                "manufacturer": "d510770c-e8cc-4b9f-8863-6044b96bb799",
                "created": "2022-09-14T18:39:45.340401Z",
                "updated": "2022-10-15T16:29:17.112739Z",
                "tag": [],
                "tag_by_user": [],
                "name_by_user": "Report",
                "iot": true
            }
        }
        """
    )


@pytest.fixture(name="state_number_obj", scope="module")
def get_state_number_obj():
    """State number fixture"""
    return json.loads(
        """
        {
            "timestamp": "2022-10-15T16:29:15.764136Z",
            "data": "0",
            "status_payment": "owned",
            "type": "Control",
            "meta": {
                "id": "69d1f4fa-b664-46f2-321e-db6a7dc12776",
                "type": "state",
                "version": "2.1",
                "owner": "a4e0a961-b3f5-4571-8a68-30cbb140d204",
                "manufacturer": "d510770c-e8cc-4b9f-8863-6044b96bb799",
                "created": "2022-09-14T18:39:45.340401Z",
                "updated": "2022-10-15T16:29:15.987863Z",
                "tag": [],
                "tag_by_user": [],
                "name_by_user": "Control",
                "iot": true
            }
        }
        """
    )
