---
title: "Errors and pagination"
description: "The exception hierarchy and the pagination wrappers returned by list operations."
---

# Errors and pagination

Non-2xx responses raise a typed exception; list operations return a lazy pagination wrapper.

## Errors

All exceptions descend from `ForgejoError`. `APIError` carries `status_code`, `body`, and the raw `httpx.Response`; transport failures raise `TransportError`, and responses that do not match the Spec raise `DecodeError`.

::: pyfj.ForgejoError

::: pyfj.APIError

::: pyfj.TransportError

::: pyfj.DecodeError

::: pyfj.BadRequestError

::: pyfj.UnauthorizedError

::: pyfj.ForbiddenError

::: pyfj.NotFoundError

::: pyfj.MethodNotAllowedError

::: pyfj.ConflictError

::: pyfj.PreconditionFailedError

::: pyfj.PayloadTooLargeError

::: pyfj.UnprocessableEntityError

::: pyfj.LockedError

::: pyfj.ServerError

## Pagination

List operations return `Paginated[T]` (sync) or `AsyncPaginated[T]` (async): iterating walks pages transparently, `.total_count` mirrors `X-Total-Count`, and `.page(n)` fetches a single page.

::: pyfj.Paginated
    options:
      members:
        - total_count
        - page

::: pyfj.AsyncPaginated
    options:
      members:
        - total_count
        - page
