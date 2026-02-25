from sqlmodel import Session
from models import Faculty, engine

#making instances of the faculty class
f1 = Faculty(first_name = 'Christopher', last_name = 'Mansour')
f2 = Faculty(first_name = 'Mahesh', last_name = 'Maddumala')
f3 = Faculty(first_name = 'Chad', last_name = 'Redmond', age = 60)

#adding the instances to the database
with Session(engine) as session:
    session.add(f1)
    session.add(f2)
    session.add(f3)
    
    #commiting the changes
    session.commit()
    
    #session is closed automatically