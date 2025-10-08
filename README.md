# pyAduro

## Overview

`pyAduro` is an asynchronous Python 3 library for interacting with Aduro P4 stoves through the [Wappsto](https://wappsto.seluxit.com) cloud API. The client automatically filters the connected Wappsto devices to the verified Aduro product `P1 [4EFA]`, exposing all available entities and their real-time state information. Both polling and streaming usage patterns are supported.

## Requirements

- Python 3.10 or newer
- An active Wappsto account with at least one connected Aduro stove
- Either a Wappsto username/password pair or an OAuth token for authentication

## Installation

Install the library from PyPI:

```bash
pip install pyaduro
```

## Authentication

Create an `AduroClient`, authenticate, and capture the Wappsto session identifier. The session ID can be reused in subsequent runs to avoid logging in repeatedly.

```python
from aduro.client import AduroClient

USERNAME = "username"
PASSWORD = "password"

client = AduroClient()
await client.async_login(USERNAME, PASSWORD)
session_id = client.session_id
```

If you already have a valid session ID or OAuth token, pass it directly when creating the client to skip the login call.

## Working with sessions

Use the session helper to discover stoves and inspect their metadata. All helper methods are asynchronous and should be awaited within an event loop (for example inside an `asyncio` task).

```python
from aduro.session import AduroSession

session = AduroSession(session_id)
stove_ids = await session.async_get_stove_ids()

device_info = await session.async_get_device_info(stove_ids[0])
```

## Entities and states

Each stove exposes a collection of entities. Every entity can include one or both of the following state types:

- **Control** – writable when the permission flag is `w`
- **Report** – read-only state representing the latest reported value

Retrieve the entities for a stove and inspect their individual states:

```python
entities = await session.async_get_device_entities(stove_ids[0])
for entity in entities:
    states = await session.async_get_state_value(entity.id)
```

## Updating control states

For writable states, call `async_patch_state_value` with the target state identifier and the new value. The coroutine returns `True` on success.

```python
success = await session.async_patch_state_value(state_id, value)
```

## Additional resources

- [Wappsto API documentation](https://documentation.wappsto.com/#/docs/introduction/introduction)
- [Project issue tracker](https://github.com/maaslalani/pyaduro/issues)

For integration examples and troubleshooting tips, consult the Home Assistant community forums or open an issue if you need further assistance.
