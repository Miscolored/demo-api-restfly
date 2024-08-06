"""
User List Endpoint
==================

Wires the UserIterator RESTfly object to the list method of the user API

"""

from __future__ import annotations

from restfly.endpoint import APIEndpoint

from reqres.user_iterator import UserIterator


class UserListEndpoint(APIEndpoint):
    def list(self) -> UserIterator:
        return UserIterator(self._api)
