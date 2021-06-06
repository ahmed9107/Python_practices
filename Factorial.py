# -------------------
# --- Ahmed Azami ---
# -------------------
# ---- Factorial ----
# -------------------


x = int(input("Enter any number: "))

def factorial(n):

    if n < 0 :
        raise ValueError("You must enter a positive number")
    elif n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(x))