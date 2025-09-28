from sqlalchemy.orm import Session
from typing import List, Optional, Dict
import models, schemas

def _normalize_stops(stops: Dict[str, List[dict]]) -> Dict[str, List[dict]]:
    """
    确保每个 stop 都有 order 和 photo_url 字段
    """
    for city, stop_list in stops.items():
        for idx, stop in enumerate(stop_list, start=1):
            if "order" not in stop or stop["order"] is None:
                stop["order"] = idx
            if "photo_url" not in stop:
                stop["photo_url"] = None
    return stops

def create_plan(db: Session, plan_in: schemas.TravelPlanCreate) -> models.TravelPlan:
    data = plan_in.dict()
    data["stops"] = _normalize_stops(data.get("stops", {}))
    db_plan = models.TravelPlan(**data)
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

def get_plans(db: Session) -> List[models.TravelPlan]:
    return db.query(models.TravelPlan).order_by(models.TravelPlan.id.desc()).all()

def get_plan(db: Session, plan_id: int) -> Optional[models.TravelPlan]:
    return db.query(models.TravelPlan).filter(models.TravelPlan.id == plan_id).first()

def update_plan(db: Session, plan_id: int, plan_in: schemas.TravelPlanUpdate) -> Optional[models.TravelPlan]:
    db_plan = db.query(models.TravelPlan).filter(models.TravelPlan.id == plan_id).first()
    if not db_plan:
        return None
    update_data = plan_in.dict(exclude_unset=True)
    if "stops" in update_data:
        update_data["stops"] = _normalize_stops(update_data.get("stops", {}))
    for key, value in update_data.items():
        setattr(db_plan, key, value)
    db.commit()
    db.refresh(db_plan)
    return db_plan

def delete_plan(db: Session, plan_id: int) -> bool:
    db_plan = db.query(models.TravelPlan).filter(models.TravelPlan.id == plan_id).first()
    if not db_plan:
        return False
    db.delete(db_plan)
    db.commit()
    return True

def add_photo_to_stop(db: Session, plan_id: int, city: str, stop_order: int, photo_url: str) -> Optional[models.TravelPlan]:
    db_plan = get_plan(db, plan_id)
    if not db_plan or not db_plan.stops or city not in db_plan.stops:
        return None
    stops = db_plan.stops
    if city not in stops:
        return None
    for stop in stops[city]:
        if stop["order"] == stop_order:
            stop["photo_url"] = photo_url
            break
    else:
        return None
    db.commit()
    db.refresh(db_plan)
    return db_plan