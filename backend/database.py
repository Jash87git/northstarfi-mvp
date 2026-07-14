import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

class FireScenario(Base):
    __tablename__ = "fire_scenarios"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="User")
    age = Column(Integer)
    current_portfolio = Column(Float)
    monthly_investment = Column(Float)
    monthly_expenses = Column(Float)
    expected_return = Column(Float)
    withdrawal_rate = Column(Float)
    fire_number = Column(Float)
    years_to_fire = Column(Float)
    fire_age = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

def create_tables():
    Base.metadata.create_all(bind=engine)
