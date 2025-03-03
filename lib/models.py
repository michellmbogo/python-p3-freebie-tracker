from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    # Relationships
    freebies = relationship('Freebie', back_populates='company')
    devs = relationship('Dev', secondary='freebies', back_populates='companies')


    def __repr__(self):
        return f'<Company {self.name}>'


    # Additional methods
    @classmethod
    def oldest_company(cls, session):
        return session.query(cls).order_by(cls.founding_year).first()

    def give_freebie(self, dev, item_name, value):
        freebie = Freebie(dev_id=dev.id, company_id=self.id, item_name=item_name, value=value)
        session.add(freebie)
        session.commit()
        return freebie    

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    freebies = relationship('Freebie', back_populates='dev')
    companies = relationship('Company', secondary='freebies', back_populates='devs')


    def __repr__(self):
        return f'<Dev {self.name}>'

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, dev, freebie):
        if freebie.dev == self:
            freebie.dev = dev
            session.commit()  

    
class Freebie(Base):
    __tablename__ = 'freebies'
    
    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    # Foreign keys
    dev_id = Column(Integer, ForeignKey('devs.id'), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    # Relationships
    dev = relationship("Dev", back_populates="freebies")
    company = relationship("Company", back_populates="freebies")

    def __repr__(self):
        return f"<Freebie {self.item_name} from {self.company.name} to {self.dev.name}>"