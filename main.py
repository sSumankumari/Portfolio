from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# Mount a static directory for serving CSS and JavaScript files
app.mount("/static", StaticFiles(directory="static"), name="static")
template = Jinja2Templates(directory="template")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=5000)