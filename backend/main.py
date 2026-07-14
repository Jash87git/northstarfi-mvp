from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.database import SessionLocal, FireScenario, create_tables
from backend.services.fire_calculator import calculate_fire
from backend.services.portfolio_analyzer import analyze_portfolio
from backend.services.ai_advisor import get_ai_advice

app = FastAPI(title="NorthstarFI API")
create_tables()

class FireRequest(BaseModel):
    name: str
    age: int
    current_portfolio: float
    monthly_investment: float
    monthly_expenses: float
    expected_return: float = 7.0
    withdrawal_rate: float = 4.0
    us_stocks: float = 0
    international_stocks: float = 0
    bonds: float = 0
    cash: float = 0

class ChatRequest(BaseModel):
    question: str
    context: str = ""

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def health_check():
    return {"status": "NorthstarFI API is running"}

@app.post("/calculate")
def calculate(request: FireRequest, db: Session = Depends(get_db)):
    fire_result = calculate_fire(
        request.age,
        request.current_portfolio,
        request.monthly_investment,
        request.monthly_expenses,
        request.expected_return,
        request.withdrawal_rate
    )

    portfolio_result = analyze_portfolio(
        request.us_stocks,
        request.international_stocks,
        request.bonds,
        request.cash
    )

    scenario = FireScenario(
        name=request.name,
        age=request.age,
        current_portfolio=request.current_portfolio,
        monthly_investment=request.monthly_investment,
        monthly_expenses=request.monthly_expenses,
        expected_return=request.expected_return,
        withdrawal_rate=request.withdrawal_rate,
        fire_number=fire_result["fire_number"],
        years_to_fire=fire_result["years_to_fire"],
        fire_age=fire_result["fire_age"]
    )
    db.add(scenario)
    db.commit()

    ai_context = f"""
    User: {request.name}
    Age: {request.age}
    Current portfolio: ${request.current_portfolio}
    Monthly investment: ${request.monthly_investment}
    Monthly expenses: ${request.monthly_expenses}
    FIRE number: ${fire_result['fire_number']}
    Years to FIRE: {fire_result['years_to_fire']}
    FIRE age: {fire_result['fire_age']}
    Portfolio analysis: {portfolio_result}
    Give educational FIRE improvement suggestions.
    """
    ai_advice = get_ai_advice(ai_context)

    return {
        "fire_result": fire_result,
        "portfolio_result": portfolio_result,
        "ai_advice": ai_advice
    }

@app.post("/chat")
def chat(request: ChatRequest):
    prompt = f"Context: {request.context}\n\nQuestion: {request.question}"
    return {"answer": get_ai_advice(prompt)}
