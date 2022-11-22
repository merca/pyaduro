# pyAduro

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=bugs)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=coverage)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=pyAduro)

Async Python 3 library for Aduro Stove
Async Python 3 library for Aduro Stove P4.

Aduro stove communicates via [Wappsto](https://wappsto.seluxit.com) API ([documentation](https://documentation.wappsto.com/#/docs/introduction/introduction)).

Wappsto portal can contain many devices, this API filters out those by Aduro, named Stove and that have product `P1 [4EFA]`, since this is the only device I can verify.

All device entities, with their state, are returned by the API. Streaming is supported.

Login methodes: username and password or OAuth token.

## Install

```bash
pip install pyaduro
```

## Pulling

```python

from aduro.client import AduroClient
user_name="username"
password="password"

aduro_client=AduroClient()
await aduro_client.async_login(username,password)
# since Wappsto only uses session_id in API, get it after login
session_id = aduro_client.session_id
# then you can store it and skip login for future connections
```

### Find stove

Returns list of stove ids found.

```python

from aduro.session import AduroSession

aduro_session = AduroSession(session_id)
stove_ids = await aduro_session.async_get_stove_ids()
```

### Get stove details

Returns object with stove details.

```python

from aduro.session import AduroSession

aduro_session = AduroSession(session_id)
stove_ids = await aduro_session.async_get_stove_ids()

device_info = await aduro_session.aync_get_device_info(stove_ids[0])

```

### Get all device entities and their states

Returns list of stove entities with all their details. `async_get_state_value` returns state value. Possible states for entity are `Control` (desired state and can be uptated when permission == `w`) or `Report` (current value for state and can not be updated). Entity can have both `Control` and `Report` state.

```python
entities = await aduro.async_get_device_entities(stove.id)
for entity in entities:
    states = await aduro.async_get_state_value(entity.id)
```

## Update state

To update state (with permission `w`).

```python
bool success = await aduro.async_patch_state_value(state_id, value)

```
