

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_FDI(Base):
    __tablename__ = "MAC_INDUSTRY_FDI"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    INDUSTRYID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    PROJECTNUM = Column(Numeric(18, 4))
    INVESTVALUE = Column(Numeric(18, 4))
