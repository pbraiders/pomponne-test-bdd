# coding=utf-8
"""Event utilities."""


from splinter.driver import DriverAPI
from pbraiders.contact import Contact
from pbraiders.event import Event
from pbraiders.pages.events import EventsPage
from pbraiders.pages.events.actions import EventCreateAction
from pbraiders.pages.events.actions import EventTimeWriteAction
from pbraiders.pages.events.actions import EventTypeWriteAction
from pbraiders.pages.events.actions import EventContactWriteAction
from pbraiders.pages.events.actions import EventHeadcountWriteAction
from pbraiders.pages.events.actions import EventMoneyWriteAction


def new_event(driver: DriverAPI, config: dict, contact: Contact, event: Event) -> bool:
    """Creates an event and a new contact.
       config=config['urls']"""

    # Visit new event page
    p_page = EventsPage(_driver=driver, _config=config, _event=event, _contact=contact)
    assert p_page.visit() is True

    # Fill the fields
    p_action = EventContactWriteAction(_page=p_page)
    p_action.fill_lastname() \
            .fill_firstname() \
            .fill_phone() \
            .fill_email()
    del p_action
    # Fill event headcount field
    p_action = EventHeadcountWriteAction(_page=p_page)
    p_action.fill_real() \
            .fill_planned()
    del p_action
    # Fill event type field
    p_action = EventTypeWriteAction(_page=p_page)
    p_action.choose()
    del p_action
    # Fill event time slot field
    p_action = EventTimeWriteAction(_page=p_page)
    p_action.choose()
    del p_action
    # Fill event arrh field
    p_action = EventMoneyWriteAction(_page=p_page)
    p_action.choose()
    del p_action

    # Create
    p_action = EventCreateAction(_page=p_page)
    p_action.click()

    # Check
    return p_action.has_succeeded()
