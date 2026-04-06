import os
print("****welcome to silent auction program****")
def find_winner(bidder_details):
    highest_bid=0
    winner=""
    for bidder in bidder_details:
        bidding_price=bidder_details[bidder]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(f"here is the list of all bidders:{bidder_details}")
    print(f"the winner is {winner} with a bid price of {highest_bid}")
bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("what is your name?:")
    price=int(input("what is your bid?:"))
    bidder_data[name]=price
    more_bidders=input("are there more bidders? type 'yes' or 'no':").lower()
    if more_bidders=='no':
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')
        
