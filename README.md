# pyAduro

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=bugs)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=coverage)](https://sonarcloud.io/summary/new_code?id=pyAduro)[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=pyAduro&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=pyAduro)

Async Python 3 library for Aduro Stove P4

Aduro stove communicates via [Wappsto](https://wappsto.seluxit.com) API ([documentation](https://documentation.wappsto.com/#/docs/introduction/introduction)).

Wappsto portal can contain many devices, this API filter out Devices by Aduro, named Stove and have product `P1 [4EFA]`, since this is the only device I can verify.

All device entities with their state are returned in API. Also streaming is supported.

Login methodes: username and password or OAuth token.

## Install

```bash
pip install pyAduro
```

## Pulling

```python

from aduro import Aduro
user_name="username"
password="password"

aduro=Aduro()
await aduro.async_login(username,password)
# since Wappsto only uses session_id in API, get it after login
session_id = aduro.session_id
# then you can store it and skip login for future connections
```

### Get stove details

Returns object with stove details

```python
# session_id is optional, if you omit session_id client uses private member
# equilent for `aduro.aduro.aduro_find_stove(aduro.session_id)` and fails if login was not priorly invoked
stove = await aduro.aduro_find_stove(session_id)
```

### Get list of all entities and loop over its states

Returns list of stove entities with all their details. `get_entity_states` retruns list of statess. Possible states for entity are `control` (desired state and can be uptated when permission == `w`) or `report` (current value for state and can not be updated)

```python
entities = await aduro.get_all_entities(stove.id, session_id)
for entity in entities:
    states = await aduro.get_entity_states(entity.id, session_id)
```

### Get only entity ids

Returns list of entity ids.

```python
entity_ids = await aduro.get_entity_ids(stove_id, session_id)
# returns dict for all the entities
```

### Get only state values

Returns list of objects that include state id, state value, timestamp

```python
state_values = await aduro.get_states(stove_id, session_id)
# return dict with all states
```

## Update state

To update state (with permission `w`)

```python
bool success = await aduro.update_state(state_id, value)

```

## Streaming

Streamin supports reading states with type "report" (that indicates current value)

```python
def _callback(pkg):
    data = pkg.get("data")
    if data is None:
        return
    print(data.get("measurment"))

async def run():
    async with aiohttp.ClientSession() as session:
        aduro = Aduro(websession=session)
    await aduro.rt_subscribe(_callback)
```
