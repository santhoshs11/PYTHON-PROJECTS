from secret_art import photo
photo()

bids={}
end = False
def finish(biding_record):
    highest =0
    winner =''
    for bider in biding_record:
        bidding_amount = biding_record[bider]
        if highest<bidding_amount:
            highest = bidding_amount
            winner = bider
    print(f'the winner is {winner},amount :{highest}')        

while not end:
    name = input('enter name : ')
    price = int(input('enter price :'))
    
    continue_ = input('want to continue :')
    bids[name] =price
    print(bids)
    if continue_ == 'no':
        end = True
        finish(bids)    
