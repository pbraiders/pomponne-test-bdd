# coding=utf-8
"""Event page - fill contact fields responsability."""

from __future__ import annotations
from pbraiders.pages.contacts.actions import FIELD_LASTNAME
from pbraiders.pages.contacts.actions import FIELD_FIRSTNAME
from pbraiders.pages.contacts.actions import FIELD_PHONE
from pbraiders.pages.contacts.actions import FIELD_EMAIL
from pbraiders.pages.events.actions import EventActionAbstract


class EventContactWriteAction(EventActionAbstract):

    def fill_email(self) -> EventContactWriteAction:
        """Fills the email field"""
        self.page.fill(FIELD_EMAIL, self.contact.email)
        return self

    def fill_lastname(self) -> EventContactWriteAction:
        """Fills the lastname field"""
        self.page.fill(FIELD_LASTNAME, self.contact.lastname)
        return self

    def fill_firstname(self) -> EventContactWriteAction:
        """Fills the firstname field"""
        self.page.fill(FIELD_FIRSTNAME, self.contact.firstname)
        return self

    def fill_phone(self) -> EventContactWriteAction:
        """Fills the phone field"""
        self.page.fill(FIELD_PHONE, self.contact.tel)
        return self
