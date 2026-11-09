from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Factor_item(Base):
    __tablename__ = 'factor_item'

    id = Column(Integer, primary_key=True, index=True)
    fid = Column(Integer, ForeignKey('factors.id'))
    pid = Column(Integer, ForeignKey('products.id'))
    no = Column(Integer, default=0)
    price = Column(Integer, default=0)
    total = Column(Integer, default=0)

    factor = relationship('Factors', back_populates='items')
    products = relationship('Product', back_populates='fitem')