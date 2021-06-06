# Write any number
n = int(input())

# define a num varible
num = False

# Check if the number greater than 1
if n > 1:
    
    # Check for the factors
    for x in range(2, int(pow(n, 1/2) + 1)):
        if n % x == 0:
        
            # If factor found, num=True
            num = True
            
            # Stop the loop
            break

# If the number less or equal 1
else:
    num = True
    
# Check if the num true or false
if num:
    print (str(n) + " Is not a prime number")
    
else:
    print (str(n) + " Is a prime number")


