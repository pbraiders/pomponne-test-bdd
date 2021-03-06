# coding=utf-8
"""PyMySQL adapter"""

from typing import Optional
from pbraiders.database.adapter import AbstractAdapter
import pymysql
import pymysql.cursors


class PyMySQLAdapter(AbstractAdapter):
    _pConnection: Optional[pymysql.connections.Connection] = None

    def __del__(self):
        self.quit()

    def connect(self) -> None:
        self.quit()
        self._pConnection = pymysql.connect(
            host=self.host,
            port=int(self.port),
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset,
            cursorclass=pymysql.cursors.DictCursor
        )
        assert self._pConnection.open is True

    def quit(self) -> None:
        if isinstance(self._pConnection, pymysql.connections.Connection):
            if self._pConnection.open:
                self._pConnection.close()
            del self._pConnection
        self._pConnection = None

    def execute(self, query: str, args: dict = None) -> None:
        try:
            self.connect()
#            with self._pConnection:
            with self._pConnection.cursor() as pCursor:
                sSql = query.format(d=self.database)
                pCursor.execute(sSql, args)
            self._pConnection.commit()
        except Exception as e:
            print("Exception occured while running execute command:{}".format(e))

    def executemany(self, query: str, args) -> None:
        try:
            self.connect()
#            with self._pConnection:
            with self._pConnection.cursor() as pCursor:
                sSql = query.format(d=self.database)
                pCursor.executemany(sSql, args)
            self._pConnection.commit()
        except Exception as e:
            print("Exception occured while running executemany command:{}".format(e))
