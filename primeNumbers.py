list = [2, 4, 3, 5, 6, 7, 8, 9]
#find prime numbers
#prime numbers are natural numbers>1 and which only divide by 1 and itself
# therefore if count variable value only increment two in condition modulus 0 then it is prime numnber

for num in list:
    if num > 1:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            print(num)
                    
                
                        
    
                
                
            
    
    
        
    
    


