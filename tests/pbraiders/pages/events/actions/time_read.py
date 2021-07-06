# coding=utf-8
"""Event page - read time slot radio button value responsability."""

from __future__ import annotations
from pbraiders.pages.events.actions import RADIO_TIME
from pbraiders.pages.events.actions import EventActionAbstract


class EventTimeReadAction(EventActionAbstract):

    def is_valid(self) -> bool:
        """Return True if the value is valid."""
        p_list = self.page.find_by_name(RADIO_TIME)
        if len(p_list) != 7:
            return False
        else:
            i_index = int(self.event.time) - 1
            p_element = p_list[i_index]
            return p_element.checked
