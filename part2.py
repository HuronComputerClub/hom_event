#Number guessing game
#player thinks of the number, computer guesses

low = 0
high = 100

print("Guess a number between",low,"and",high)

input("press enter when ready\n")

count = 0  #number of guesses
guess = int((high+low)/2) #the first guess, can make this randint(low,high) too

response = ""
while response != "c":
    response = input("\nIs it " + str(guess) + "? (h=too high, l=too low, c=correct) ")

    if response!="l" and response!="h" and response!="c":
        print("invalid response. Please enter 'l', 'h', or 'c'")
        count -= 1
        
    if response == "l":
        low = guess + 1
    elif response == "h":
        high = guess - 1
        
    guess =  int((high+low)/2) 
    count+=1
print("I won in", count, "guesses!!!")
    
