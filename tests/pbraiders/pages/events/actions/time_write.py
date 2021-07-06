# coding=utf-8
"""Event page - choose time slot radio button responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import RADIO_TIME
from pbraiders.pages.events.actions import EventActionAbstract


class EventTimeWriteAction(EventActionAbstract):

    def choose(self) -> None:
        """Choose a value in the time slot radio buttons group."""
        self.page.choose(RADIO_TIME, self.event.time)
