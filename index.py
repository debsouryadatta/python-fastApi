from fastapi import FastAPI
from routes.note import note
from fastapi.staticfiles import StaticFiles


app = FastAPI()
# Serving static files to be used in the templates
app.mount("/static", StaticFiles(directory="static"), name="static") 


# Adding routes to our main app
app.include_router(note)