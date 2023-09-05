from typing import  Union
import datetime
import inspect
from sqlalchemy import create_engine, select, exc
import sqlalchemy
from sqlalchemy.orm import Session
from Models.UserModels import User

from structlog import get_logger

from Models.UserModels import User

logger = get_logger(__name__)

db_url = "sqlite:///test-db.sqlite"

engine = create_engine(db_url, echo=True)

session = Session(engine)

def get_user_by_email(email: str) -> User:
    """returns a single user"""

    logger.debug("get_user_by_email")
    stmt = select(User).filter_by(email = email)

    try:
        result = session.execute(stmt).scalars().all()[0].as_dict()
    except IndexError:
            return "email Invalid"


def create_user(email:str, password:str, orgName: str, firstName:str, lastName: str) -> User:
    """creates a single user"""

    logger.debug("create_user")
    user = User(email=email, password=password, orgName = orgName, 
                 firstName = firstName, lastName = lastName)
    session.add(user)
    session.commit()
    return user



def delete_user(user: User) -> Union[User, None]:
    """deletes a single user"""

    logger.debug("delete_user")
    session.delete(user)
    session.commit()
    return user
