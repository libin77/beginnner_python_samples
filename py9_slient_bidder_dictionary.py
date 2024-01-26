from replit import clear #https://replit.com/
from art import logo_bidder

any_new_bidder = True
bid_data = {}

print(logo_bidder)

def find_highest_bidder(bid_data):
  highest_amount = 0
  winner = ""
  for name in bid_data:
    if bid_data[name] > highest_amount:
      highest_amount = bid_data[name]
      winner = name
  print(f"The winner is {winner} with a bid of ${highest_amount}.")

while any_new_bidder:
  name = input("What is your name?: ")
  amount = int(input("What's your bid?: $"))
  new_bidder = input("Any more bidder (Yes/No): ")

  bid_data[name] = amount
  
  if new_bidder.lower() == "no":
    any_new_bidder = False
    
  clear()
  print(logo_bidder)
  
find_highest_bidder(bid_data)
