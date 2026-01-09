import numpy as np
from src.finance import npv, irr, bond_price, capm_expected_return

cashflows = [-1000, 200, 300, 400, 500]

print("NPV:", round( npv(0.10, cashflows)), 2)
print("IRR:", round(irr(cashflows),4))
print("Bond Price:", round(bond_price(1000, 0.05, 0.04, 10),2))
print("CAPM Return:", round(capm_expected_return(0.02, 1.3, 0.08),2))