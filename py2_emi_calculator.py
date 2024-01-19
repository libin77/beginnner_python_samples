def emi_calculator:
  #EMI Calculator
  #[P x R x (1+R)^N]/[(1+R)^N-1] 
  principal_amt = input("What is the total loan amount? Rs ")
  rate_of_intr = input("What is the rate of interest? ")
  num_months = input("Select tenure in months ")

  #calculation
  rate  = float(rate_of_intr)/12/100
  compunding_factor = (1+rate)**int(num_months)
  emi = (int(principal_amt) * rate * compunding_factor) / (compunding_factor - 1)

  print(f"Your montly emi will be Rs {round(emi,2)}")
