#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dev, Company, Freebie

# Set up the database connection and session
engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)  # Creates the tables in the database

Session = sessionmaker(bind=engine)
session = Session()

# Creating some sample companies
company1 = Company(name="TechCorp", founding_year=2000)
company2 = Company(name="WebWorks", founding_year=2010)

# Creating some sample devs
dev1 = Dev(name="John Doe")
dev2 = Dev(name="Jane Smith")

# Add companies and devs to the session
session.add(company1)
session.add(company2)
session.add(dev1)
session.add(dev2)

# Commit the session to save devs and companies
session.commit()

# Assigning freebies to devs
freebie1 = Freebie(dev_id=dev1.id, company_id=company1.id, item_name="Laptop", value=1000)
freebie2 = Freebie(dev_id=dev2.id, company_id=company1.id, item_name="Smartphone", value=500)
freebie3 = Freebie(dev_id=dev1.id, company_id=company2.id, item_name="Headphones", value=150)

# Add freebies to the session
session.add(freebie1)
session.add(freebie2)
session.add(freebie3)

# Commit the session to save the freebies
session.commit()

print("Seed data has been added to the database.")
