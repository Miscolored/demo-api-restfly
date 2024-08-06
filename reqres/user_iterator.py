"""
User Iterator
=============

Manages the pagination of the Reqres `users` api,
presenting instead a Python iterator

"""

from __future__ import annotations

from restfly.iterator import APIIterator


class UserIterator(APIIterator):
    def _get_page(self) -> None:
        resp = self._api.get(
            "users",
            params={
                "page": self.num_pages + 1,
            },
        ).json()

        self.total = resp.get("total")
        self.page = resp.get("data", list())
