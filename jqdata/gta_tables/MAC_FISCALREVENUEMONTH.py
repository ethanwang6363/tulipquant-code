

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FISCALREVENUEMONTH(Base):
    __tablename__ = "MAC_FISCALREVENUEMONTH"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    DATASIGN = Column(String(4, u'utf8_bin'), primary_key=True, nullable=False)
    FISCALREVENUEID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    REVENUE = Column(Numeric(18, 4))
    REVENUEYOY = Column(Numeric(10, 4))
