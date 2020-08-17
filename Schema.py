# coding: utf-8
import sys
from random import randint

from sqlalchemy import BigInteger, CHAR, Column, DECIMAL, DateTime, ForeignKey, Index, Integer, LargeBinary, Unicode, \
    create_engine, MetaData
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from faker.factory import Factory
faker = Factory.create
faker = faker()

database_URL = r'mssql+pymssql://postgres:postgres@localhost\SQLEXPRESS/shop'
Base = declarative_base()
metadata = MetaData()
engine = create_engine(database_URL, convert_unicode=True)
Base.metadata.bind = engine
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
# We will need this for querying
Base.query = db_session.query_property()
Base.metadata.create_all(engine, Base.metadata.tables.values(), checkfirst=True)


class CUSTOMER(Base):
    __tablename__ = 'CUSTOMER'

    cid = Column(Integer, primary_key=True)
    cName = Column(Unicode(30), nullable=False)
    customerType = Column(CHAR(30, 'Arabic_CI_AS'))
    maxCredit = Column(BigInteger)


class PRODUCT(Base):
    __tablename__ = 'PRODUCT'

    pid = Column(Integer, primary_key=True)
    pName = Column(Unicode(30), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)


class ORDER1(Base):
    __tablename__ = 'ORDER1'

    oid = Column(Integer, primary_key=True)
    oDate = Column(DateTime, nullable=False)
    cid = Column(ForeignKey('CUSTOMER.cid', ondelete='CASCADE'), nullable=False)

    CUSTOMER = relationship('CUSTOMER', backref='ORDER1', passive_deletes=True)


class OrderTotal(ORDER1):
    __tablename__ = 'OrderTotal'

    oid = Column(ForeignKey('ORDER1.oid', ondelete='CASCADE'), primary_key=True)
    totalAmount = Column(BigInteger)
    lastUpdate = Column(DateTime)


class ORDERITEM(Base):
    __tablename__ = 'ORDERITEM'

    iid = Column(Integer, primary_key=True)
    oid = Column(ForeignKey('ORDER1.oid', ondelete='CASCADE'), nullable=False)
    pid = Column(ForeignKey('PRODUCT.pid', ondelete='CASCADE'), nullable=False)
    quantity = Column(Integer, nullable=False)

    ORDER1 = relationship('ORDER1', backref='ORDERITEM', passive_deletes=True)
    PRODUCT = relationship('PRODUCT', backref='ORDERITEM', passive_deletes=True)


if __name__ == '__main__':
    if '-g' in sys.argv:
        for i in range(1000):
            p = PRODUCT(pName=faker.word(), price=randint(0, 1000))
            c = CUSTOMER(cName=faker.name(),
                         customerType=randint(0, 1),
                         maxCredit=randint(0, 1000)
                         )
            db_session.add(p)
            db_session.add(c)
        db_session.commit()
        for i in range(1000):
            o = ORDER1(oDate=faker.date_time(),
                   cid=randint(0, 1000),
                   )
            db_session.add(o)
        db_session.commit()
        for i in range(1000):
            oi = ORDERITEM(oid=randint(0, 1000),
                      pid=randint(0, 1000),
                      quantity=randint(0, 1000)
                      )
            db_session.add(oi)
        db_session.commit()
        print('added 1000 item')
