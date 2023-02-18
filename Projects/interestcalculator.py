#collect the required inputs: principal, rate, time
#calculate the monthly payments
#display result


print("Interest Loan Calculator")
print("=========================")
start_calculator = input("Calculate a loan payment?(Y/N):\n").upper()

def main():

    #define variables
    principal = float(input("Enter your loan amount:\n"))
    annual_pr = float(input("Enter your annual interest rate:\n"))
    period = int(input("Enter the number of years:\n"))
    

    #write formulas
    monthly_int_rate = annual_pr / 1200
    period_in_months = period * 12
    monthly_payments = principal * monthly_int_rate /(1 - (1 + monthly_int_rate) ** (-period_in_months))

    #display monthly payment formatted to 2d.p
    print(f"Monthly Payment: ${monthly_payments:.2f}\n")

while(start_calculator == "Y"):
    main()
    start_calculator = input("Calculate a loan payment?(Y/N):\n").upper()
    





