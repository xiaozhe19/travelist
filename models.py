from sqlalchemy import Column, Interger, String, Date, Json, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TravelPlan(Base):
    __tablename__ = "travel_plans"

    id = Column(Interger,primary_key=True, index=True)
    title = Column(String, nullable=False) # 计划标题
    is_multi_cities = Column(Boolean, nullable = False) # 是否为多城市计划
    description = Column(String, nullable = True) # 计划描述
    start_date = Column(Date, nullable=False) # 计划开始日期
    end_date = Column(Date, nullable=False) # 计划结束日期
    stops = Column(Json, nullable = True) # 计划停靠点，存储为JSON格式
