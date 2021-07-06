# coding=utf-8
"""Event page - choose type radio button responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import RADIO_TYPE
from pbraiders.pages.events.actions import EventActionAbstract


class EventTypeWriteAction(EventActionAbstract):

    def choose(self) -> None:
        """Choose a value in the type radio buttons group."""
        self.page.choose(RADIO_TYPE, self.event.type)
