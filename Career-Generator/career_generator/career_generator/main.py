from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from career_generator.engine import ConversationEngine, Pipeline
from career_generator.career_engine import suggest_careers

app = FastAPI()

class UserResponse(BaseModel):
    interests: str
    skills: str
    work_style: str
    environment: str
    values: str

class CareerPipeline(Pipeline):
    def run(self, inputs):
        return suggest_careers(inputs)

career_pipeline = CareerPipeline()
engine = ConversationEngine(pipelines={"career": career_pipeline})

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    return FileResponse("static/index.html")

@app.post("/generate-career")
def generate_career(user_response: UserResponse):
    input_data = user_response.dict()
    result = engine.run("career", input_data)
    return {
        "message": "Based on your answers, these careers suit you best:",
        "careers": result
    }

