from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from setting.config import get_settings

settings = get_settings()

# Create engine
engine = create_engine(settings.database_url)

Base = declarative_base()

database = Database(settings.database_url)

Session = sessionmaker(bind=engine)
session = Session()
