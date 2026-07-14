def calculate_fire(age: int, current_portfolio: float, monthly_investment: float,
                   monthly_expenses: float, expected_return: float,
                   withdrawal_rate: float) -> dict:
    """
    Basic FIRE calculation.
    expected_return and withdrawal_rate should be percentages, e.g. 7 and 4.
    """
    annual_expenses = monthly_expenses * 12
    fire_number = annual_expenses / (withdrawal_rate / 100)

    monthly_return = (expected_return / 100) / 12
    portfolio = current_portfolio
    months = 0
    max_months = 100 * 12

    while portfolio < fire_number and months < max_months:
        portfolio = portfolio * (1 + monthly_return) + monthly_investment
        months += 1

    years_to_fire = months / 12
    fire_age = age + years_to_fire

    return {
        "annual_expenses": round(annual_expenses, 2),
        "fire_number": round(fire_number, 2),
        "years_to_fire": round(years_to_fire, 1),
        "fire_age": round(fire_age, 1),
        "projected_portfolio": round(portfolio, 2)
    }
