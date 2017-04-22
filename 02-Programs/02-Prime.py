##a = int(input("Enter the num : "))
##
##if a > 1:
##    
##    for i in range(2,a):
##        if a%i == 0:
##            print("Divided by",i)
##            break
##        else:
##            print("Not Divided by",i)
##
##    else:
##        print("Prime")


min_range = int(input("Enter the min range : "))
max_range = int(input("Enter the max range : "))

for x in range(min_range,max_range):

    if x > 1:

        for num in range(2,x):
            if x%num == 0:
                #print(x,"is not a prime number")
                break
        else:
            print(x,"is prime number")
