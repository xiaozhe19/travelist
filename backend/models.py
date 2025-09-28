from sqlalchemy import Column, String, Date, JSON, Boolean, Integer
from database import Base

class TravelPlan(Base):
    __tablename__ = "travel_plans"

    id = Column(Integer,primary_key=True, index=True)
    title = Column(String, nullable=False) # 计划标题
    is_multi_cities = Column(Boolean, nullable = False) # 是否为多城市计划
    description = Column(String, nullable = True) # 计划描述
    start_date = Column(Date, nullable=False) # 计划开始日期
    end_date = Column(Date, nullable=False) # 计划结束日期
    stops = Column(JSON, nullable = True) # 计划停靠点，存储为JSON格式
    # stops的格式为 {"city_name": [{"order": 1, "name": "stop1", "photo_url": "http://..."}, {"order": 2, "name": "stop2"}], "another_city": [...]}