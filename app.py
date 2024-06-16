from fastapi import FastAPI, Path, HTTPException, status, Depends, Request, Form, responses
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates')

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", reload=True)

@app.get("/", response_class=HTMLResponse) #Adding template response for basepage
def index(request: Request):
    context = {'request' : request}
    return templates.TemplateResponse("veritycalcV1.html", context)

@app.post("/")
def insideCall(insideCall):
    print(f"{insideCall}")
    return 0