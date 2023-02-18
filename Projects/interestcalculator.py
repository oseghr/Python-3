#collect the required inputs: principal, rate, time
#calculate the monthly payments
#display result

def main():
    print("Interest Loan Calculator")
    print("=========================")

    principal = float(input("Enter your loan amount:|n"))
    apr = float(input("Enter your annual interest rate:\n"))
    period = int(input("Enter the number of years:\n"))

    