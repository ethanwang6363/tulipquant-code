

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_REGION_POSTY(Base):
    __tablename__ = "MAC_REGION_POSTY"

    SGNYEAR = Column(String(8, u'utf8_bin'), primary_key=True, nullable=False)
    AREAID = Column(BigInteger, primary_key=True, nullable=False)
    AREANAME = Column(String(100, u'utf8_bin'))
    POSTOFFICE = Column(Numeric(20, 4))
    POSTALSERVICE = Column(Numeric(20, 4))
    TELESERVICE = Column(Numeric(20, 4))
    PHONEUSER = Column(Numeric(20, 4))
    MOBILEUSER = Column(Numeric(20, 4))
    INTERNETUSER = Column(Numeric(20, 4))
    POSTALTELE = Column(Numeric(20, 4))
    PHONEPERHUNDRED = Column(Numeric(20, 4))
