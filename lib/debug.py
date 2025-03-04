#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()



company1 = Company(name="Agape Tech", founding_year=2000)
company2 = Company(name="Mawingu Internet", founding_year=2010)
dev1 = Dev(name="Michell")
dev2 = Dev(name="Wambui")

# Add them to the session
session.add(company1)
session.add(company2)
session.add(dev1)
session.add(dev2)

# Commit the changes to the database
session.commit()


companies = session.query(Company).all()
devs = session.query(Dev).all()


print("Companies:", companies)
print("Developers:", devs)

#  giving freebies
company1.give_freebie(dev1, "Laptop", 2)
company1.give_freebie(dev2, "Tablet", 2)

company2.give_freebie(dev1, "Water Bottle", 1)
company2.give_freebie(dev1, "Smart Watch", 2)

session.commit()  



# Check dev1's freebies
print(dev1.freebies)


session.close()
