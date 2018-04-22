

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class STK_PERSONALHOLDERALIAS(Base):
    __tablename__ = "STK_PERSONALHOLDERALIAS"

    PERSONALHOLDERID = Column(Numeric(30, 0))
    ALIAS = Column(String(200, u'utf8_bin'), primary_key=True)
    SHAREHOLDERTYPE = Column(String(100, u'utf8_bin'))
    SHAREHOLDERTYPECODE = Column(String(10, u'utf8_bin'))
    ISSTANDARDFULLNAME = Column(String(2, u'utf8_bin'))
