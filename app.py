import streamlit as st
from wacc_function import calculate_wacc
import json

st.set_page_config(page_title="💸 WACC API", layout="centered")

# Read query parameters (?equity_value=...&debt_value=...)
params = st.query_params

st.title("💸 Weighted Average Cost of Capital (WACC) API")

if params:
    try:
        equity_value   = float(params.get("equity_value", [0])[0])
        debt_value     = float(params.get("debt_value", [0])[0])
        cost_of_equity = float(params.get("cost_of_equity", [0])[0])
        cost_of_debt   = float(params.get("cost_of_debt", [0])[0])
        tax_rate       = float(params.get("tax_rate", [0])[0])

        result = calculate_wacc(equity_value, debt_value, cost_of_equity, cost_of_debt, tax_rate)
        st.json({"WACC (%)": result})

    except Exception as e:
        st.json({"error": str(e)})

else:
    st.markdown(
        """
        ### Usage  
        Call this API with query parameters, e.g.:

        ```
        ?equity_value=12000
        &debt_value=2000
        &cost_of_equity=0.10
        &cost_of_debt=0.067
        &tax_rate=0.25
        ```

        Example full URL (after deployment):
        ```
        https://amcbhome-wacc-api.streamlit.app/?equity_value=12000&debt_value=2000&cost_of_equity=0.10&cost_of_debt=0.067&tax_rate=0.25
        ```
        """
    )
