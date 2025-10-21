"""
WACC Calculation Function
Reusable component for API or app use.
"""

def calculate_wacc(equity_value, debt_value, cost_of_equity, cost_of_debt, tax_rate):
    """Return WACC (%) rounded to 2 dp."""
    total_value = equity_value + debt_value
    if total_value == 0:
        raise ValueError("Total capital cannot be zero.")
    w_e = equity_value / total_value
    w_d = debt_value / total_value
    wacc = (w_e * cost_of_equity) + (w_d * cost_of_debt * (1 - tax_rate))
    return round(wacc * 100, 2)
