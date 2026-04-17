n = int(input("How many numbers? ")) 
for i in range(n): 
    num = float(input("Enter number: ")) 
    if num > 0: 
        print("Positive") 
    elif num < 0: 
        print("Negative") 
    else: 
        print("Zero")