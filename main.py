from fastapi import FastAPI , Path,Query,Form,File,UploadFile,HTTPException
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

class Nitesh(BaseModel):
    one:str
    two:str
    three:int

#form data
@app.post("/form/data")
async def form_data(username:str=Form(),password:str=Form()):
    return{"username":username,"password":password}


#Upload File
@app.post("/file/upload")
async def file_bytes_len(file:bytes=File()):
    return{"file":len(file)}


@app.post("/upload/file")
async def file_upload(file:UploadFile):
    return{"filename":file.filename,"file_content_type":file.content_type}


@app.post("/form/data/filedata")
async def formdata_uploadfile(file1:UploadFile,file2:bytes=File(),name:str=Form()):
    return{"filename":file1.filename,"file_size":len(file2) ,"name":name}



#error handling 

items=[1,2,3,4,5]
@app.get("/error/handling")
async def handle_error(item:int):
    if item not in items :
        return HTTPException(status_code=400,detail="item is not equal to 2 try another number")
    return {"value":item}