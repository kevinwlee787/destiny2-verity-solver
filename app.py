from fastapi import FastAPI, Path, HTTPException, status, Depends, Request, Form, responses
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

class Calls(BaseModel):
    insidedata: str
    left: int
    middle: int #base model for json request pkg can change type 
    right: int

app = FastAPI()

templates = Jinja2Templates(directory='templates') #templates for easy page display

if __name__ == "__main__": #starts and runs the app
    uvicorn.run("app:app", host="127.0.0.1", reload=True)

@app.get("/", response_class=HTMLResponse) #Adding template response for basepage
def index(request: Request):
    context = {'request' : request}
    return templates.TemplateResponse("veritycalcV1.html", context) #go to what template we assigne 

@app.post("/")
def insideCall(calls: Calls):
    print(f"{calls.insidedata}, {calls.left}, {calls.middle}, {calls.right}") #testing to get userinput into api layer
    return 0