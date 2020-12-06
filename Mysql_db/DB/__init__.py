import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = sqlalchemy.create_engine(
    "mysql+mysqlconnector://root:mysql@localhost:33010/databasv2"
)

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()