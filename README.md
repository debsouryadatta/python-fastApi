### FastAPI with MongoDB (CWH)
1. Mongo Types Basics
2. Installing FastApi and basic api
3. Serving static files & templates(Using Jinja2)
4. Installing Pymongo and connecting to MongoDB
5. Testing Read endpoint with MongoDB
6. Building the basic frontend for our notes app and rendering the notes

7. Best Practices -> 
index.py for main app,
routes folder for routes,
models folder for models,
config folder for db connection, 
schemas folder to convert mongodb object to pydantic dict
* We need to write schemas twice, once for pydantic and once for mongodb

8. Shifting code to routes folder(best practices)
9. pip install python-multipart
10. Creating post request to add notes also changing html form and jinja2 elements