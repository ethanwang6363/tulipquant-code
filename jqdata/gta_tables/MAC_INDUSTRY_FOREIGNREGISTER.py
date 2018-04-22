

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_INDUSTRY_FOREIGNREGISTER(Base):
    __tablename__ = "MAC_INDUSTRY_FOREIGNREGISTER"

    SGNYEAR = Column(String(8, u'utf8_bin'))
    INDUSTRYID = Column(String(20, u'utf8_bin'))
    ENTERPRISENUM = Column(Numeric(18, 4))
    INVEST = Column(Numeric(18, 4))
    REGISTEREDCAPITAL = Column(Numeric(18, 4))
    FOREIGNREGISTERED = Column(Numeric(18, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
