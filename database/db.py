from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine (
    'sqlite:///database/accounts.sqlite',
    echo=True,
    connect_args = {'check_same_thread': False})
    
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
