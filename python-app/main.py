from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from db import db

app = FastAPI(debug=True)

@app.get("/wydarzenie")
def get_wydarzenie():
    my_db = db()
    return my_db.get_wydarzenie()

@app.post("/wydarzenie")
async def save_wydarzenie(request: Request):
    wydarzenie_data = await request.json()
    my_db = db()
    result = my_db.save_wydarzenie(wydarzenie_data)
    return JSONResponse(status_code=201, content=result)

@app.put("/wydarzenie/{id}")
async def put_wydarzenie(id, request: Request):
    wydarzenie_edytuj = await request.json()
    my_db = db()
    result = my_db.put_wydarzenie(id, wydarzenie_edytuj)
    return JSONResponse(status_code=201, content=result)

@app.delete("/wydarzenie/{id}")
async def soft_delete_wydarzenie(id, request: Request):
    id = id
    my_db = db()
    result = my_db.soft_delete_wydarzenie(id)
    return JSONResponse(status_code=201, content=result)

#--------------------------------------------------------------------------------

@app.get("/organizator")
def get_organizator():
    my_db = db()
    return my_db.get_organizator()

@app.post("/organizator")
async def save_organizator(request: Request):
    organizator_data = await request.json()
    my_db = db()
    result = my_db.save_organizator(organizator_data)
    return JSONResponse(status_code=201, content=result)

@app.put("/organizator/{id}")
async def put_organizator(id, request: Request):
    organizator_edytuj = await request.json()
    my_db = db()
    result = my_db.put_organizator(id, organizator_edytuj)
    return JSONResponse(status_code=201, content=result)

@app.delete("/organizator/{id}")
async def soft_delete_organizator(id, request: Request):
    id = id
    my_db = db()
    result = my_db.soft_delete_organizator(id)
    return JSONResponse(status_code=201, content=result)

#--------------------------------------------------------------------------------

@app.get("/adres")
def get_adres():
    my_db = db()
    return my_db.get_adres()

@app.post("/adres")
async def save_adres(request: Request):
    adres_data = await request.json()
    my_db = db()
    result = my_db.save_adres(adres_data)
    return JSONResponse(status_code=201, content=result)

@app.put("/adres/{id}")
async def put_adres(id, request: Request):
    adres_edytuj = await request.json()
    my_db = db()
    result = my_db.put_adres(id, adres_edytuj)
    return JSONResponse(status_code=201, content=result)

@app.delete("/adres/{id}")
async def soft_delete_adres(id, request: Request):
    id = id
    my_db = db()
    result = my_db.soft_delete_adres(id)
    return JSONResponse(status_code=201, content=result)