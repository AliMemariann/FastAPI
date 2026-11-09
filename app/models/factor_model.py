from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Factors(Base):
    __tablename__ = 'factors'

    id = Column(Integer, primary_key=True, index=True)
    cid = Column(Integer, ForeignKey('customers.id'))
    date = Column(DateTime, default=datetime.utcnow)
    total = Column(Integer, default=0)
    jalalidate = Column(String, default='')

    customer = relationship('Customer', back_populates='factors')
    items = relationship('Factor_item', back_populates='factor')