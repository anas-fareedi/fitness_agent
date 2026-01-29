from fastapi import APIRouter, FastAPI
from app.fitness_advisor.model import FitnessProfile
from app.fitness_advisor.service import analyze_profile

router =APIRouter()

@router.post("/analyze")
async def analyze_fitness(fitness_profile: FitnessProfile):
    return await analyze_profile(fitness_profile)
