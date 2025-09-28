from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine,Base
import models, schemas, crud

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Travel Plan API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#分为两个部分 一个是plan 一个是 gallery

@app.get("/")
def read_root():
    return {"tip": "What are u doing here?"}

#先构建plan部分
@app.get("/plans/",response_model=List[schemas.TravelPlanResponse])
def read_plans(db: Session=Depends(get_db)): #读取所有的计划
    return crud.get_plans(db)

@app.post("/plans/",response_model=schemas.TravelPlanResponse) #创建一个新的计划
def create_plan(plan: schemas.TravelPlanCreate, db: Session = Depends(get_db)):
    return crud.create_plan(db=db, plan_in=plan)

@app.get("/plans/{plan_id}", response_model=schemas.TravelPlanResponse)
def read_plan(plan_id:int, db: Session = Depends(get_db)): # 查询单个plan
    plan = crud.get_plan(db, plan_id=plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

@app.put("/plans/{plan_id}", response_model=schemas.TravelPlanResponse) # 修改一个指定plan
def update_plan(plan_id:int, plan_in:schemas.TravelPlanUpdate, db: Session=Depends(get_db)):
    plan = crud.update_plan(db, plan_id=plan_id, plan_in=plan_in)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

@app.delete("/plans/{plan_id}")
def delete_plan(plan_id:int, db: Session = Depends(get_db)): # 删除一个指定plan
    ok = crud.delete_plan(db, plan_id=plan_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Plan not found")    
    return {"status":200, "plan_id":plan_id}
