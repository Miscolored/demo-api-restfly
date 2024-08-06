"""
Users Endpoint
==============

Wires the UserIterator RESTfly object to the list method of the user API

"""

from __future__ import annotations

from restfly.endpoint import APIEndpoint

from reqres.users_iterator import UsersIterator


class UsersEndpoint(APIEndpoint):
    def list(self) -> UsersIterator:
        return UsersIterator(self._api)
