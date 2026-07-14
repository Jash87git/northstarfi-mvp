def analyze_portfolio(us_stocks: float, international_stocks: float, bonds: float, cash: float) -> dict:
    total = us_stocks + international_stocks + bonds + cash
    if total <= 0:
        return {"error": "Portfolio total must be greater than zero."}

    allocation = {
        "us_stocks_pct": round(us_stocks / total * 100, 1),
        "international_stocks_pct": round(international_stocks / total * 100, 1),
        "bonds_pct": round(bonds / total * 100, 1),
        "cash_pct": round(cash / total * 100, 1),
        "total": round(total, 2)
    }

    risk_notes = []
    equity_pct = allocation["us_stocks_pct"] + allocation["international_stocks_pct"]

    if equity_pct > 85:
        risk_notes.append("High equity exposure. Good for growth, but higher short-term risk.")
    elif equity_pct < 50:
        risk_notes.append("Conservative allocation. Lower volatility, but may slow FIRE progress.")
    else:
        risk_notes.append("Balanced equity exposure for long-term planning.")

    if allocation["cash_pct"] > 20:
        risk_notes.append("Cash allocation is high. Consider whether excess cash can be invested.")

    return {"allocation": allocation, "risk_notes": risk_notes}
