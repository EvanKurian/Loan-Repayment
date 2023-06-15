#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:36:04 2023

@author: evankurian
"""

def calculate_monthly_repayment(PV, r, n):
    """
    Calculates the monthly repayment amount for a loan.
    
    PV: Present Value (loan amount)
    r: Annual interest rate as a decimal (APR)
    n: Number of months
    
    Returns: Monthly repayment amount
    """
    r = r / 100  # Convert APR to decimal
    
    # Calculate the monthly repayment amount
    Pmt = r * PV / (1 - (1 + r) ** -n)
    
    return Pmt


# Example usage
PV = 12000  # Present Value (loan amount)
r = 7.45  # Annual interest rate (APR)
n = 48  # Number of months

monthly_repayment = calculate_monthly_repayment(PV, r, n)
print("Monthly repayment amount: $", round(monthly_repayment, 2))
