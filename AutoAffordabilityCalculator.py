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
    This function will take the total cost of an automobile and run it 
    through calculations including tax, down payment, payment term, maintenance,
    and insurance to produce an average salary needed to COMFORTABLY afford the
    chosen autombile based off of the 10% of income rule. 
          Parameters:
               total -- initial total cost of automobile
               tax -- tax rate based off state expressed as percentage
               down_payment -- desired down payment expressed as percentage
               term -- desired loan term 
               maintenance -- average maintenance cost of automobile 
               insurace -- average insurance cost of automobile 
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
     This main function will prompt the user to input the total cost of the car,
     tax rate in state (becasue this varies based off of state), down payment in percentage,
     desired loan term, average mintenance cost, and average insurance cost. The function
     will then take all inputs and use them as the parameters of the average_salary() function. 
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
