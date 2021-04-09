from art import logo
from replit import clear
print (logo)
bids={}
to_contiune=True

def heighest_bidder(bidding_record):
  highest_amount=0
  heighest_bidder="none"
  for key in bidding_record:
    if (bidding_record[key]>highest_amount):
      highest_amount=bidding_record[key]
      heighest_bidder=key
  print(bidding_record)
  print(f"highest_bidder is {heighest_bidder}   and the bid amount is {highest_amount}")

while to_contiune:
  name=input ("What is your name\n")
  bid_amount=int(input("What is the bid amount Rs \n"))
  bids[name]=bid_amount
  if (input("Are there any other bidders\n")=='yes'):
    clear()
  else:
    to_contiune=False
heighest_bidder(bids)











