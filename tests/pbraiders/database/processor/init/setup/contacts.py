# coding=utf-8
"""Insert default contacts in database"""

from pbraiders.database.processor import AbstractProcessor


class Contacts(AbstractProcessor):

    def execute(self, contacts: dict):
        print('Inserting contacts')
        self._pAdapter.execute(u"delete from `{d}`.`contact`;")
        self._pAdapter.executemany(
            u"insert into `{d}`.`contact` (`lastname`, `firstname`, `tel`, `email`, `comment`, `create_iduser`, `create_date`) VALUES (%(lastname)s, %(firstname)s, %(tel)s, %(email)s, %(comment)s, 2, NOW());",
            contacts)
