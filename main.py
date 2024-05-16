

# from typing import Union

# from fastapi import FastAPI, Request, Response
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from pymongo import MongoClient

# app = FastAPI()

# # Serving static files to be used in the templates
# app.mount("/static", StaticFiles(directory="static"), name="static") 

# templates = Jinja2Templates(directory="templates")

# con = MongoClient("mongodb+srv://Neel:lovecoding@cluster0.qymvclt.mongodb.net/fastapi_cwh?retryWrites=true&w=majority&appName=Cluster0")


#  # Serving templates - Following fastapi template docs
# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):  
#     docs = con.fastapi_cwh.notes.find({})
#     newDocs = []
#     for doc in docs:
#         newDocs.append({
#             "id": doc["_id"],
#             "note": doc["note"]
#         })
#     return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}