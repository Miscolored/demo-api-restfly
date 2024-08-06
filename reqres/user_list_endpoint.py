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

from restfly.endpoint import APIEndpoint

from reqres.user_iterator import UserIterator


class UserListEndpoint(APIEndpoint):
    def list(self) -> UserIterator:
        return UserIterator(self._api)
