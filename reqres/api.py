"""
Reqres API
==========

The following classes wrap https://reqres.in/api using RESTfly

Example Usage:

from reqres.api import API as ReqresAPI

reqres_api = ReqresAPI()

for user in reqres_api.users.list():
    print(user)

"""

from __future__ import annotations

from restfly.session import APISession

from reqres.users_endpoint import UsersEndpoint


class API(APISession):
    _url = "https://reqres.in/api"  # no trailing slash by RESTfly standard

    @property
    def users(self) -> UsersEndpoint:
        return UsersEndpoint(self)
