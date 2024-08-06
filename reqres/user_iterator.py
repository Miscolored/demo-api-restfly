"""
Demo Users API
==============

The following classes wrap https://reqres.in/api using RESTfly

Usage:
from demo.users import Reqres
reqres_api = Reqres()
for user in reqres_api.users.list():
    print(user)

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
