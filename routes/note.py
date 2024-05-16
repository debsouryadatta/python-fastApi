from fastapi import APIRouter, Request, Response
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


note = APIRouter()
templates = Jinja2Templates(directory="templates")


 # Serving templates - Following fastapi template docs
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):  
    docs = conn.fastapi_cwh.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            # "important": doc["important"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    print(formDict)
    # formDict["important"] = True if formDict["important"] == "on" else False
    note = conn.fastapi_cwh.notes.insert_one(formDict)
    return {"Success": "Note added successfully!"}
    