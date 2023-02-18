#collect the required inputs: principal, rate, time
#calculate the monthly payments
#display result

def main():
    print("Interest Loan Calculator")
    print("=========================")

    #define variables
    principal = float(input("Enter your loan amount:|n"))
    annual_pr = float(input("Enter your annual interest rate:\n"))
    period = int(input("Enter the number of years:\n"))

    #write formulas
    monthly_int_rate = annual_pr / 1200
    period_in_months = period * 12
    monthly_payments = principal * monthly_int_rate /(1 - (1 + monthly_int_rate) ** (-period_in_months))


    print(f"Monthly Payment: {monthly_payments}")

main()