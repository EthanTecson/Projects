"""
Created on Sun Nov 20 14:12:34 2022

@author: ethantecson
"""
"""
     Author/copyright: Ethan Tecson.  All rights reserved.
     Used with permission and modified by: WhoeverModifiesIt
     Date: 20 November 2022
"""
#######################################################################
def average_salary(total, tax, down_payment, term, maintenance, insurace):
    """
          Parameters:
          Returns:
    """
    print(total)
    tax = tax * .01
    total = total + total * tax
    print(total)
    down_payment = down_payment * .01
    down_payment = total * down_payment
    total = total - down_payment
    monthly_total = total / term
    print(monthly_total)
    monthly_maintenance = maintenance / 12
    monthly_insurance = insurace / 12
    monthly_total = monthly_total + monthly_insurance + monthly_maintenance
    print(total)
    answer = monthly_total * 10 * 12

    print('$' + str(answer))
######################################################################
def main():
     """
     This main function...
     """
     auto_cost = int(input('Total Cost of Car: '))
     tax_rate = int(input('Tax Rate in State (In Percentage): %'))
     down_payment = int(input('Down Payment (In Percentage): %'))
     desired_loan_term = int(input('Desired Loan Term (# of Months): '))
     maintenance = int(input('Average Maintenance Cost (Yearly): '))
     insurance = int(input('Average Insurance Cost (Yearly): '))
     average_salary(auto_cost, tax_rate, down_payment, desired_loan_term, maintenance, insurance)
######################################################################
main()
