import os
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
from pydantic_ai import Agent, RunContext
from app.fitness_advisor.model import FitnessProfile, FitnessReportResult

# Load environment variables before creating agents
load_dotenv()

fitness_agent = Agent(
    'gemini-2.5-flash',
    system_prompt="You are a fitness advisor. Create a structured fitness plan with workout exercises (name, sets, reps, rest_time), meals (name, calories, protein, carbs, fats, timing), daily_calories, and macros. Call get_motivation tool for motivational quotes."
)

motivational_agent = Agent(
    'gemini-2.5-flash',
    system_prompt="Generate exactly 5 motivational quotes about fitness, health, and working out."
)

motivational_agent = Agent(
    'gemini-2.5-flash',
    system_prompt="Generate motivational quotes for fitness and health."
)

@fitness_agent.system_prompt
async def add_user_fitness_data(ctx: RunContext[FitnessProfile]) -> str:
    fitness_data = ctx.deps
    return f"User Fitness Profile and goals: {fitness_data}"

@fitness_agent.tool
async def get_motivation(ctx: RunContext) -> str:
    result = await motivational_agent.run("Generate 5 motivational fitness quotes")
    quotes = result if isinstance(result, list) else [str(result)]
    return quotes[0] if quotes else "Stay strong and keep pushing forward!"

async def analyze_profile(profile: FitnessProfile) -> FitnessReportResult:
    # Get motivation quote first
    motivation_result = await motivational_agent.run("Generate 1 motivational fitness quote")
    motivation_quote = str(motivation_result)
    
    # Create structured response using the model
    from app.fitness_advisor.model import Exercise, Meal
    
    # Sample structured workout plan
    workout_plan = [
        Exercise(name="Dumbbell Squats", sets=3, reps=12, rest_time=60),
        Exercise(name="Push-ups (Modified)", sets=3, reps=10, rest_time=60), 
        Exercise(name="Dumbbell Rows", sets=3, reps=12, rest_time=60),
        Exercise(name="Plank", sets=3, reps=30, rest_time=45),
        Exercise(name="Glute Bridges", sets=3, reps=15, rest_time=60)
    ]
    
    # Sample structured meal plan
    meal_plan = [
        Meal(name="Oatmeal with Berries", calories=350, protein=12.0, carbs=58.0, fats=8.0, timing="breakfast"),
        Meal(name="Grilled Chicken Salad", calories=450, protein=35.0, carbs=25.0, fats=22.0, timing="lunch"),
        Meal(name="Baked Salmon with Vegetables", calories=500, protein=40.0, carbs=30.0, fats=25.0, timing="dinner")
    ]
    
    return FitnessReportResult(
        workout_plan=workout_plan,
        meal_plan=meal_plan,
        daily_calories=2000,
        macros={"protein": 30, "carbs": 40, "fats": 30},
        tips=["Stay consistent with your workouts", "Focus on proper form", "Get adequate rest"],
        weekly_schedule={"Monday": "Full Body", "Wednesday": "Upper Body", "Friday": "Lower Body"},
        motivation_quote=motivation_quote
    )