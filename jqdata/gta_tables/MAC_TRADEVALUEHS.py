

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_TRADEVALUEHS(Base):
    __tablename__ = "MAC_TRADEVALUEHS"

    SGNMONTH = Column(String(14, u'utf8_bin'))
    DATASIGN = Column(String(4, u'utf8_bin'))
    HSID = Column(BigInteger)
    EXPORT = Column(Numeric(18, 4))
    IMPORT = Column(Numeric(18, 4))
    EXPORTYOY = Column(Numeric(10, 4))
    IMPORTYOY = Column(Numeric(10, 4))
    UPDATEID = Column(BigInteger, primary_key=True)
