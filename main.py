from typing import Union

from fastapi import FastAPI

app = FastAPI()

#分为两个部分 一个是plan 一个是 gallery

@app.get("/")
def read_root():
    return {"tip": "What are u doing here?"}

#先构建plan部分
@app.get("/plans/")
def read_plans(): #读取所有的计划
    return {"plans":"Here are all plans."}

@app.post("/plans/") #创建一个新的计划
def create_plan(plan: dict):
    return {"status":200, "plan":plan}

@app.get("/plans/{plan_id}")
def read_plan(plan_id:int): # 查询单个plan
    return {"status":200, "plan_id":plan_id}

@app.put("/plans/{plan_id}") # 修改一个指定plan
def update_plan(plan_id:int, plan:dict):
    return {"status":200, "plan_id":plan_id, "plan":plan}

@app.delete("/plans/{plan_id}")
def delete_plan(plan_id:int): # 删除一个指定plan
    return {"status":200, "plan_id":plan_id}