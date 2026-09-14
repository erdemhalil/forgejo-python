---
description: Token, basic auth, and one-time password credentials for pyfj clients.
---

# Authentication

pyfj takes credentials as explicit constructor arguments — it never reads them from the environment. `Forgejo` and `AsyncForgejo` accept the same arguments, and the credentials are applied to every request the client sends, including raw [escape hatch](escape-hatch.md) calls.

## API token

Tokens are the usual flavour. Pass one to `token=` and pyfj sends `Authorization: token <value>` on every request:

```python
from pyfj import Forgejo

with Forgejo("https://codeberg.org", token="...") as client:
    user = client.user.get()
    print(user.login)
```

Create a token in Forgejo under **Settings → Applications → Generate new token**, with the scopes your calls need. A value that already carries the `token ` prefix is tolerated and not duplicated.

## Basic auth

Pass a `(username, password)` pair to `auth=` to use HTTP Basic:

```python
with Forgejo("https://codeberg.org", auth=("alice", "hunter2")) as client:
    user = client.user.get()
```

Token and basic auth are mutually exclusive: constructing a client with both raises `ValueError` immediately.

## One-time password

When the account has a second factor, `otp=` supplies the one-time password; it is sent as the `X-FORGEJO-OTP` header and can accompany either credential flavour:

```python
with Forgejo("https://codeberg.org", token="...", otp="123456") as client:
    user = client.user.get()
```

## Where credentials live

Credentials are resolved once at construction and composed into the headers of each request. A client built with `client=` (an injected `httpx2.Client`) still uses pyfj's credentials rather than letting the injected client's own auth flow run. The [clients reference](../reference/clients.md) documents the full constructor.
