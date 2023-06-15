# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Pmt = r * PV/(1-(1+r)**-n)
pmt is how much you back/mo
n is number of months
r is interest rate per month
n is number f months 
"""

def Idunno(PV, r, n):
    """
    

    Parameters
    ----------
    PV : TYPE float
        DESCRIPTION. present value (amt borrow)
    r : TYPE float
        DESCRIPTION. interest rate PAR
    n : TYPE integer 
        DESCRIPTION. number of months to pay back loan 

    Returns
    -------
    Pmt : TYPE float 
        DESCRIPTION. amt paid per month
    """
    
    Pmt = r * PV/(1-(1+r)**-n)
    return Pmt

# input the PV
import numpy as np


n = 48
PV = input('enter PV: ')
PV = float(PV)

#equivalently PV = float(input('enter PF: '))
print(f"PV = {PV} \n")

r = input('interest APR: ')
r = float(r)/100
r = r/12

print(f"interest = {r: 0.2f}")


pmt = Idunno(PV, r, n)
pmt = np.round(pmt, 2)
print(f"payment is {pmt: } per month")
 
