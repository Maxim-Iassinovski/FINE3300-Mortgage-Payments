#Function calculates the pva factor given a rate and number of payments
def calculate_pva(r, n):

    return (1 - (1 + r) ** -n) / r

#Function calculates the mortgage payments for each payment frequency, given principal amount, rate and # of amortization years
def mortgage_payments(principal, rate, amortization): 

    #Convert interest rate to decimal form
    rate = rate / 100

    #Calculate the periodic rate for each payment frequency
    monthly_r = (1 + rate / 2)**(2/12) - 1
    semi_monthly_r = (1 + rate / 2)**(2/24) - 1
    biweekly_r = (1 + rate / 2)**(2/26) - 1
    weekly_r = (1 + rate / 2)**(2/52) - 1

    #Calculate the pva for each payment frequency
    monthly_pva = calculate_pva(monthly_r, 12*amortization)
    semi_monthly_pva = calculate_pva(semi_monthly_r, 24*amortization)
    biweekly_pva = calculate_pva(biweekly_r, 26*amortization)
    weekly_pva = calculate_pva(weekly_r, 52*amortization)

    #Calculate mortgage payments for each payment frequency
    monthly_payment = principal / monthly_pva
    semi_monthly_payment = principal / semi_monthly_pva
    biweekly_payment = principal / biweekly_pva
    weekly_payment = principal / weekly_pva
    rapid_biweekly_payment = monthly_payment / 2
    rapid_weekly_payment = rapid_biweekly_payment / 2

    #Return mortgage payments as a tuple
    return (
        round(monthly_payment, 2),
        round(semi_monthly_payment, 2),
        round(biweekly_payment, 2),
        round(weekly_payment, 2),
        round(rapid_biweekly_payment, 2),
        round(rapid_weekly_payment, 2)
    )

#Prompt user for required information
print("Please enter the principal amount")
principalAmt = int(input())

print("Please enter the quoted interest rate as a percentage")
interestRate = float(input())

print("Please enter the amortization period in years")
amortizationPeriod = int(input())
print("")

#Assign payments to the tuple of mortgage payments returned in the function
payments = mortgage_payments(principalAmt, interestRate, amortizationPeriod)

#Print payments by indexing the tuple
print("Monthly Payment: ", payments[0])
print("Semi-monthly Payment: ", payments[1])
print("Bi-weekly Payment: ", payments[2])
print("Weekly Payment: ", payments[3])
print("Rapid Bi-weekly Payment: ", payments[4])
print("Rapid Weekly Payment: ", payments[5])
print("")