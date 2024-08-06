"""
Users Endpoint Testing

"""

from __future__ import annotations

from reqres.api import API
from reqres.users_endpoint import UsersEndpoint
from reqres.users_iterator import UsersIterator


def test_constructor():
    """
    Test construction with API
    """
    UsersEndpoint(API())


def test_list_iterator():
    """
    Test list iteration
    """
    users_endpoint = UsersEndpoint(API())
    assert isinstance(users_endpoint.list(), UsersIterator)
