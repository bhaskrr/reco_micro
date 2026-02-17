from sqlalchemy import Column, Integer, String, Float, DateTime
from src.db.database import Base
import datetime


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, index=True)
    item_id = Column(String, index=True)
    action_type = Column(String)  # 'click', 'like', 'purchase'
    weight = Column(Float, default=1.0)  # For "Weighted Interactions" feature!
    timestamp = Column(DateTime, default=datetime.utcnow)
