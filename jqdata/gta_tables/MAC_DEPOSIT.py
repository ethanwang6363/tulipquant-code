

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_DEPOSIT(Base):
    __tablename__ = "MAC_DEPOSIT"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True)
    NETFOREIGNASSETS = Column(Numeric(20, 4))
    DOMESTICCREDIT = Column(Numeric(20, 4))
    GOVERNMENTCLAIM = Column(Numeric(20, 4))
    NONFINANCECLAIM = Column(Numeric(20, 4))
    OTHERFINANCECLAIM = Column(Numeric(20, 4))
    M2 = Column(Numeric(20, 4))
    M1 = Column(Numeric(20, 4))
    M0 = Column(Numeric(20, 4))
    CORPORATEDEMANDDEPOSIT = Column(Numeric(20, 4))
    QUASIMONEY = Column(Numeric(20, 4))
    CORPORATETIMEDEPOSIT = Column(Numeric(20, 4))
    PERSONALDEPOSIT = Column(Numeric(20, 4))
    OTHERDEPOSIT = Column(Numeric(20, 4))
    EXCLUDEBROADMONEY = Column(Numeric(20, 4))
    BOND = Column(Numeric(20, 4))
    PAIDINCAPITAL = Column(Numeric(20, 4))
    OTHERITEM = Column(Numeric(20, 4))
