#Assumption: Stocks can be bought and sold on same day

def main():
    n = int(input())
    stocks = [int(i) for i in input().split()]
    
    max_price = stocks[n-1]
    max_profit = 0
    ptr = n-2
    day = n-1
    
    while(ptr >=0):
        if stocks[ptr] > max_price:
            max_price = stocks[ptr]
        
        if max_price - stocks[ptr] >= max_profit:
            max_profit = max_price - stocks[ptr]
            day = ptr + 1
            
        ptr -= 1
    
    print(max_profit)
    print(day)
            
main()