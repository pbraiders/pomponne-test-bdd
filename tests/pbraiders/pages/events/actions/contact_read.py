# coding=utf-8
"""Event page - is_equal contact fields responsability."""

from __future__ import annotations
from pbraiders.pages.contacts.actions import FIELD_LASTNAME
from pbraiders.pages.contacts.actions import FIELD_FIRSTNAME
from pbraiders.pages.contacts.actions import FIELD_PHONE
from pbraiders.pages.contacts.actions import FIELD_EMAIL
from pbraiders.pages.events.actions import EventActionAbstract


class EventContactReadAction(EventActionAbstract):

    def is_equal_email(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_EMAIL)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.contact.email).lower()

    def is_equal_lastname(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_LASTNAME)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.contact.lastname).lower()

    def is_equal_firstname(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_FIRSTNAME)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.contact.firstname).lower()

    def is_equal_phone(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(FIELD_PHONE)
        if p_list.is_empty():
            return False
        else:
            return str(p_list.first.value).lower() == str(self.contact.tel).lower()
