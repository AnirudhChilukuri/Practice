import argparse

cde = []
# A default function for Prime checking conditions  
def PrimeChecker(a,cde):  
    # Checking that given number is more than 1  
    if a > 1:  
        # Iterating over the given number with for loop  
        for j in range(2, int(a/2) + 1):  
            # If the given number is divisible or not  
            if (a % j) == 0:  
                print(a, "is not a prime number")  
                break  
        # Else it is a prime number  
        else:  
            print(a, "is a prime number")
            cde.append(a)
    # If the given number is 1  
    else:  
        print(a, "is not a prime number") 



parser = argparse.ArgumentParser()
parser.add_argument("--para1", type=int, nargs='+')
args = vars(parser.parse_args())

for i in args['para1']:
    print(PrimeChecker(i, cde))