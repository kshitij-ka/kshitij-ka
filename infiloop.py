# Description: A menu driven, random character generator.

## BEGINNING OF CODE

# Importing modules
import random, string, time

# Declaring variables
speed=0
quantity=int()
n=1

# Generate gibberish using built-in string and random modules.
def generator(quantity):
    txt=''.join(random.choice(string.ascii_letters) for _ in  range(quantity))
    return txt

# Print the randomly generated text at user defined speed and quantity.
def printer():
    global n
    while (n<=quantity):
        gen=generator(n)
        print(n, "->", gen)
        n+=1
        time.sleep(speed)

# Select the speed at which text is displayed.
def speed_optn():
    global speed
    print("\n----- SPEED SELECTION -----")
    print("1 -> Silly")
    print("2 -> Mili")
    print("3 -> Bili")
    print("4 -> I'm Feeling Lucky 🌟")
    print("5 -> Exit now (last chance)")
    speed=int(input("Select an option (1-5):\t"))
    if (speed==1): #Silly
        speed=0.040
    elif (speed==2): #Mili
        speed=0.027
    elif (speed==3): #Bili
        speed=0.010
    elif (speed==4):
        speed=0.001
    elif (speed==5):
        print("\n\n##DESIGNED AND ENGINEERED BY KSHITIJ\n")
        quit()
    else:
        print("\n\nPlease choose a valid option.\n\n")
        speed_optn()

# Select the quantity of gibberish content to be displayed.
def rand_optn():
    global quantity,n
    while True:
        print("\n----- RANDOMNESS OPTIONS -----")
        print("1 -> Genhun")
        print("2 -> Genfou")
        print("3 -> Geneter 🌟")
        print("4 -> Exit now (i'm scared)")
        quantity=int(input("Choose quantity of randomness (CHOOSE WISELY):\t"))
        speed_optn()
        if (quantity==1):
            quantity=100
            printer()
            print("\n\n##DESIGNED AND ENGINEERED BY KSHITIJ\n\n")
        elif (quantity==2):
            quantity=500
            printer()
            print("\n\n##DESIGNED AND ENGINEERED BY KSHITIJ\n\n")
        elif (quantity==3):
            print("\n\n##DESIGNED AND ENGINEERED BY KSHITIJ\n\n")
            while True:
                quantity+=1
                printer()
        elif (quantity==4):
            print("\n\n## DESIGNED AND ENGINEERED BY KSHITIJ")
            quit()
        else:
            print("\n\nPlease choose a valid option.\n\n")
            rand_optn()
        n=1
        speed=0
        quantity=0
        #print("N:\t", n,"\nSpeed:\t", speed, "\nQuantity:\t", quantity) # For debugging purposes

rand_optn()
## END OF CODE
