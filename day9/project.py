auction={}
finished = False

def find_highest(bidding_record):
    highest_bid = 0
    for person in bidding_record:
        amount = bidding_record[person]
        if amount > highest_bid:
            highest_bid = amount
            winner = person
    print(f"The winner is {winner}, with ${highest_bid}")
            
while not finished:
    Name = input("Type name: ")
    Price =int(input("Enter Bid price: $"))
    auction[Name] = Price
    bidder = input("Is there any other Bidder. type 'yes' or 'No'")
    if bidder == "No":
        finished=True
        find_highest(auction)
        
