# for the first number enter the number you want m to be divided by
# for the 2nd number enter when you would want to divid n by
# basically we are doing m/n and if m can be diveded by n then n is a muliple of m 

def is_multiple():
    print("Is n a multiple of m?")
    n= int(input( "enter 1st number for n: "))
    m= int(input( "enter 2nd number m: "))
    if m % n == 0:
        print( "True! n is a multiple of m")
    if m % n != 0:
        print( "False! n is NOT a multiple of m")
            
            
is_multiple()