name = input("Please enter your name :")
pin = int(input("Please enter your pin: "))

def auth(name, pin):
    count = 2
    while count > 0:
        if pin == 1234 :
        
            print("Welcome to Python 101")
        
            break
        else:
               print("You have ",count, " attempts remaining")
               pin = int(input("Please enter your pin : "))
               count -= 1
     
    if count == 0:
        print("Your number of attempts have been exhausted :")

    
result = auth(name, pin)
#print (result)
