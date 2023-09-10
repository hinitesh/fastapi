from fastapi import FastAPI , Path,Query
from typing import Union  
from enum import Enum
from unittest.util import _MAX_LENGTH
from pydantic import BaseModel    



class Choice_Name(str, Enum):
    one = "one"
    two = "two"
    three = "three"

class schema1(BaseModel):
    name:str
    Class:str
    roll_no:int


app= FastAPI()

@app.get("/")
async def root():
    return {"message":"hello world"}

@app.get("/Nitesh")
async def hi():
    return {"message":"hello Nitesh"}


@app.get("/items/{Item}")
async def path_func(Item):
    var_name={"path_varaible":Item}
    return (var_name)


@app.get("/query")
async def query_func(name:str,roll_no:Union[int,None]=None):
    var_name={"name":name ,"roll_no":roll_no}
    return (var_name)

@app.get("/models/{model_name}")
async def get_model(model_name: Choice_Name):
    if model_name.value=="one":
        return {"model_name": model_name, "message": "calling one"}

    if model_name.value == "two":
        return {"model_name": model_name, "message": "calling two   "}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/newquery")
async def query_func(name:Union[str,None]=None,roll_no:Union[str,None]=Query(default=None,min_length=3,max_length=3)):
    var_name={"name":name ,"roll_no":roll_no}
    return (var_name)


#REQUEST BODY



@app.post("/items/")
async def create_item(item:schema1):
    return item
