# coding=utf-8
"""Users utilities."""

from pbraiders.user import User
from pbraiders.options.users import PageUsers


def new_account(p_page_users: PageUsers, p_user: User) -> None:
    """Creates account."""
    p_page_users.set_user(p_user).visit().fill_name().fill_password().confirm_password().click()
    assert p_page_users.has_succeeded() is True