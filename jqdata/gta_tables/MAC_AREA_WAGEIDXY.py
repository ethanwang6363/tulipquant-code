

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_WAGEIDXY(Base):
    __tablename__ = "MAC_AREA_WAGEIDXY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    OBJECTID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    AREACODE = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    WAGE = Column(Numeric(18, 4))
    WAGEIDX = Column(Numeric(10, 4))
    AVGWAGE = Column(Numeric(18, 4))
    AVGCURRENCYWAGEIDX = Column(Numeric(10, 4))
    AVGACTUALWAGEIDX = Column(Numeric(10, 4))
