# coding=utf-8
"""Contact page - main responsabilities."""

from urllib.parse import urljoin
from pbraiders.pages.contacts import ContactPageAbstract

TITLE = 'PBRaiders - {lastname} {firstname}'
HEADER = '{lastname} {firstname}'
CONTACT_LIST_LOCATOR = "//*[contains(text(),'{lastname} {firstname} • {phone}')]/.."


class ContactPage(ContactPageAbstract):
    """Contact page - main responsabilities."""

    def on_page(self) -> bool:
        """Returns True if we are visiting this page."""
        if self.contact is None:
            raise TypeError("Contact is not set!")
        s_title = TITLE.format(lastname=self.contact.lastname, firstname=self.contact.firstname)
        s_header = HEADER.format(lastname=self.contact.lastname, firstname=self.contact.firstname)
        return (self.page.title.lower() == s_title.lower()) and (self.page.find_by_tag('h1').first.text.lower() == s_header.lower())

    def visit(self) -> bool:
        """Goes to the page."""
        if self.contact is None:
            raise TypeError("Contact is not set!")

        try:
            self.page.visit(urljoin(str(self.config['home']), str(self.config['contacts'])))
            self.page.find_by_xpath(CONTACT_LIST_LOCATOR.format(lastname=self.contact.lastname,
                                                                firstname=self.contact.firstname,
                                                                phone=self.contact.tel)).first.click()
        except Exception:
            return False

        return self.on_page()
