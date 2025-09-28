from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import date

class TravelPlanCreate(BaseModel):
    title: str
    start_date: date
    end_date: date
    is_multi_cities: bool
    description: Optional[str] = None
    stops: Optional[Dict[str, List[Dict]]] = None

class TravelPlanUpdate(BaseModel):
    title: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    is_multi_cities: Optional[bool] = None
    description: Optional[str] = None
    stops: Optional[Dict[str, List[Dict]]] = None

class TravelPlanResponse(BaseModel):
    id: int
    title: str
    start_date: date
    end_date: date
    is_multi_cities: bool
    description: Optional[str] = None
    stops: Optional[Dict[str, List[Dict]]] = None

    class Config:
        orm_mode = True