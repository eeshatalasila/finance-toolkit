import numpy as np
import numpy_financial as npf

def npv(rate, cashflows):
    """Calculate Net Present Value."""
    return sum(cf / (1 + rate) ** i for i, cf in enumerate(cashflows))

def irr(cashflows):
    """Calculate Internal Rate of Return."""
    return npf.irr(cashflows)

def bond_price(face_value, coupon_rate, ytm, years, freq=2):
    """Calculate bond price given YTM."""
    coupon = face_value * coupon_rate / freq
    periods = years * freq

    price = 0
    for t in range(1, periods + 1):
        price += coupon / (1 + ytm / freq) ** t

    price += face_value / (1 + ytm / freq) ** periods
    return price

def capm_expected_return(rf, beta, rm):
    """Expected return using CAPM."""
    return rf + beta * (rm - rf)
