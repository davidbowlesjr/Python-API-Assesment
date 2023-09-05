from sqlalchemy import DateTime, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column("id", Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    orgName = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    

    def __repr__(self):
        return f"User({self.id},'{self.email}','{self.password}','{self.orgName}','{self.firstName}','{self.lastName})"
    
    def __str__(self):
        return f"User({self.id},'{self.email}','{self.password}','{self.orgName}','{self.firstName}','{self.lastName})"

    def as_dict(self):
       userDict = {c.name: getattr(self, c.name) for c in self.__table__.columns}
       userDict.pop("password")
       return {"user": userDict}

        
    