from sqlmodel import SQLModel,create_engine,Field

#creating the metadata
class Faculty(SQLModel, table = True):
    id: int | None = Field(default = None, primary_key = True)
    first_name: str
    last_name: str
    age: int | None = None #can be interger or nothing. None = None means that it is automatically assigned none withou having to type in none
    
   
#creating the database 
engine = create_engine('sqlite:/// department.db')

#accessing the metadata from the class
SQLModel.metadata.create_all(engine)