"""
User Iterator Testing

"""

from __future__ import annotations

from reqres.api import API
from reqres.users_iterator import UsersIterator


def test_constructor():
    """
    Test constructor with API
    """
    UsersIterator(API())


def test_page_population():
    """
    Test population of page attribute
    """
    iterator = UsersIterator(API())

    assert len(iterator.page) == 0
    iterator._get_page()
    assert len(iterator.page) > 1


def test_iteration():
    """
    Test population of page attribute
    """
    iterator = UsersIterator(API())

    assert iterator.next() is not None
