from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configs.env import get_settings
from sqlalchemy.engine import URL

settings = get_settings()

database_url = URL.create(
    drivername="postgresql",
    host=settings.database_hostname,
    username=settings.database_username,
    password=settings.database_password,
    port=settings.database_port,
    database=settings.database_name,
)

engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
