"""
Reqres API Testing

"""

from __future__ import annotations

from reqres.api import API
from reqres.users_endpoint import UsersEndpoint


def test_constructor():
    """
    Test default constructor
    """
    API()


def test_api_users_endpoint():
    """
    Test the return type of `users` method
    """
    api = API()
    assert isinstance(api.users, UsersEndpoint)
