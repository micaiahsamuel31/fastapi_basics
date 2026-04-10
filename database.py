from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session

database_url = "mysql+pymysql://root:Qwerty%40123@localhost:3306/fast_apidatabase"
engine = create_engine(database_url)

Ses = sessionmaker(autoflush=False, autocommit=False, bind=engine )

def get_task();
  db=Ses()
  try:
    yield db
  finally:
    db.close()

