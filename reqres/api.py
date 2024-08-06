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

from restfly.session import APISession

from reqres.user_list_endpoint import UserListEndpoint


class API(APISession):
    _url = "https://reqres.in/api"  # no trailing slash by RESTfly standard

    @property
    def users(self) -> UserListEndpoint:
        return UserListEndpoint(self)
