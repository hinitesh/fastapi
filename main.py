from fastapi import FastAPI         

app= FastAPI()

@app.get("/")
async def root():
    return {"message":"hello world"}

@app.get("/Nitesh")
async def hi():
    return {"message":"hello Nitesh"}