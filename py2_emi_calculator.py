# EMI Calculator
# [P x R x (1+R)^N]/[(1+R)^N-1]
principal_amt = input("What is the total loan amount? Rs ")
rate_of_interest = input("What is the rate of interest? ")
num_months = input("Select tenure in months ")

# calculation
rate = float(rate_of_interest)/12/100
compounding_factor = (1 + rate) ** int(num_months)
emi = (int(principal_amt) * rate * compounding_factor) / (compounding_factor - 1)

# f-string support any datatype values
print(f"Your monthly emi will be Rs {round(emi,2)}")
