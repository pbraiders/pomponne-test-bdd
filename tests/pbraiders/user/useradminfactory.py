# coding=utf-8
"""Factory used to create admin user from config."""

from pbraiders.user import User
from pbraiders.user import UserAbstractFactory


class UserAdminFactory(UserAbstractFactory):
    """Factory used to create admin user from config."""

    def create(self, config: dict) -> User:
        return User(login=config['admin']['login'],
                    password=config['admin']['password'],
                    passwordc=config['admin']['password'])
