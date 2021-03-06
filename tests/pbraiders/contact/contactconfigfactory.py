# coding=utf-8
"""Factory used to create a contact from config."""

from __future__ import annotations
from dataclasses import dataclass
from pbraiders.contact import Contact
from pbraiders.contact import ContactAbstractFactory


@dataclass
class ContactConfigFactory(ContactAbstractFactory):
    """Factory used to create a contact from config."""

    def create(self, config: dict) -> Contact:
        config = config[0]
        return Contact(
            lastname=config['lastname'],
            firstname=config['firstname'],
            tel=config['tel'],
            email=config['email'])
