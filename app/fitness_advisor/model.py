from pydantic import BaseModel,Field
from typing import List, Optional 
from enum import Enum

class ActivityLevel(str, Enum):
    SEDENTARY = 'sedentary'
    LIGHT = 'light'
    MODERATE = 'moderate'
    ATHLETE = 'athlete'
    VERY_ACTIVE = 'very_active'

class FitnessGoal(str, Enum):
    LOSE_WEIGHT = 'lose_weight'
    MAINTENANCE = 'maintenance'
    GAIN_MUSCLE = 'gain_muscle'
    ENDURANCE = 'endurance'
    STRENGTH = 'strength'

class FitnessProfile(BaseModel):
    age: int 
    weight: float  
    height: float  
    gender: str
    activity_level: ActivityLevel  
    fitness_goal: FitnessGoal
    dietary_restrictions : List[str] = []
    injuries : List[str] = []
    preferred_workout_time:str
    available_equipment : List[str] = []
    workout_days_per_week: int

class Exercise(BaseModel):
    name:str
    sets:int
    reps:int
    rest_time:int  = Field(..., description="rest time in seconds")

class Meal(BaseModel):
    name:str
    calories:int
    protein:float    
    carbs:float
    fats:float
    timing:str = Field(..., description="breakfast, lunch, dinner")

class FitnessReportResult(BaseModel):
    workout_plan: List[Exercise] = Field(description="customized workout plan based on the user's fitness profile")
    meal_plan: List[Meal] = Field(description="daily meal plan")
    daily_calories: int = Field(description="recommended daily calories")
    macros: dict = Field(description="recommended macro split (protein, carbs, fats)")
    tips: List[str] = Field(description="personalized fitness and nutrition tips")
    weekly_schedule: dict = Field(description="weekly workout and meal schedule")
    motivation_quote: str = Field(description="motivational quote")