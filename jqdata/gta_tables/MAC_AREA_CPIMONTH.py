

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_CPIMONTH(Base):
    __tablename__ = "MAC_AREA_CPIMONTH"

    DECLAREDATE = Column(DateTime)
    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    DATASIGN = Column(String(4, u'utf8_bin'), primary_key=True, nullable=False)
    OBJECTID = Column(String(4, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    ITEMID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    CPI = Column(Numeric(10, 4))
    CPIMOM = Column(Numeric(10, 4))
