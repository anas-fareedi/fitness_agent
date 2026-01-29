import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.fitness_advisor.controller import router

load_dotenv()

app = FastAPI(title="AI fitness trainer")

app.include_router(router)